# My Custom nmap scanner
# by 0xskar

import subprocess
import argparse

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('-h', '--host', required=True, help='the host to scan')
parser.add_argument('-p', '--ports', required=True, help='the ports to scan')
args = parser.parse_args()

host = args.host
ports = args.ports.split(',')

print(f'Scanning host: {host} on ports {ports}')

def execute_shell_script(command):
    p = subprocess.Popen(['bash', '-c', command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    return stdout, stderr

for x in ports:
    print(x)
    
command = 'nmap -sV' + host + ports
stdout, stderr = execute_shell_script(command)

if stdout:
    print(f'stdout: {stdout.decode("utf-8")}')
if stderr:
    print(f'stderr: {stderr.decode("utf-8")}')



