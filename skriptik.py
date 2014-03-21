#! /usr/bin/python
from telnetlib import Telnet
from datetime import datetime
import socket,os,sys

def main():
	ClearCLI()
	About()
	strFile = raw_input("Provide the directory ")
	blnSave = raw_input("Save result [y/n]?:")

	if os.path.exists(strFile):
	    if len(strFile) != 0:
	        File = open(strFile,'r+')
	        Buffer = File.readlines()
	        List = []
	        print('\n[+]Beginning the scan!')
	        print('[+]Time now: ' + str(datetime.now()) + '\n')
	        print('**********************************************')
	        for lines in Buffer:
		    try:
		       tn = Telnet(lines.strip(), 23)
		       strTemp = tn.read_some()

		       if len(strTemp) != 0:
		           if strTemp.find('MikroTik') != -1:
			       if blnSave == 'y':
			           List.append(lines)                               
			       print('[+]Mikrotik found at: {0}\n'.format(lines.strip())),
			       print('[>]Header: {0}\n'.format(strTemp.strip()))
		           else:
			       print('[-]No results found: {0}\n'.format(lines.strip()))
		       tn.close()
		
		    except socket.timeout:
		           print('[-]Timeout at: {0}\n'.format(lines.strip()))
		           pass
		    except socket.error:
		          print('[-]Telnet closed at: {0}\n'.format(lines.strip()))
		          pass
	        File.close()

	        if len(List) != 0:
		    File = open('Servers.txt','w')
		    for ips in List:
		        File.write(ips)
		    File.close()
	        print('*************Scanning done!**************')
                sys.stdin.read(1)
	else:
            print('[-]Directory not found! Please check directory name.')
            sys.stdin.read(1)   

# print script info			
def About():
    print('#-----------------------------------------------------#')
    print('# Script Name : Skriptikv0.1                          #')
    print('# Author      : Abano Drazhi                          #')
    print('# Mail        : albano.drazhi@cybersecurity.maine.edu #')
    print('# WebPage     : github.com/albtop                     #')
    print('# Usage       : At own risk                  	     #')
    print('# Requirements: Python 2.7                            #')
    print('#---------------------------------------------------#\n')

# Checking the platform
def ClearCLI(): 
    if sys.platform == ('win32' or 'win64'):
            os.system('cls')
            os.system('title MikScanner v0.1')
    elif sys.platform == ('linux' or 'linux2'):
            os.system('clear')
					
# run the main function					
if __name__ == '__main__':main()