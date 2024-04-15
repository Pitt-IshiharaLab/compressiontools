#!/bin/bash

bfc_path="bfconvert" # if not in system PATH, enter absolute path to bfconvert.sh for Windows
index_pattern="S%%sC%%c"
in_path="D:/CellVoyagerACE_Data/BO_2ndPass/20240412T174054_BOauto"
temp_path="D:/jetraw_testing/temp"
dest_path="D:/jetraw_testing/conv_comp"
delete_intermediate=true

#
# Step 0: Define functions and parameters
#

replace_string_in_file() {
    local file="$1"
    local replacement="$2"
    local temp_file="${file}.tmp"

    # Use sed to replace "FileName=" with "FileName=<replacement>/"
    sed "s|FileName=\"|FileName=\"${replacement}/|g" "$file" > "$temp_file"

    # Move temp file to original file
    mv "$temp_file" "$file"
}

dataset_name=$(basename $in_path)
out_path="$temp_path/$dataset_name"
final_path="$dest_path/$dataset_name"

#
# Step 1: Use Bio-Formats CLI to convert indivudal CQ1 tif to stacks
#

if [ -f "$in_path/MeasurementResultMIP.ome.tif" ]; then
    comp_file="$out_path/MeasurementResultMIP.companion.ome"
    input_file="$in_path/MeasurementResultMIP.ome.tif"
    output_file="$out_path/Projection/MIP-$index_pattern.ome.tif"
    "$bfc_path" -overwrite -option ometiff.companion "$comp_file" "$input_file" "$output_file"
    replace_string_in_file "$comp_file" "Projection"
    echo "Completed: bfconvert for MeasurementResultMIP.ome.tif"
fi

if [ -f "$in_path/MeasurementResult.ome.tif" ]; then
    comp_file="$out_path/MeasurementResult.companion.ome"
    input_file="$in_path/MeasurementResult.ome.tif"
    output_file="$out_path/Image/$index_pattern.ome.tif"
    "$bfc_path" -overwrite -option ometiff.companion "$comp_file" "$input_file" "$output_file"
    replace_string_in_file "$comp_file" "Image"
    echo "Completed: bfconvert for MeasurementResult.ome.tif"
fi

#
# Step 2: Use dpcore to compress OME-TIF files
#

if [ -d "$final_path" ]; then
    echo "Directory '$final_path' already exists."
else
    # Create the directory
    mkdir -p "$final_path"
    if [ $? -eq 0 ]; then
        echo "Directory '$final_path' created successfully."
    else
        echo "Failed to create directory '$final_path'."
    fi
fi

dpcore --preserve-extension --overwrite --copy-others -r -c -d  "$final_path" -i 306296 "$out_path"
echo "Completed: Jetraw compression."

#
# Step 3: Copy all other files from CQ1 directory.
#

# Copy contents excluding "Image" and "Projection" subdirectories
find "$in_path" -mindepth 1 -maxdepth 1 -type d \( ! -name "Image" -a ! -name "Projection" \) -exec cp -r {} "$final_path\fromCQ1" \;
echo "Completed: Copy other files."

#
# Step 4: Delete intermediate files.
#

if [ "$delete_intermediate" = true ]; then
    if [ -d "$out_path" ]; then
        # Delete all contents of the directory
        rm -rf "out_path"
        echo "Completed: Delete intermediate files in $out_path"
    else
        echo "Directory '$out_path' does not exist."
    fi
fi

#
# Step 5: Write log file.
#

# echo "Completed: Write log files."

read -p "Script completed." -t 15