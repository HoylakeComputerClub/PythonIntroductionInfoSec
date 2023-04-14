        #    -4  -3 -2    -1
        #     0  1  2     3
numberList = [1, 2, 3, [2,3,4]]
                     #  0 1 2

nums = numberList.copy() # [1, 45, 3, [2,3,4]]

# print(numberList)
# numberList[3][2]
nums[1] = 45
# print(nums[1]) # <<--- 45
# print(numberList[1])
# print(dir(l))



methodList = ['append', 'clear', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# print(methodList.count("clear"))
# for method in methodList:
#     print(method)


# help(numberList.copy)

st = "this is a string it is not very long"

# version 1
# print(st[::-1])

# version 2
newSt = ""
for i in range(len(st) - 1, -1, -1):
    newSt += st[i]

# print(newSt)

# st2 = st.split()
# print(st2)
# for i in range(len(st2)):
#     st2[i] = st2[i][::-1]

# print(st2)
# st3 = " ".join(st2)
# print(st3)
# st2.reverse()
# print(st2)
# st3 = " ".join(st2)
# print(st3)


def myThing(st, seperator):
    st2 = st.split()
    st2.reverse()
    st3 = str(seperator).join(st2)
    return st3
    

myString = myThing("good feeling am i", " this is a seperator ")
# print(myString)


a = 10 
b = 20
c = 10
# == equal
# != not equal
# < less than
# > greater than
# <= less than or equal
# >= greater than or equal
# print(a < c)

# if (a != c and b > a) or a == a:
#     print("print if true")
# else:
#     print("print if false")

def searchForName(name, nameList):
    if name in nameList:
        return nameList.index(name)
    else:
        return -1

names = ["Steve", "Joe"]
foundName = searchForName("Joe", names)

# print(names[foundName])


## Understand -> Plan -> Execute -> Reflect (UPER)
"""
you are standing in an allyway in front of you is a glass door.
on the other side of the door is some food.
you are starving and you need to get to the food.


- run at door
- break the door with face
- pick up food
- eat food
- go to hospital

on reflextion. that was not a good plan!

- walk to door
- open door X
- walk trough door
- pick up food
- eat food
- be full
"""

def functionOne(name):
    print("hello",name,"You chose function 1")

def functionTwo(name):
    print("hello",name,"You chose function 2")

def functionThree(name):
    print("hello",name,"You chose function 3")

name = input("What is your name? ")
option = input("Enter an Option [1], [2] or [3] ")
if option == "1" and name == "Bob":
    functionOne(name)
elif option == "2":
    functionTwo(name)
elif option == "3":
    functionThree(name)
else:
    print("Please input a number between 1 and 3 and if you chose 1 then only do that if you are Bob")

