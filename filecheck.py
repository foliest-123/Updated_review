import subprocess
import re
import ndjson
import ast






subprocess.run(['git', 'add', '.'])

result = subprocess.run(['git', 'status'], capture_output=True, text=True)
modified_files = re.findall(r'\s+modified:\s+([\w./]+\.ndjson)', result.stdout)

added_lines = []

for file in modified_files:
    print(file)
    diff_command = f'git diff --color=always --staged -U0 {file}'
    diff_result = subprocess.run(diff_command, capture_output=True, shell=True, text=True)
    diff_lines = diff_result.stdout.splitlines()

    for add_line in diff_lines:
        if add_line.startswith('\x1b[32m+'):
            added_lines.append(add_line)

print(added_lines[2])
