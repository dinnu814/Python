#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dchanna
#
# Created:     12/07/2020
# Copyright:   (c) dchanna 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
##print(os.getcwd())
##print(os.chdir("C:/Users/dchanna/Documents/Learning/"))
##print(os.getpid())
##print(os.listdir("C:/Users/dchanna/Documents/Learning/"))

for root, dir, files in os.walk("C:/Users/dchanna/Documents/Learning/"):
    print(root)
    print(dir)
    print(files)
