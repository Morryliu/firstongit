# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 12:38:08 2021

@author: User
"""

products_list=[
    ["phone",10000],
    ["headset",1000],
    ["microphone",1000],
    ["keyboard",2000],
    ["mouse",5000]
    ]
shopping_car = []

balance = input("請輸入購買金額:")

if balance.isdigit():
    balance = int(balance)
    while True:
        for i,goods in enumerate(products_list):
            print(i,goods)
        products_id = input("請輸入購買的商品編號[退出q]]:")
        if products_id.isdigit():
            products_id = int(products_id)
            if products_id >= 0 and products_id < len(products_list):
               products_price = products_list[products_id]
               balance = balance-products_price[1]
               if (balance) >= 0:
                   shopping_car.append(products_price)
                   print("將 %s 放入購物車，餘額還剩 %s 元" %(products_price,balance))
               else:
                   print("餘額不足")
                   break
            else:
                 print("商品編號不存在")
        elif products_id == 'q':
            print("------購買商品如下------")
            for p in shopping_car:
                print(p)
            print("餘額剩餘%s元" % balance)
            print('Exit')
            exit()
else:
    print("請輸入數值!")
        
