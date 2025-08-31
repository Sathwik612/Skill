class employee:
    def __init__(self):
        self.id=123
        self.slary=500000
        self.designation="SDE"
    #method dec 
    def travel(self,destination):
        print(f"Employee is now travelling to {destination}")
    
    
        
#creating an instance /obg
sam=employee()
print(sam.slary) 
sam.travel("mysore")   
