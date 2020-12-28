#! /bin/sh

openapi-generator generate -i swagger.yaml -o client \
-g typescript-axios \
-p typescriptThreePlus=true,prefixParameterInterfaces=true,supportsES6=true