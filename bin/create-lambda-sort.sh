#!/usr/bin/env bash

mkdir -p ../tmp

FUNCTION_NAME=sort

echo moving to
pushd ../lambda-${FUNCTION_NAME}
rm -f ../tmp/lambda.${FUNCTION_NAME}.zip &&  \
zip -r ../tmp/lambda.${FUNCTION_NAME}.zip * && \
popd

