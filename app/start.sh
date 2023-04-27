#!/bin/bash
app = "TPF.whitelistDoc"
docker buld -t ${app} .
docker run -d -p 56733:80 \
    --name=${app} \
    -v $PWD:/app ${app}