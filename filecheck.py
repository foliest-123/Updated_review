import subprocess
import re

subprocess.run(['git', 'add', '.'])

result = subprocess.run(['git', 'status'], capture_output=True, text=True)

modified_files = re.findall(r'\s+modified:\s+([\w./]+\.ndjson)', result.stdout)

print("Modified .ndjson files:")
for file in modified_files:
    print(file)

    diff_result = subprocess.run(['git', 'diff', file], capture_output=True, text=True)
    

changes = subprocess.run(
    f'git diff --staged --color=always {file} | Select-String -Pattern "\\e[32m|\\e[0m"',
    capture_output=True,
    text=True,
    shell=True
)

changed_lines = changes.stdout

print("Changed lines:")
print(len(changed_lines))