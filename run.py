from subprocess import call, check_output, run, PIPE, check_call, STDOUT
from sys import executable,argv
import os

packages = ["discord.py","youtube_dl","discord.py[voice]"]
print("Updating librairies")

def install_package(package):#it should work if not tell me it
	code1 = executable[:-5] + executable[-4:]+" -m pip install --upgrade {}".format(package)
	if "python.exe" in code1 or "pythonw.exe" in code1:
		print(check_call(code1, shell=True,
			stdout=open(os.devnull, 'wb'), stderr=STDOUT))
	else:
	    print(check_call(executable+" -m pip install --upgrade {}".format(package), shell=True,
	    	stdout=open(os.devnull, 'wb'), stderr=STDOUT))

for librairy in packages:
	install_package(librairy)
print("Librairy up to date")

this_dir = os.getcwd()
print(this_dir)
Bot_location = "\\Juicy\\main.py"

def run(file):
	code1 = executable[:-5]+executable[-4:]+" -i {}".format(file)
	if "python.exe" in code1 or "pythonw.exe" in code1:
	    print(check_output(code1, shell=True).decode())
	else:
	    print(check_output(executable+" -i {}".format(file), shell=True).decode())
import sys
sys.path.append(this_dir+"\\Juicy")
import main
exec(main)

#run(this_dir+Bot_location)
