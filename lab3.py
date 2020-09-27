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
   for i in range(0, len(set2):
      set2[i] = set2[i].strip()
   
   if function == "x":
      if len(set1) == len(set2):
         for i in range(len(set1)):
            print(set1[i] + " -> " + set2[i])
      else:
         print("For One to One, both sets must be the same size.")
   
   
if __name__ == "__main__":
   main()
