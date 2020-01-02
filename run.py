from subprocess import call, check_output, run, PIPE
from sys import executable,argv
import os

packages = ["discord.py","youtube_dl","discord.py[voice]"]

def install_package(package):#it should work if not tell me it
	code1 = executable[:-5] + executable[-4:]+" -m pip install --upgrade {}".format(package)
	if "python.exe" in code1 or "pythonw.exe" in code1:
		print(check_output(code1, shell=True).decode())
	else:
	    print(check_output(executable+" -m pip install --upgrade {}".format(package), shell=True).decode())

for librairy in packages:
	install_package(librairy)

this_dir = os.getcwd()
print(this_dir)
Bot_location = "\\Juicy\\main.py"

def run(file):
	code1 = executable[:-5] + executable[-4:]+" {}".format(file)
	if "python.exe" in code1 or "pythonw.exe" in code1:
	    print(check_output(code1, shell=True).decode())
	else:
	    print(check_output(executable+" {}".format(file), shell=True).decode())

run(this_dir+Bot_location)