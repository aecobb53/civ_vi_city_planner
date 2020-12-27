#! /bin/sh

openapi-generator generate -i swagger.yaml -o client \
-g typescript-fetch \
-p typescriptThreePlus=true,prefixParameterInterfaces=true