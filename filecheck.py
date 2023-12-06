import subprocess
import re

subprocess.run(['git', 'add', '.'])

result = subprocess.run(['git', 'status'], capture_output=True, text=True)
modified_files = re.findall(r'\s+modified:\s+([\w./]+\.ndjson)', result.stdout)


for file in modified_files:
    print(file)

    diff_command = (f'git diff --color=always {file}')

    diff_result = subprocess.run(
        diff_command,
        capture_output=True,
        shell=True,
        text=True)

    print(diff_result.stdout)
    print(diff_result.stderr)