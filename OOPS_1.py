class employee: #initiate a class
    def __init__(self): #special method/ dunder method/ magic method - constructor
        print("started excuting attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("completed")
        
    def travel(self,destination): #function
        print(f"employee is now travelling to {destination}")
            
            
#create an obj/instance of the class
sam = employee()

#printing the attributes
print(sam.id)

#calling a method
sam.travel("kerela")

print(type(sam))    