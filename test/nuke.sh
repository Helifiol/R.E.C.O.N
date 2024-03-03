#!/bin/bash
JSON_FILE="filelist.json"

FILES=$(jq -r '.files[]' "$JSON_FILE")
echo "$FILE"

for FILE in $FILES; do
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        if [ -f "$(pwd)$FILE" ]; then
            shred "$(pwd)$FILE"
            rm -r "$(pwd)$FILE"
            echo "$FILE has been shredded."
        else
            echo "Error: $FILE does not exist."
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        if [ -f "$(pwd)$FILE" ]; then
            gshred "$(pwd)$FILE"
            rm -r "$(pwd)$FILE"
            echo "$FILE has been shredded."
        else
            echo "Error: $FILE does not exist."
        fi
    fi
done

#add all the python files to leave no trace and remove the echo cmds
#if machine is linux change to shred