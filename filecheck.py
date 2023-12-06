import subprocess
import re

subprocess.run(['git', 'add', '.'])

result = subprocess.run(['git', 'status'], capture_output=True, text=True)

modified_files = re.findall(r'\s+modified:\s+([\w./]+\.ndjson)', result.stdout)

print("Modified .ndjson files:")
for file in modified_files:
    print(file)
    try:
        diff_result = subprocess.run(
        f'git diff --staged --color=always {file} | Select-String -Pattern "`e[32m|`e[0m"',
        text=True,
        shell=False,
        stdout=True
        )
        print(diff_result.stdout)
    except Exception as e:
        print("Error..." , e)
