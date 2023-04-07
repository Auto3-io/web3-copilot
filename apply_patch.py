import os
import sys
from unidiff import PatchSet


def apply_patch(patch_file, target_file):
    with open(patch_file, 'r') as pf:
        patch_set = PatchSet(pf)

    if not patch_set:
        print(f"No patches found in {patch_file}")
        return

    with open(target_file, 'r') as tf:
        target_lines = tf.readlines()

    for patch in patch_set:
        for hunk in patch:
            for line in hunk:
                if line.is_added:
                    target_lines.insert(line.target_line_no - 1, line.value)
                elif line.is_removed:
                    del target_lines[line.target_line_no - 1]

    with open(target_file, 'w') as tf:
        tf.writelines(target_lines)

    print(f"Patch {patch_file} applied to {target_file}")


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python apply_patch.py <patch_file> <site_package_name> <relative_target_file_path>")
        sys.exit(1)

    patch_file = sys.argv[1]
    site_package_name = sys.argv[2]
    relative_target_file_path = sys.argv[3]

    pip_show_output = os.popen(f"pip show {site_package_name}").read().split("\n")
    site_package_location = ""
    for line in pip_show_output:
        if line.startswith("Location:"):
            site_package_location = line[10:]
            break

    if not site_package_location:
        print(f"Error: Could not find the location of '{site_package_name}'.")
        sys.exit(1)
    target_file = os.path.join(
        site_package_location, relative_target_file_path)

    apply_patch(patch_file, target_file)
