#!/usr/bin/python
import os
import re
import sys
#import urllib
#import requests
import math





def main():
    f = open('day1_2.txt','r')
    modules = f.readlines()

    total_fuel = 0
    
    for mass in modules:
        module_total_fuel = 0
        
        fuel = math.floor(int(mass) / 3) - 2

        while fuel > 0:
            module_total_fuel = module_total_fuel + fuel
            fuel = math.floor(int(fuel) / 3) - 2

        total_fuel = total_fuel + module_total_fuel

    print total_fuel
    


if __name__ == '__main__':
  main()



