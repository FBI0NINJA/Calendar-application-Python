from tkinter import *
import calendar


win = Tk()
win.title("Ahmed Sayed Calendar")
win.geometry("400x300")
#win.iconbitmap('D:\\icone.ico') الايقون
win.configure(bg="#00ff99")
win.resizable(False,False)
def text():

    year_str = year.get()
    month_str = month.get()
    year_int = int(year_str)
    month_int = int (month_str)
    cal = calendar.month(year_int, month_int)
    textfield.delete(0.0, END)
    textfield.insert(INSERT, cal)

label1 = Label(win, text = 'السنه ' , bg="#00ff99" , font=("Arial",11,"bold"))
label1.grid(row = 0, column = 0)
label1 = Label(win, text = 'الشهر ' , bg="#00ff99" , font=("Arial",11,"bold"))
label1.grid(row = 0, column = 2)

year = Spinbox(win, from_= 1932, to = 3000, width = 30   , bg="#cc33ff" ,fg="white" , font=("Arial",11 ))
year.grid(row = 1, column = 0, padx = 16)
month = Spinbox(win, from_= 1, to = 12, width = 5  , bg="#cc33ff" ,fg="white" , font=("Arial",11))
month.grid(row = 1, column = 2)

button = Button(win, text = "اضغط", command = text , font=("Arial",11,"bold"))
button.grid(row = 3, column = 5)

textfield = Text(win, height = 10, width = 30, foreground = 'black')
textfield.grid(row = 3, columnspan = 3)

win.mainloop()