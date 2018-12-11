#!/usr/bin/env bash

R_DIR="$( cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null && pwd )";

docker run \
  --rm \
  -it \
  --name python \
  -v ${R_DIR}/app:/opt/pyth/app \
  python-36:1.0.0 \
  bash

