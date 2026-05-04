# how to create a list what is list 
# list is store mutiple varible instead of use line by line
# there is multile function to help to upadate remove insert and pop
# 1 insert 
# 2 remove()
# 3 pop()
# 4 clear()
# 5 append()

Array=[ 'name' , 4, 5 , 6]
# print (Array[0])
# a = len(Array)
# print(a)

for i in range(len(Array)):
    print(Array[i])

Array.insert(1,"robin")
Array.append(10)

Array.pop()
Array.remove(5)

for i in range(len(Array)):
    print(Array[i])


