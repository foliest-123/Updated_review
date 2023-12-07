import subprocess
import re
import ndjson

subprocess.run(['git', 'add', '.'])

result = subprocess.run(['git', 'status'], capture_output=True, text=True)
modified_files = re.findall(r'\s+modified:\s+([\w./]+\.ndjson)', result.stdout)

added_lines = []
def remove_ansi_escape(line):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    line = ansi_escape.sub('', line)
    # if line.startswith('+'):
    #     line = line[1:].strip().replace("\\", " ")
    return line

for file in modified_files:
    print(file)
    diff_command = f'git diff --color=always --staged -U0 {file}'
    diff_result = subprocess.run(diff_command, capture_output=True, shell=True, text=True)
    diff_lines = diff_result.stdout.splitlines()

    for add_line in diff_lines:
        if add_line.startswith('\x1b[32m+'):
            processed_line = remove_ansi_escape(add_line)
            added_lines.append(processed_line)

print(added_lines)
with open('added_lines.ndjson', 'w') as file:
    for line in added_lines:
        file.write(line + '\n')

try:
    subprocess.run(['git', 'commit', '-m', 'last-commit'], capture_output=True, text=True)
except subprocess.CalledProcessError as e:
    print(f"Git commit failed with error: {e}")
