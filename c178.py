from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk

root=Tk()
root.title("juice center")
root.geometry("800x600")

class juice():
    def __init__(self,fruit_name,quantity):
        self.fruit=fruit_name
        self.qty=int(quantity)
        self.__cost=250
        
    def __calculatecost(self):
        total_cost=self.qty*self.__cost
        print("you have to pay "+str(total_cost)+"USD")
        if(self.fruit=="orange"):
            calorie=47*self.qty
        elif(self.fruit=="mango"):
            calorie=60*self.qty
        elif(self.fruit=="apple"):
            calorie=52*self.qty
        print("x"+str(self.qty)+"="+str(calorie)+"calories")
        
    def getcost(self):
        self.__calculatecost()
        
        

def orderjuice():
    fruit="orange"
    quantity=200
    obj1=juice(fruit,quantity)
    obj1.getcost()
    
    
    

btn_fruit_total=Button(root,text="Total",command=orderjuice)
btn_fruit_total.place(relx=0.95,rely=0.5,anchor=E)
    

root.mainloop()