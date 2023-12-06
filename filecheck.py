import subprocess
import re

# Run git add command
subprocess.run(['git', 'add', '.'])

# Run git status and capture the output in a variable
result = subprocess.run(['git', 'status'], capture_output=True, text=True)

# Get modified .ndjson files using regular expression
modified_files = re.findall(r'\s+modified:\s+([\w./]+\.ndjson)', result.stdout)

# Display the modified .ndjson files
print("Modified .ndjson files:")
for file in modified_files:
    print(file)

    # Run git diff for each modified file
    diff_result = subprocess.run(['git', 'diff', file], capture_output=True, text=True)
    
    # Display the changes
    print(diff_result.stdout)
