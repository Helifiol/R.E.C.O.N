import subprocess

# Example 1: Running a simple shell command
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
# print("Output:", type(result.stdout.encode('utf-8')))

s = "ls -la"
print(s.split())