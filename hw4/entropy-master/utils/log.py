# Entropy
# Designed and Developed By Mausam, http://www.cs.washington.edu/homes/mausam
# Modified by Chitesh Tewani

#------------------------------------------------------------#
#                 DO NOT CHANGE ANYTHING IN 	         	 #
#                   THIS FILE                    			 #
#------------------------------------------------------------#

# My favourite terminal color module!
# it may or may not work with windows

DEBUG = True

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	OKBLACK = '\033[30m'
	OKRED = '\033[31m'
	OKYELLOW = '\033[33m'
	OKMAGENTA = '\033[35m'
	OKCYAN = '\033[36m'
	OKWHITE = '\033[37m'
	BACKBLACK = '\033[40m'
	BACKRED = '\033[41m'
	BACKGREEN = '\033[42m'
	BACKYELLOW = '\033[43m'
	BACKBLUE = '\033[44m'
	BACKMEGNETA = '\033[45m'
	BACKCYAN = '\033[46m'
	BACKWHITE = '\033[47m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	BLINK = '\033[5m'
	CONCEAL = '\033[8m'


def log(message):
	if (DEBUG == True):
		print (message)

def pr(message):
	print (message)

def Warn(message):
	print (bcolors.BOLD + bcolors.WARNING + message + bcolors.ENDC)

def Error(message):
	print (bcolors.BOLD + bcolors.FAIL + message + bcolors.ENDC)

def Info(msg):
	print (bcolors.BOLD + bcolors.OKGREEN + msg + bcolors.ENDC)

# -------------------------------------------------------------------------------
def pr_underl(message):
	print (bcolors.BOLD + bcolors.UNDERLINE + message + bcolors.ENDC)

def pr_okblue(message):
	print (bcolors.BOLD + bcolors.OKBLUE + message + bcolors.ENDC)

def pr_okgreen(message):
	print (bcolors.BOLD + bcolors.OKGREEN + message + bcolors.ENDC)

def pr_okblack(message):
	print (bcolors.BOLD + bcolors.OKBLACK + message + bcolors.ENDC)

def pr_okred(message):
	print (bcolors.BOLD + bcolors.OKRED + message + bcolors.ENDC)

def pr_okyellow(message):
	print (bcolors.BOLD + bcolors.OKYELLOW + message + bcolors.ENDC)

def pr_okmegenta(message):
	print (bcolors.BOLD + bcolors.OKMAGENTA + message + bcolors.ENDC)

def pr_okcyan(message):
	print (bcolors.BOLD + bcolors.OKCYAN + message + bcolors.ENDC)

def pr_okwhite(message):
	print (bcolors.BOLD + bcolors.OKWHITE + message + bcolors.ENDC)

def pr_header(message):
	print (bcolors.BOLD + bcolors.HEADER + message + bcolors.ENDC)

def pr_blink(message):
	print (bcolors.BOLD + bcolors.BLINK + message + bcolors.ENDC)

def pr_conceal(message):
	print (bcolors.BOLD + bcolors.CONCEAL + message + bcolors.ENDC)

def pr_bblack(message):
	print (bcolors.BOLD + bcolors.BACKBLACK + message + bcolors.ENDC)

def pr_bred(message):
	print (bcolors.BOLD + bcolors.BACKRED + message + bcolors.ENDC)

def pr_bgreen(message):
	print (bcolors.BOLD + bcolors.BACKGREEN + message + bcolors.ENDC)

def pr_byellow(message):
	print (bcolors.BOLD + bcolors.BACKYELLOW + message + bcolors.ENDC)

def pr_bblue(message):
	print (bcolors.BOLD + bcolors.BACKBLUE + message + bcolors.ENDC)

def pr_bmagenta(message):
	print (bcolors.BOLD + bcolors.BACKMEGNETA + message + bcolors.ENDC)

def pr_bcyan(message):
	print (bcolors.BOLD + bcolors.BACKCYAN + message + bcolors.ENDC)

def pr_bwhite(message):
	print (bcolors.BOLD + bcolors.BACKWHITE + message + bcolors.ENDC)
