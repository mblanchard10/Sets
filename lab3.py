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
   print("Enter with single quotations(' ') \n")

   set1list = str(input("Set One: "))
   set2list = str(input("Set Two: "))
   function = int(input("Function Type: "))

   set1 = set1list.split(",")
   for i in range(0, len(set1)):
      set1[i] = set1[i].strip()
   
   set2 = set2list.split(",")
   for i in range(0, len(set2)):
      set2[i] = set2[i].strip()
   
   if function == 1:
      if len(set1) > len(set2):
         print("For One to One, set one can not be bigger than set two. However, set two can be bigger than set one.")
      for i in range(len(set1)):
         print(set1[i] + " -> " + set2[i])
   
   if function == 2:
      if len(set1) > len(set2):
         for i in range(len(set1)):
            index = i
            if index >= len(set2):
               index = len(set2)-1
            print(set1[i] + " -> " + set2[index])
      if len(set1) < len(set2):
         print("For onto, set two must be smaller or equal to set one.")
if __name__ == "__main__":
   main()
