#!/bin/bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTPUT_DIR="$SCRIPT_DIR/images"
OUTPUT_NAME=""
IMAGES=()
DEFAULT_IMAGES=(py:latest cpp:latest cs:latest web:latest flow:latest dev:latest)

usage() {
  cat <<EOF
USAGE:
  $0 [-o output.tar] [image...]

OPTIONS:
  -o, --output  Output tar name or path, default: images-YYYYmmdd-HHMMSS.tar
  -h, --help    Show this help
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    -o|--output)
      OUTPUT_NAME="${2:-}"
      if [[ -z "$OUTPUT_NAME" ]]; then
        echo "Error: output file not specified" >&2
        exit 1
      fi
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    -*)
      echo "Error: unknown option $1" >&2
      usage
      exit 1
      ;;
    *)
      IMAGES+=("$1")
      # 显式带 tag（含仓库/标签分隔符）原样保留；裸名称自动补 :latest，
      # 避免默认行为把 repo 下其它 tag（如 redis:7-alpine）一并打进去。
      if [[ "$1" != *:* ]]; then
        IMAGES[-1]="$1:latest"
      fi
      shift
      ;;
  esac
done

if [[ ${#IMAGES[@]} -eq 0 ]]; then
  IMAGES=("${DEFAULT_IMAGES[@]}")
fi

mkdir -p "$OUTPUT_DIR"

if [[ -z "$OUTPUT_NAME" ]]; then
  OUTPUT_NAME="images-$(date +%Y%m%d-%H%M%S).tar"
fi

if [[ "$OUTPUT_NAME" == */* ]]; then
  OUTPUT_PATH="$OUTPUT_NAME"
  mkdir -p "$(dirname "$OUTPUT_PATH")"
else
  OUTPUT_PATH="$OUTPUT_DIR/$OUTPUT_NAME"
fi

echo "Saving images to $OUTPUT_PATH"
docker save -o "$OUTPUT_PATH" "${IMAGES[@]}"

echo "Saved:"
echo "  $OUTPUT_PATH"
