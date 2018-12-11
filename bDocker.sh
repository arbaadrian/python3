#!/usr/bin/env bash

R_DIR="$( cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null && pwd )";

cd ${R_DIR}

docker build -t python-36:1.0.0 .

