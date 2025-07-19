class chatbook:
    def __init__(self): #constructor
        self.username = ""
        self.password = ""
        self.LoggedIN = False
        self.menu()
        
    def menu(self): #method
        user_input = input("""Welcome to Chatbook!! How would you like to proceed
                           1. press 1 to signup
                           2. press 2 to signin
                           3. press 3 to wrtie a post
                           4. press 4 to message a friend
                           3. press any other key to exit""")
        
        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()
            
            
obj = chatbook()