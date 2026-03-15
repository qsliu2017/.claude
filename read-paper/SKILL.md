---
name: read-paper
description: Read and summarize academic papers (PDF files or URLs). Use this skill whenever the user provides a paper — via @file, a URL to a PDF or arXiv page, or asks you to review/summarize/read a research paper. Also trigger when the user says things like "what's this paper about", "summarize this", or "give me the key takeaways" alongside a paper file or link.
---

# Read Paper

Produce a concise, structured review of an academic paper. The goal is to help the reader quickly understand what the paper does, what it found, and how it was evaluated — without having to read the full text.

## Getting the Paper

- **@file (PDF)**: Read the file directly. For large PDFs, read in page ranges (e.g., start with pages 1-15 to get abstract, intro, and core contribution, then read the evaluation sections).
- **URL**: If it's an arXiv URL, fetch the abstract page first to get the overview, then fetch the PDF if needed for evaluation details. For other URLs, fetch and extract the content.

Read enough of the paper to confidently fill in every section of the review. At minimum: the abstract, introduction, core contribution/method section, and evaluation/experiments section. If the paper is long, skim middle sections and focus on the parts that inform the review.

## Review Format

Output the review in exactly this structure:

### Overview
_3 sentences._ What problem does this paper address? What approach do the authors take? What is the main contribution?

### Key Findings
_2-3 sentences._ What are the most important results or takeaways? Focus on what a reader would want to remember a week later.

### System
_1 sentence._ What system or artifact is being evaluated, and how was it designed, modified, or extended?

### Evaluation
_1 sentence._ What workloads, benchmarks, or datasets were used to evaluate the system?

## Writing Guidelines

- Be specific and concrete. Instead of "the system performs well", say what metric improved by how much.
- Use the paper's own terminology for system names, benchmark names, and metrics.
- Don't editorialize or critique — just report what the paper says.
- Keep each section to exactly the sentence count specified. This forces precision.

## Non-Systems Papers

Most papers will be systems or CS papers with clear benchmarks and evaluation. When a paper doesn't fit that mold (theoretical work, surveys, position papers), adapt:

- **System** → describe the main artifact, framework, or formalism instead
- **Evaluation** → describe what evidence or analysis the authors provide (proofs, case studies, comparisons with prior work)

Don't force systems language onto a paper that doesn't have one. Adjust naturally.
