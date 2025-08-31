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
            self.signup()
        elif user_input =="2":
            self.signin()
        elif user_input =="3":
            self.post()
        elif user_input =="4":
            self.message()
        else :
            exit ()    
    def signup(self):
        email =input ("enter your email her ->")   
        password =   input ("enter your password l her ->") 
        self.username=email
        self.password =password
        print(f"You have succesfullt logge in as {email}")  
        print ("\n")  
        self.menu()
    def signin(self):
        if self.username =='' and self.password =='':
            print("Please sign-up first ")
        else :
            uname= input ("enter ur username here ->")
            pwd =input ("Enter ur pwd ->")
            if self.username ==uname and self.password ==pwd:
                print(f"you are logged in successfully as {uname}")
                self.loggedin = True 
            else :
                print ("Input exact credentials ")
            print ("\n")
        self.menu()    
    def post(self):
        if self.loggedin ==True :
            txt =input ("Enter your message her ->")
            print(f" Succesfully posted the following {txt}")
            self.menu()
        else :
            print ("Sign in first ")
            self.menu()    
    def message(self):
        if self.loggedin ==True :
            frnd =input ("enter user id of frnd ->")
            msg=input ("Enter msg ")
            print(f"Msg sent succesfully  to {frnd }")
            self.menu()
        else :
            print ("Sign in first ")
            self.menu()       
            
                                       
        
obj =chatbook()                                 