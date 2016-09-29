#!/usr/bin/env python3
# Code written by Security Programmer: AbdulMuaz Aqeel, Iraq - Baghdad
# Social Media: facebook.com/AbdulMuaz.Aqeel.SSP

# The script based to work with high python version like python3.4 and
# python3.5 but it also can be worked with python2.7 but should be without errors.

import sys as system
import os as operating_system
import time
def main():
    Intro = '''> Terminal Packages Commands (TPC) - Installer
> Version: [v1.0] only for linux systems.\n'''
    if len(system.argv) == 2:
        try:
            file_content = open(system.argv[1], 'r').readlines()
        except(IOError, TypeError):
            time.sleep(1)
            print('Error: Something went wrong while reading the text file.')
            print('Canceled in: '+str(time.ctime()))
            time.sleep(1)
            system.exit('Closing                            [ OK ]')
            time.sleep(0.3)
        time.sleep(1)
        print(Intro)
        time.sleep(1)
        print('[+] Searching for commands...\n')
        time.sleep(4)
        for lines in file_content:
            if lines.startswith('#') or lines.startswith('\n'):
                pass
            elif lines.startswith('>'):
                try:
                    com = lines.split('>')
                    for commands in com[1:]:
                        operating_system.system(commands)
                except(OSError, SystemError):
                    print('Error: Something went wrong while reading the commands.')
            else:
                system.exit('Error: The file contain an incorrect lines. Check the spaces before each line')
                break
    else:
        if len(system.argv) == 1:
            system.exit('Error: No text file was found or entered.')
        elif len(system.argv) > 2:
            system.exit('Error: The entered files were more than one file.')

if __name__ == '__main__':
    main()

