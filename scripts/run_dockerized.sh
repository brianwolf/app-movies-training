#!/bin/bash
set -eo pipefail

################################# ---- HELPER ---- #################################

if [[ $# -lt 1 ]]; then
  echo "Uso: $0 <comando_python>"
  exit 1
fi
################################# ---- VARIABLES ---- #################################

PYTHON_IMAGE="python:3.10-slim"
COMMAND="$1"

if [ -z ${WORKSPACE+x} ]; then
  WORKSPACE=$(pwd)
fi

################################# ---- EJECUCION ---- #################################

docker run --rm --net=host \
  -v ${WORKSPACE}:/workspace \
  -w /workspace \
  "$PYTHON_IMAGE" bash -c "pip install -r requirements.txt && $COMMAND"