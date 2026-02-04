#list&tuple
numbers=[10,20,30,40] #list

coordinates=(5,10) #tuple

print(numbers)
print(coordinates)

#indexing&slicing
a=[100,200,300,400,500,600,700,800,900]
print(a[-3:-1])

print(a[1:4:2]) #positive indexing

print(a[-7:-2:2]) #negative indexing

#list methods & mutability
a=[1,3,2,5,4]
a.append(6)
a.pop()
a.sort()
a.reverse()
print(a)

