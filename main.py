#Import the tkinter library
from tkinter import*
from tkinter import messagebox
import json

from difflib import get_close_matches

# for working of button label (function)

def iexit():
    res = messagebox.askyesno('Exit', 'Do you want to exit?')
    if res == True:
        root.destroy()
    else:
        pass


def clear():
    textarea.config(state=NORMAL)
    enterwordentry.delete(0, END)
    textarea.delete(1.0, END)
    textarea.config(state=DISABLED)


def search():
    data = json.load(open('data.json'))
    word = enterwordentry.get()

    word = word.lower()

    if word in data:
        meaning = data[word]

        textarea.config( state=NORMAL)
        textarea.delete(1.0,END)
        for item in meaning:
            textarea.insert(END, u'\u2022'+ item + '\n\n')
            textarea.config(state=DISABLED)
    else:
        textarea.delete(1.0,END)
        messagebox.showinfo('Information','Please type a correct word')
        enterwordentry.delete(0,END)













#Create an instance of the tkinter frame
root=Tk()

root.title('DICTIONARY')

#Define the geometry of the frame
root.geometry('1000x800+100+30')

root.resizable(0, 0)



bgimage = PhotoImage(file='n1.png')
bgLabel = Label(root, image=bgimage)
bgLabel.place(x=0, y=0)

enterwordLabel = Label(root, text='Enter Word', font=('castellar' ,29, 'bold'), fg='black', bg='white')
enterwordLabel.place(x=120, y=120)

enterwordentry = Entry(root, font=('arial', 23, 'bold'), bd=8, relief=GROOVE, justify=CENTER)
enterwordentry.place(x=100, y=200)

enterwordentry.focus_set()


searchimage = PhotoImage(file='search.png')
searchButton = Button(root, image=searchimage, bd=0, bg='white', activebackground='white', cursor='hand2', command= search)
searchButton.place(x=245, y=300)


meaninglabel = Label(root, text="Meaning", font=('castellar', 35, 'bold'), fg='red', bg='white')
meaninglabel.place(x=600, y=120)


textarea = Text(root, font=('arial', 18, 'bold'), height=8, width=30, bd=8, relief=GROOVE, wrap='word')
textarea.place(x=539, y=250)



clearimage = PhotoImage(file='clear.png')
clearButton = Button(root, image=clearimage, bd=0, bg='white', activebackground='white', cursor='hand2', command=clear)
clearButton.place(x=650, y=550)



exitimage = PhotoImage(file='exit.png')
exitButton = Button(root, image=exitimage, bd=0, bg='white', activebackground='white', cursor='hand2', command=iexit)
exitButton.place(x=800, y=550)







root.mainloop()