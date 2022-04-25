import subprocess

print (subprocess.run(['make', 'demo'], capture_output=True, text=True))
