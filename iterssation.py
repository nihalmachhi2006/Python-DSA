# n = 50

# for i in range(0,n):
#     print(i)


# li = ["geeks", "for", "geeks"]
# for x in li:
#     print(x)
    
# tup = ("geeks", "for", "geeks")
# for x in tup:
#     print(x)
    
# s = "abc"
# for x in s:
#     print(x)
    
# d = dict({'x':123, 'y':354})
# for x in d:
#     print("%s  %d" % (x, d[x]))
    
# set1 = {10, 30, 20}
# for x in set1:
#     print(x),

# while (True):
#     print("Hello Geek")

#Infinite While Loop


# listofnumber = [1,2,3,41-8,-9,-88,-10]

# postivie_number_count = 0

# for num in listofnumber:
#     if num>0:
#         postivie_number_count += 1
# print(postivie_number_count)


# n = int(input('Enter your number User'))

# sum_even = 0

# for i in range(1, n+1):
#     if i%2 == 0:
#         sum_even += 1

# print(sum_even)

# num = 3

# for i in range (1, 11):
#     if i == 5:
#         continue
#     print(num, "x", i ,"=", num*i)


# input_Str = "thisisstring"

# rev_str = ""

# for char in input_Str:
#     rev_str = char + rev_str

# print(rev_str)


# input_str = "nihalMachhi"

# for char in input_str:
#    if input_str.count(char) == 1:
#        print(char)
#        break

# number = int(input(' ENter input number'))

# factorial = 1

# while number>0:
#     factorial = factorial * number
#     number = number - 1

# print(factorial)

# while True:
#    number =  int(input('enter value between 1-10'))
#    if 1<= number <=10:
#        print("thx")
#        break
#    else:
#        print('invalid number try again')


# number = 30

# isprime = True

# if number>1:
#     for i in range (2, number):
#         if (number% i) == 0:
#             isprime = False
#             break

# print(isprime)

# items = ['apple', 'mango', 'orange', 'apple']

# uniqueitem = set()


# for item in items:
#     if item in uniqueitem:
#         print(item)
#         break
#     uniqueitem.add(item)

import time

waittime = 1
maxretries = 5
attempts = 0

while attempts < maxretries:
    print(attempts + 1, waittime)
    time.sleep(waittime)
    waittime *= 2
    attempts += 1







        
