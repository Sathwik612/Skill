class chatbook :
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin=False
        self.menu()
        
        
        
        
        
    def menu(self):
        user_input =input("""WElcome to the chabook !! select the option below ::
                          1. Press 1 to signup
                          2.press 2 to sign in 
                          3 .press 3 to write a post 
                          4. press 4 to message a frnd
                          5. press any other key to exit """)
    
        if user_input =="1":
            pass
        elif user_input =="2":
            pass
        elif user_input =="3":
            pass
        elif user_input =="4":
            pass
        else :
            exit ()    
        
obj =chatbook()                                 