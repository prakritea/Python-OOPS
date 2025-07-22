# lst = [1,2,3]
# my_str = "mlops playlist"
# my_int = 155

# print(type(my_int))
# lst.capitalize()
# my_str = my_str.capitalize()

# print(lst)

# a = 'x'
# b = 'y'
# print(a+b)

# from OOPS_proj import chatbook
# user1 = chatbook()
# print(user1.id) 
#print(user1.name) #will throw error
# print(user1.__chatbook__name) #we will be able to access it now

# user1 = chatbook() #creates an object
# print(user1.get_name()) #check the name according to the object
# user1.set_name("Agent X") #change the name
# print(user1.get_name()) #printed the name






# Using static method directly from class rather than obj
# chatbook.set_id(10)

# user2 = chatbook()
# print(user2.id)

# user3 = chatbook()
# print(user3.id)



# getter and setter
# print(user1.get_name())
# user1.set_name("Agent X")
# print(user1.get_name())




# function vs method below
# lst = [1,2,3]

# # function
# a1 = len(lst)
# print(a1)

# # method
# user1 = chatbook()
# user1.sendmsg()

# from OOPS_proj import chatbook
# user1 = chatbook()
# print(user1.user_id)

# user2 = chatbook()
# print(user2.user_id)

# user3 = chatbook()
# print(user3.user_id)

# from OOPS_proj import chatbook #static method
# user1 = chatbook()
# print(user1.id)

# user2 = chatbook()
# print(user2.id)

# user3 = chatbook()
# print(user3.id)

#using static method directly from class rather than object
from OOPS_proj import chatbook
user1 = chatbook()
print(user1.id) #1

chatbook.set_id(10)
user2 = chatbook()
print(user2.id) #10

user3 = chatbook()
print(user3.id) #11