from tkinter import *

#Create a calculator class
class Calculator:
    #Step 2 and 3: create the first method
    def __init__(self, master):
        #Assign reference to the main window of the application
        self.master = master
        #Add a title to the application
        master.title("Python Calculator")
        self.equation=Entry(master)
        self.equation.grid(row=0,column=0,columnspan=4, padx=10, pady=10)
        #create buttons for the application
        self.createButton()


    def createButton(self):
        Button(self.master,text='0',bg='white',fg='black',width=4,command = lambda: self.clickButton(str(0))).grid(row=4,column=1)
        Button(self.master,text='1',bg='white',fg='black',width=4,command = lambda: self.clickButton(str(1))).grid(row=3,column=0)
        Button(self.master,text='2',bg='white',fg='black',width=4,command = lambda: self.clickButton(str(2))).grid(row=3,column=1)
        Button(self.master,text='3',bg='white',fg='black',width=4,command = lambda: self.clickButton(str(3))).grid(row=3,column=2)
        Button(self.master,text='4',bg='white',fg='black',width=4,command = lambda: self.clickButton(str(4))).grid(row=2,column=0)
        Button(self.master,text='5',bg='white',fg='black',width=4,command = lambda: self.clickButton(str(5))).grid(row=2,column=1)
        Button(self.master,text='6',bg='white',fg='black',width=4,command = lambda: self.clickButton(str(6))).grid(row=2,column=2)
        Button(self.master,text='7',bg='white',fg='black',width=4,command = lambda: self.clickButton(str(7))).grid(row=1,column=0)
        Button(self.master,text='8',bg='white',fg='black',width=4,command = lambda: self.clickButton(str(8))).grid(row=1,column=1)
        Button(self.master,text='9',bg='white',fg='black',width=4,command = lambda: self.clickButton(str(9))).grid(row=1,column=2)
        Button(self.master,text='+',bg='white',fg='black',width=4,command = lambda: self.clickButton(str('+'))).grid(row=1,column=3)
        Button(self.master,text='-',bg='white',fg='black',width=4,command = lambda: self.clickButton(str('-'))).grid(row=2,column=3)
        Button(self.master,text='*',bg='white',fg='black',width=4,command = lambda: self.clickButton(str('*'))).grid(row=3,column=3)
        Button(self.master,text='/',bg='white',fg='black',width=4,command = lambda: self.clickButton(str('/'))).grid(row=4,column=3)
        Button(self.master,text='=',bg='white',fg='black',width=4,command = lambda: self.clickButton(str('='))).grid(row=4,column=2)
        Button(self.master,text='clr',bg='white',fg='black',width=4,command = lambda: self.clickButton(str('clr'))).grid(row=4,column=0)
        Button(self.master,text='del',bg='white',fg='black',width=4,command = lambda: self.clickButton(str('del'))).grid(row=5,column=1)

    def clickButton(self,value):
        current_equation = self.equation.get()
        if value == 'clr':
            self.equation.delete(-1,END)
        elif value == '=':
            answer = str(eval(current_equation))
            self.equation.delete(-1, END)
            self.equation.insert(0, answer)
        #add button to the equation line
        elif value == 'del':
            self.equation.delete(len(self.equation.get())-1,END)
        else:
            self.equation.delete(0, END)
            self.equation.insert(-1, current_equation+value)


#Execution
if __name__=='__main__':
    #Create the main window of an application
    root = Tk()
    #Tell our calculator class to use this window
    my_gui = Calculator(root)
    #Executable loop on the application, waits for user input
    root.mainloop()
