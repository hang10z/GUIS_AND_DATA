from tkinter import *


def save_data():
    file = open('Deliveries.text', 'a')
    file.write('Depot:\n')
    file.write('%s \n' % depot.get())
    file.write('Description:\n')
    file.write('%s \n' % description.get())
    file.write('Address:\n')
    file.write('%s \n' % address.get('1.0', END))

    # Clear Radiobuttons, description and address fields after saving
    depot.set(NONE)
    description.delete(0, END)
    address.delete(1.0, END)


def read_depots(file):
    depots = []
    depots_f = open(file)
    for line in depots_f:
        depots.append(line.rstrip())
    return depots


app = Tk()
app.title('Head-Ex Deliveries')
Label(app, text='Depot:').pack()
depot = StringVar()
depot.set(NONE)

options = read_depots('depots.txt')
OptionMenu(app, depot, *options).pack()

Label(app, text='Description:').pack()
description = Entry(app)
description.pack()

Label(app, text='Address:').pack()
address = Text(app)
address.pack()
Button(app, text='Save', command=save_data).pack()
app.mainloop()
