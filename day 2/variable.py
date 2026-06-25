
x = [1,2,3,4,5]
print(x)

#data type
x=[1,2,3,4,5]
print(type(x))

#list and array operations
#append method
x = [6,7,8,9,10]
x.append(11)
x.append(12)
print(x)

#append at fix index
a = [1,2,3,4,5]
a.insert(3, 3) #insert 3 at index 0
print("append at index 3:", a)

#pop method
a = [1,2,3,4,5]
a.pop(2) #remove element at index 2
print("pop at index 2:", a)

#slicing
marks = [10,20,30,40,50]
marks[1:4] = [25,35,45] #replace elements from index 1 to 3
print("marks before slicing:", marks)   
print(marks[1:3]) #print elements from index 1 to 2
print("marks after slicing:", marks)   

