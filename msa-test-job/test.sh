#!/bin/bash

curl --insecure -X POST --data info="{\"key-$RANDOM\": \"value-$RANDOM\" }" https://localhost:9090/api/info
curl --insecure -X POST --data info="{\"key-$RANDOM\": { \"key-$RANDOM\": \"value-$RANDOM\" } }" https://localhost:9090/api/info
