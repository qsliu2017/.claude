#!/bin/bash
if [ -z "$ANTHROPIC_BASE_URL" ] || [ -z "$ANTHROPIC_CUSTOM_HEADERS" ]; then
  echo "Error: ANTHROPIC_BASE_URL and ANTHROPIC_CUSTOM_HEADERS must be set" >&2
  # TODO: should exit 2 accrodding to docs, but it doesn't work
  exit 1
fi

exit 0

