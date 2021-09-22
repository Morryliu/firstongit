# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 13:27:12 2021

@author: User
"""
list1 = range(1,1001)
num = int(input("輸入一個數字(1-1000):"))

if (num >0) and (num<=1000):  
    for i in list1:        
        if (num % 2 == 0):          
            print("%d是偶數" % num)
            break
    else:
        print("%d是奇數" % num)    
else:
    print("輸入數值無效")
    
    

