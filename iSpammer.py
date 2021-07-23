import random
from requests import get
import argparse
import os
import time
from api import Api
import sys

def check():
    print(color)
    print("\t\t\t\t Bombing Started...")
    
def banner():
    os.system('''
	figlet -c -k  I-Spam
	echo  "   FinsTeR"
	printf " "
	printf "\e[1;32m \e[0m\e[1;95m OTP && CALL bombing tool  \e[0m\e[1;32m\e[0m\n"
	printf "\e[1;32m \e[0m\e[1;95m made by \e[31m FinsTeR \e[0m \e[0m\e[1;32m\e[0m\n"
	printf "\n"
	printf "\e[101m \e[1;77m Disclaimer: Developers assume no liability and are not \e[0m\n"
	printf "\e[101m \e[1;77m responsible for any misuse or damage caused by I-Spam \e[0m\n"
	printf "\n"
	''')

colors=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m']
color = random.choice(colors)
print('\n\n')

parser = argparse.ArgumentParser()
parser.add_argument('-t', type=str, default=0, help="Use this Argument to Add Target.")
parser.add_argument('-m', type=int, default=0, help="Use this Argument to Set Number of Msgs You want to Send.")

args = parser.parse_args()
target = str(args.t)
msgs = args.m
if  target == '':
    banner()
    print("Please Enter the Number of Target with -t Argument.")
elif msgs == 0:
    banner()
    print("Please Enter the Number of Msgs with -m Argument")
elif msgs>100001:
    banner()
    print(color)
    print("You can't Send more than 100000 Msgs At a Time")
elif len(target)==10 and msgs<=100001:
        print(color)
        banner()
        check()
        Api.infinite(target, color, msgs)
        banner()
        print(color)
        print("Bombed "+str(msgs)+" Messages Successfully...")
else:
    print("Please Enter Correct Mobile Number and Number of Msgs or Contact FinsTeR.")
