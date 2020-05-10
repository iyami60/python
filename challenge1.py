"""
Task:
You have to create a program where a list of numbers is given and a number of rotation is given. Now you to bring last number of list in front and swift each number to the right. Do this till the given number of rotation.

Sample :-
input - [1,2,3,4] , 2
output - [4,1,2,3] -> [3,4,1,2]

Good luck!
"""
list1 = [4,3,2,1]
rot =2
for i in range(2):
    a=list1.pop(0)
    list1.append(a)
print(list1)
def rotat(liss,num):
    for i in range(num):
        a=liss.pop(0)
        liss.append(a)
    return liss

print(rotat([4,3,2,1],2))
