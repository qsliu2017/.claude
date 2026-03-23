#!/bin/bash
if [ -z "$ANTHROPIC_BASE_URL" ] || [ -z "$ANTHROPIC_CUSTOM_HEADERS" ]; then
  echo "Error: ANTHROPIC_BASE_URL and ANTHROPIC_CUSTOM_HEADERS must be set"
  exit 1
fi

