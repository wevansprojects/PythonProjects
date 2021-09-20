#!/usr/bin/env python3
#import subprocess
from subprocess import check_output, CalledProcessError, STDOUT

#Extracting Command Output into a variable to be printed out with Text

def system_info():
   command1 = ["lsb_release", "-d"]
   output1 = check_output(command1, stderr=STDOUT).decode()
   print(output1.rstrip())   
   command2 = ["uname", "-r"]
   output2 = check_output(command2, stderr=STDOUT).decode()
   print("Kernel:         " + output2.rstrip())
   command3 = ["uname", "-i"]
   output3 = check_output(command3, stderr=STDOUT).decode()
   print("System:         " + output3.rstrip())
   command4 = ["uname", "-o"]
   output4 = check_output(command4, stderr=STDOUT).decode()
   print("OS:             " + output4.rstrip())
   command5 = ["hostname", "-I"]
   output = check_output(command5, stderr=STDOUT).decode()
   print("Local IP:       " + output.rstrip())

#Main Function That Calls Other Functions

def main():
   system_info()
if __name__ == "__main__":
   main()
