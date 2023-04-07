#!/bin/bash

# Create a trash directory under the script's current directory
script_dir=$(dirname "$(readlink -f "$0")")
trash_dir="${script_dir}/trash"

if [ ! -d "${trash_dir}" ]; then
  mkdir "${trash_dir}"
fi

# Pattern for directories named "images"
dir_pattern="images"

# Find and move matching directories to the trash directory with unique names
find "${script_dir}" -type d -name "${dir_pattern}" -exec bash -c 'mv "$0" "${1}/$(uuidgen)_$(basename "$0")"' {} "${trash_dir}" \;

# Pattern for files with the ".json" extension
file_pattern="*.json"

# Find and move matching files to the trash directory with unique names
find "${script_dir}" -type f -name "${file_pattern}" -exec bash -c 'mv "$0" "${1}/$(uuidgen)_$(basename "$0")"' {} "${trash_dir}" \;
