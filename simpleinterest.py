from tkinter import *

window = Tk()

window.title("Simple Interest Calculator")
window.geometry("400x400")
window.configure(bg="black")

def calculateSimpleInterest():
    p = float(principleLabel.get())
    r = float(rateLabel.get())
    t = float(timeLabel.get())
    i = (p*r*t)/100
    interest = round(i, 2)

    showLabel.destroy()

    msg=""

    output = Label(resultFrame, text=name+",your Simple Interest Is"+str(interest))+"and"+msg, bg="lightcyan", font=("Calibri",12), width=42)
    output.place(x=20,y=20)
    output.pack()

appLabel = Label(window,text="SIMPLE INTEREST CALCULATOR",fg="Black",bg="Yellow", font=("Calibri"),bd=5)
appLabel.place(x=60, y=20)



nameLabel = Label(window,text="Enter Your Name",fg="White",bg="Black", font=("Calibri, 20"),bd=5)
nameLabel.place(x=20, y=90)



userName = Entry(window,text="", bd = 2,width = 22)
userName.place(x=150,y=92)



rateLabel = Label(window,text="Enter Your Rate", fg="White", bg="Black", font=("Calibri", 20),bd=5)
rateLabel.place(x=20,y=140)

rateEntry = Entry(window,text="",bd=2, width=15)
rateEntry.place(x=150,y=142)



principleLabel=Label(window,text="Enter Your Principle", fg="White",bg="Black", font=("Calibri", 20),bd=5)
principleLabel.place(x=20, y=185)

principleEntry = Entry(window, text="",bd=2, width = 15)
principleEntry.place(x=150, y=187)



timeLabel=Label(window,text="Enter Your Principle", fg="White",bg="Black", font=("Calibri", 20),bd=5)
timeLabel.place(x=20, y=230)

timeEntry = Entry(window, text="",bd=2, width = 15)
timeEntry.place(x=150, y=205)



calculateButton = Button(window, text="Calculate Simple Interest", fg = "black", bd="cyan", bd=4, command=calculate_interest)
calculateButton.place(x=20,y=250)



resultFrame = LabelFrame(window,text="Result" , bg = "lightcyan", font=("Calibri", 12))
resultFrame.pack(padx=20, pady=20)
resultFrame.place(x=20,y=300)

resultLabel = Label(resultFrame, text="Result", bg ="lightcyan", font=("Calibri",12), width = 33)
resultLabel.place(x=20,y=20)
resultLabel.pack()


showLabel=Label(resultFrame, text="Your Result Will Be Displayed Here",bg="grey",font=("Calibri",12), width=55)
showLabel.place(x=20,y=20)
showLabel.pack()

window.mainloop()