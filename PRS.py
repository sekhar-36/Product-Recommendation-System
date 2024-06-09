# Overall, the code seems to be a simple prototype of a product recommendation system
# where users can receive recommendations based on their interaction history with products.

#Product Recommendation System

import numpy as np  #importing numpy

users = ["user1", "user2", "user3"]  # users  is a list
products = ["laptop", "mouse", "monitor", "pen drive", "hard disk"]  # list

uids = {}  #dict
for i in range(len(users)):  # start=0, stop 3 step 1  i 3 i<stop 3<3 False
    uids[users[i]] = i  # uids[users[0]]=0  user1: 0 user2:1 user3:2

pids = {}  # dict
for i in range(len(products)):  # start =0 stop =5 step =1 i 0
    pids[products[i]] = i  # pids[laoptop]=0 , mouse 1 monitor 2 pendrive 3 harddisk 4

print(uids, pids)

prd_fq = np.zeros((len(users), len(products)))  # 3*5
print(prd_fq)


def reclist(uid):  # function definition
    uid = uids[uid]  # Row id of User
    upids = prd_fq[uid, :]  # column id of the products
    plist = np.argsort(upids)[::-1][:len(upids)]  #frequnecy based sorting for the products
    plist = [products[p] for p in plist]  # to retrive items in the sorted order based on frequency
    print(plist)  #display


def viewproduct(uid, pid):  # function definition
    uid = uids[uid]  # row id of user
    pid = pids[pid]  # column id of the product
    prd_fq[uid, pid] = prd_fq[uid, pid] + 1  # frequency increment
    print(prd_fq)  # display


uname = input("Enter user name:")
print(reclist(uname))
pname = input("Select one product:")
viewproduct(uname, pname)
