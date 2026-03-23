#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.8"
# ///
import json, sys, subprocess, os

GREEN, YELLOW, RED, BLUE, RESET = '\033[32m', '\033[33m', '\033[31m', '\033[34m', '\033[0m'
BOLD_RED = '\033[1;31m'  # Bold + Red combined
BOLD_BLUE = '\033[1;34m'
BOLD_CYAN = '\033[1;36m'

def color(color, content):
    return f"{color}{content}{RESET}"

def pct_color(pct):
    if pct >= 80: return RED
    if pct >= 50: return YELLOW
    return GREEN

def format_duration(seconds):
    if seconds <= 0:
        return "0m"
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    if hours >= 24:
        days = hours // 24
        hours = hours % 24
        return f"{days}d{hours}h" if hours else f"{days}d"
    if hours:
        return f"{hours}h{minutes}m" if minutes else f"{hours}h"
    return f"{minutes}m"

WINDOW_LABELS = {'five_hour': '5h', 'seven_day': '7d'}

def format_rate_limits(data):
    rl = data.get('rate_limits')
    if not rl:
        return ""
    import time
    now = time.time()
    parts = []
    for key, label in WINDOW_LABELS.items():
        window = rl.get(key)
        if window:
            pct = window.get('used_percentage', 0)
            resets_at = window.get('resets_at', 0)
            remaining = max(0, int(resets_at - now))
            parts.append(f"{color(pct_color(pct), f'{pct:.0f}%')}({format_duration(remaining)}/{label})")
    return " ".join(parts) if parts else ""

def format_context(data):
    cw = data.get('context_window')
    if not cw:
        return ""
    pct = cw.get('used_percentage', 0)
    return f"ctx:{color(pct_color(pct), f'{pct}%')}"

data = json.load(sys.stdin)
directory = os.path.relpath(data['workspace']['current_dir'], data['workspace']['project_dir'])
rate_info = format_rate_limits(data)
ctx_info = format_context(data)

try:
    subprocess.check_output(['git', 'rev-parse', '--git-dir'], stderr=subprocess.DEVNULL)
    branch = subprocess.check_output(['git', 'branch', '--show-current'], text=True).strip()
    staged_output = subprocess.check_output(['git', 'diff', '--cached', '--numstat'], text=True).strip()
    modified_output = subprocess.check_output(['git', 'diff', '--numstat'], text=True).strip()
    staged = len(staged_output.split('\n')) if staged_output else 0
    modified = len(modified_output.split('\n')) if modified_output else 0

    git_status = f"{GREEN}+{staged}{RESET}" if staged else ""
    git_status += f"{YELLOW}~{modified}{RESET}" if modified else ""

    print(f"{color(BOLD_CYAN, directory)} {color(BOLD_BLUE, 'git:(')}{color(BOLD_RED, branch)}{color(BOLD_BLUE, ')')} {git_status} {ctx_info}\n{rate_info}")
except:
    print(f"{directory}{ctx_info}\n{rate_info}")
