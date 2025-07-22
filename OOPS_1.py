class employee: #initiate a class
    def __init__(self): #special method/ dunder method/ magic method - constructor
        # print("started excuting attributes/data")
        print(id(self)) #return location from the memory
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        # print("completed")
        
    def travel(self,destination): #function
        print(f"employee is now travelling to {destination}")
            
            
#create an obj/instance of the class
sam = employee()
jake = employee()

# print(id(sam)) #sam id = self id

#printing the attributes
print(sam.id)
print(jake.id)

sam.name = "sammy"  #this object's attribute was not defined while building constructor

#calling a method
sam.travel("kerela")

print(type(sam))    