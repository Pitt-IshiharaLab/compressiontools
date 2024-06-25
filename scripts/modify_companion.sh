#!/bin/bash

# Define function to replace string in file
replace_string_in_file() {
    local file="$1"
    local replacement="$2"
    local temp_file="${file}.tmp"

    # Use sed to replace "FileName=" with "FileName=<replacement>/"
    sed "s|FileName=\"|FileName=\"${replacement}/|g" "$file" > "$temp_file"

    # Move temp file to original file
    mv "$temp_file" "$file"
}

replace_string_in_file "D:/out/MeasurementResult.companion.ome" "Image"
replace_string_in_file "D:/out/MeasurementResultMIP.companion.ome" "Projection"

# # Check if two input arguments were provided
# if [ $# -ne 2 ]; then
#     echo "Usage: $0 <file> <replacement>"
#     exit 1
# fi

# Call the function with the provided arguments
# replace_string_in_file "$1" "$2"