#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 10:35:42 2020

@author: Mritunjay Kumar
@Question: 3 (Indices of sub list)
"""
def indicesOfSubList(lst):
    n = len(lst)
    resultListIndices = [] 
    temp = []
    tempLst = lst.copy()
    
    # Created duplicate list to work on for finding the same persons
    # Iterating the each person in the duplicate list untill it is empty
    while(len(tempLst) > 0): 
        # Creating a list for username, phonenumber, email to check the each user different
        username = [tempLst[0][0]]
        phoneNumber = [tempLst[0][1]]
        email = [tempLst[0][2]]
        flag = False
        print("new persson list, username : ",username, ", phoneNumber : ",phoneNumber," and Email : ", email)
        temp.append(lst.index(tempLst[0]))
        for j in range(1, len(tempLst)): 
            print("Index : ", j, " and its values : ", tempLst[j][0])
            if(tempLst[j][0] in username):
                phoneNumber.append(tempLst[j][1])
                email.append(tempLst[j][2])
                flag = True
                
            if(tempLst[j][1] in phoneNumber):
                username.append(tempLst[j][0])
                email.append(tempLst[j][2])
                flag = True
                
            if(tempLst[j][2] in email):
                phoneNumber.append(tempLst[j][1])
                username.append(tempLst[j][0])
                flag = True
            
            if flag:
                temp.append(lst.index(tempLst[j]))
            
            flag = False                              # reset the flag 
            
        print("temp = ", temp)
        resultListIndices.append(temp.copy())
            
        # Removing the persons sublists from the duplicate list on the basis of index value from original list
        for i in temp:
            tempLst.remove(lst[i])
        temp.clear()
        
    return resultListIndices

# Test Case 1
# expected: [[0,1,3][2]]
data = [
("username1","phone_number1", "email1"),
("usernameX","phone_number1", "emailX"),
("usernameZ","phone_numberZ", "email1Z"),
("usernameY","phone_numberY", "emailX")
]
#print(data)
print("Indices Of SubList : ",indicesOfSubList(data))

# Test Case 2 (My own test case)
# expected: [[0, 1, 3, 5], [2, 7], [4], [6]]
data2 = [
("username1","phone_number1", "email1"),
("usernameX","phone_number1", "emailX"),
("usernameZ","phone_numberZ", "email1Z"),
("usernameY","phone_numberY", "emailX"),
("username2","phone_number2", "email2"),
("usernameX","phone_number5", "emailX"),
("usernameW","phone_numberW", "email1W"),
("usernameM","phone_numberZ", "email1M")
]
print("Indices Of SubList : ",indicesOfSubList(data2))