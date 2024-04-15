#!/bin/bash

# Define function to run bfconvert command
run_bfconvert() {

    local arg1=$1
    local arg2=$2
    local arg3=$3
    local arg4=$4
    local arg5="$5"
    echo $arg1
    echo $arg2
    echo $arg3
    echo $arg4
    echo $arg5
    sleep 4

    $arg1 $arg2 $arg3 $arg4 "$arg5"
  
}

bfc_path="C:\Users\lab_user\bftools-6.11.1jetraw\bfconvert.bat"
bfc_opts="-overwrite -option ometiff.companion"
comp_file="D:\out\MeasurementResultMIP.companion.ome"
input_file="D:\CellVoyagerACE_Data\BO_2ndPass\20240412T174054_BOauto\MeasurementResultMIP.ome.tif"
output_file="D:\out 3\MIP-S%%sC%%c.ome.tif"

# NOTE: while the directory for companion file needs to exist,
# the sub-directory for tif images will be created with bfconvert

# running directly - requires quotes for output_file, but not for bfc_opts
$bfc_path $bfc_opts $comp_file $input_file "$output_file"

# running directly - this might be less confusing, caters to cases where space is part of filepath
"$bfc_path" -overwrite -option ometiff.companion "$comp_file" "$input_file" "$output_file"

# running via the function - requires quotes for bfc_opts and output_file
run_bfconvert $bfc_path "$bfc_opts" $comp_file $input_file "$output_file"

read -p "Script completed."