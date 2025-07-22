class chatbook: #class
    
    __user_id = 0
    
    def __init__(self): #constructor
        self.username = ""    #attributes
        self.password = ""    #attributes
        self.LoggedIN = False #attributes
        # self.name = "default user"
        self.__name = "Default User" #now we wont be able to access it anymore until...
        # self.user_id = 0
        # self.user_id += 1
        # self.menu()
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        
    @staticmethod
    def get_id():
        return chatbook.__user_id
        
    @staticmethod
    def set_id(val):
        chatbook.__user_id = val
        
    def get_name(self): #return the name of the user ##getter and setter
        return self.__name
    
    def set_name(self,value): #rename
        self.__name = value
        
    def menu(self): #method
        user_input = input("""Welcome to Chatbook!! How would you like to proceed
                           1. press 1 to signup
                           2. press 2 to signin
                           3. press 3 to wrtie a post
                           4. press 4 to message a friend
                           5. press any other key to exit -->""")
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sendmsg()
        else:
            exit()
            
    def signup(self):
        email = input("enter your email here: ")
        pwd = input("enter your password here: ")
        self.username = email
        self.password = pwd
        print("you have signed in successfully")
        print("\n")
        self.menu()
        
    def signin(self):
        if self.username =='' and self.password=='': #if the pass and email is still not defined yet
            print("please signup first by pressing 1 in main menu")
        else:
            uname = input("enter you email/username here: ")
            pwd = input("enter your password here: ")
            if self.username == uname and self.password==pwd:
                print("you have signed in successfully!")
                self.LoggedIN = True
            else:
                print("please input correct credentials")
        print("\n")
        self.menu()
        
    def my_post(self):
        if self.LoggedIN==True:
            txt = input("enter your message here: ")
            print(f"followinf content has been posted: {txt}")
        else:
            print("you need to sigin to post something")
        print("\n")
        self.menu()
        
    def sendmsg(self):
        if self.LoggedIN == True:
            txt = input("Enter your message here: ")
            frnd = input("whom to send the message?: ")
            print(f"your message has been send to {frnd}")
        else:
            print("you need to signin first")
        print("\n")
        self.menu()
            
# user_1 = chatbook()