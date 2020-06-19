from tkinter import *  # noqa ignore=F405
import backend


def get_selected_row(event):
    try:
        global selected_row
        index = lb1.curselection()[0]
        selected_row = lb1.get(index)
        e1.delete(0, END)  # noqa ignore=F405
        e1.insert(END, selected_row[1])  # noqa ignore=F405
        e2.delete(0, END)  # noqa ignore=F405
        e2.insert(END, selected_row[2])  # noqa ignore=F405
        e3.delete(0, END)  # noqa ignore=F405
        e3.insert(END, selected_row[3])  # noqa ignore=F405
        e4.delete(0, END)  # noqa ignore=F405
        e4.insert(END, selected_row[4])  # noqa ignore=F405
    except IndexError:
        pass


def view_command():
    lb1.delete(0, END)  # noqa ignore=F405
    for i in backend.view():
        lb1.insert(END, i)  # noqa ignore=F405


def search_command():
    lb1.delete(0, END)  # noqa ignore=F405
    for i in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):  # noqa ignore=E501
        lb1.insert(END, i)  # noqa ignore=F405


def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())  # noqa ignore=E501
    lb1.delete(0, END)  # noqa ignore=F405
    lb1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))  # noqa ignore=E501)


def delete_command():
    backend.delete(selected_row[0])


def update_command():
    backend.update(selected_row[0], title_text.get(),
                   author_text.get(), year_text.get(), isbn_text.get())


window = Tk()  # noqa ignore=F405

window.title("BookStore")

l1 = Label(window, text='Title').grid(row=0, column=0)  # noqa ignore=F405

l2 = Label(window, text='Author').grid(row=0, column=2)  # noqa ignore=F405

l3 = Label(window, text='Year').grid(row=1, column=0)  # noqa ignore=F405

l4 = Label(window, text='ISBN').grid(row=1, column=2)  # noqa ignore=F405


title_text = StringVar()  # noqa ignore=F405
e1 = Entry(window, textvariable=title_text)  # noqa ignore=F405
e1.grid(row=0, column=1)


author_text = StringVar()  # noqa ignore=F405
e2 = Entry(window, textvariable=author_text)  # noqa ignore=F405
e2.grid(row=0, column=3)


year_text = StringVar()  # noqa ignore=F405
e3 = Entry(window, textvariable=year_text)  # noqa ignore=F405
e3.grid(row=1, column=1)

isbn_text = StringVar()  # noqa ignore=F405
e4 = Entry(window, textvariable=isbn_text)  # noqa ignore=F405
e4.grid(row=1, column=3)


lb1 = Listbox(window, height=8, width=60)  # noqa ignore=F405
lb1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)  # noqa ignore=F405
sb1.grid(row=2, column=2, rowspan=8)

# Telling the scrollbar about the list and vice versa
lb1.configure(yscrollcommand=sb1.set)
sb1.configure(command=lb1.yview)

# Retrieving rows from listbox by clicking on it
lb1.bind("<<ListboxSelect>>", get_selected_row)

b1 = Button(window, text="View all", width=12, command=view_command)  # noqa ignore=F405
b1.grid(row=2, column=3)

b2 = Button(window, text="Search entry", width=12, command=search_command)  # noqa ignore=F405
b2.grid(row=3, column=3)

b3 = Button(window, text="Add entry", width=12, command=add_command)  # noqa ignore=F405
b3.grid(row=4, column=3)

b4 = Button(window, text="Update selected", width=12, command=update_command)  # noqa ignore=F405
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete selected", width=12, command=delete_command)  # noqa ignore=F405
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)  # noqa ignore=F405
b6.grid(row=7, column=3)
window.mainloop()  # noqa ignore=F405
