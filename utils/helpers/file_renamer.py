import os
import re
import shutil

directory = None

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.readlines()

    first_line = content[0]
    pattern = r"# https:\/\/leetcode.com\/problems\/(?P<problem_name>[a-z-]*)"
    match = re.search(pattern, first_line)
    if match:
        problem_name = match.group("problem_name")

        # Create the new filename
        new_filename = os.path.splitext(filename)[0] + "-" + problem_name + ".py"

        shutil.copy(file_path, os.path.join("new_completed", new_filename))
