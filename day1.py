#!/usr/bin/python
import os
import re
import sys
#import urllib
#import requests
import math





def main():
    f = open('day1.txt','r')
    modules = f.readlines()

    total_fuel = 0
    
    for mass in modules:
        fuel = math.floor(int(mass) / 3) - 2
        total_fuel = total_fuel + fuel

    print total_fuel
    


if __name__ == '__main__':
  main()



