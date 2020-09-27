#!/usr/bin/env python3

__author__ = "Mike Blanchard"
__copyright__ = "Copyright 2020"
__credits__ = ["Cam Bortle, Braeden Thompson"]
__license__ = "GPLv3"
__version__ = "0.0.0"
__maintainer__ = ""
__email__ = "mblancha@highpoint.edu"
__status__ = ""


def main():
   print("Enter two sets as 1,2,3 and a,b,c etc. Then Specify the function type. Enter 1 for one to one, or 2 for onto.")
   set1list = input("Set One: ")
   set2list = input("Set Two: ")
   function = input("Function Type: ")

   set1 = set1list.split(",")
   for i in range(0, len(set1)):
      set1[i] = set1[i].strip()
   
   set2 = set2list.split(",")

   #print("Enter 1 for one -to- one (Injective)")
   #print("Enter 2 for onto (Surjective)")
   #answer = input("Enter Here: ")
   
   map(addition,set1,set2) 
   #if (answer == 1): 
   
   
if __name__ == "__main__":
   main()
