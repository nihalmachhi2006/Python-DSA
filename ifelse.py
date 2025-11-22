# age = 11

# if(age>18):
#     print("bravo")
# elif(age<=12):
#     if(age == 12):
#         print('chromebook elite')
#     else:
#         print('chromebook lite')
#     print('chrome')
# else:
#     print("brave")

# Match case switch case for python

number = 2

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")