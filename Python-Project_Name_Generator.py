#!/usr/bin/env python3.7

import random
import string

def ec2_names():
  
    number = (int(input("How many EC2 instances do you want names for?" )))
    department = (input("What is the name of your department?" ))
    
    instances = []
    
    for n in range(number):
    
        res = ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))
        name = department + "-" + res
        instances.append(name)
     
    print(instances)

print(ec2_names())

