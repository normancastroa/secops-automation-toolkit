from placeHolderClass import apiHandler #from <class file> import <class>

#We will call the functions cereated under apiHandler from package placeHolderClass
print("----------GET---------------")
x = apiHandler.apiGet(99) #when 99 it prints the title, when 100 it prints JSON with timestamp, for any other value it brings the title as well
print(x)

print("\n----------POST--------------")
y=apiHandler.apiPost() #The tupple being passed for posting is burnt into the code. 
print(y)

print("\n---------DELETE-------------")
z=apiHandler.apiDelete(101) #deleting the new entry created, by "id"
print (z)

