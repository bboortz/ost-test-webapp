#!/bin/bash

URL="https://localhost:9091/api/info"

curl --insecure -H "Content-Type: application/json" -X POST --data "{\"key-$RANDOM\": \"value-$RANDOM\" }" "$URL"
curl --insecure -H "Content-Type: application/json" -X POST --data "{\"key-$RANDOM\": { \"key-$RANDOM\": \"value-$RANDOM\" } }" ${URL}
#curl --insecure -H "Content-Type: application/json" -X GET "$URL" 
