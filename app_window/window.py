from tkinter import *

def get_text():
    # print(text_box.get(1.0, END))
    label_sended["text"] += text_box.get(1.0, END) + "\n"
    text_box.delete(1.0, END)

window = Tk()
window.geometry('700x700')

canvas = Canvas(window, width=500, height=700)
text_box = Text(window, font=('Arial', 15), wrap='word', height=5)
button_send = Button(window, text='Send', command=get_text)
label_sended = Label(canvas, text='', height=15, font=('Arial', 15))

scrollbar = Scrollbar(canvas, orient=VERTICAL, command=canvas.yview)
scrollbar.place(relx=1, rely=0, relheight=1, anchor=NE)
canvas.config(yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, 0))

label_sended.pack()
text_box.pack()
button_send.pack()

window.mainloop()

# from tkinter import *
#
# root = Tk()
# canvas = Canvas(root)
# canvas.pack()
#
# lst = []
# y = 0
# for i in range(1, 100):
#     label = Label(canvas, text="File number " + str(i), font=("Courier", 44), compound=RIGHT)
#     canvas.create_window(0, y, window=label, anchor=NW)
#     y += 60
#
# scrollbar = Scrollbar(canvas, orient=VERTICAL, command=canvas.yview)
# scrollbar.place(relx=1, rely=0, relheight=1, anchor=NE)
# canvas.config(yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, y))
# root.mainloop()