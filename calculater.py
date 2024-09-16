from tkinter import *
def buttonClick(number):
    global operater
    operater = operater + str(number)
    input_value.set(operater)
def buttonClear():
    global operater
    operater = ""
    input_value.set("")
def buttonEqual():
    global operater
    result = str(eval(operater))
    input_value.set(result)
    operater = ""
main = Tk()
main.title("Calculator")

operater = ""
input_value = StringVar()
display_text = Entry(main, font=("arial",20 ,"bold"),textvariable=input_value,bd=4,insertwidth=4,
                     bg="light gray",justify=RIGHT)
display_text.grid(columnspan=4)
# first row of numders on caluculater
but_7 = Button(main, padx=16,bd=8,fg='black',font=("arial",20,"bold"),text="7",command=lambda:buttonClick(7))
but_7.grid(column=0,row=1)

but_8 = Button(main, padx=16,bd=8,fg='black',font=("arial",20,"bold"),text="8",command=lambda:buttonClick(8))
but_8.grid(column=1,row=1)

but_9 = Button(main, padx=16,bd=8,fg='black',font=("arial",20,"bold"),text="9",command=lambda:buttonClick(9))
but_9.grid(column=2,row=1)

but_add = Button(main, padx=16,bd=8,fg='black',font=("arial",20,"bold"),text="+",command=lambda:buttonClick("+"))
but_add.grid(column=3,row=1)

# row two of calculater

but_4 = Button(main, padx=16,bd=8,fg='black',font=("arial",20,"bold"),text="4",command=lambda:buttonClick(4))
but_4.grid(column=0,row=2)

but_5 = Button(main, padx=16,bd=8,fg='black',font=("arial",20,"bold"),text="5",command=lambda:buttonClick(5))
but_5.grid(column=1,row=2)


but_6 = Button(main, padx=16,bd=8,fg='black',font=("arial",20,"bold"),text="6",command=lambda:buttonClick(6))
but_6.grid(column=2,row=2)

but_sub = Button(main, padx=16,bd=8,fg='black',font=("arial",20,"bold"),text="-",command=lambda:buttonClick("-"))
but_sub.grid(column=3,row=2)

# THERD ROW

but_1 = Button(main, padx=16,bd=8,fg='black',font=("arial",20,"bold"),text="1",command=lambda:buttonClick(1))
but_1.grid(column=0,row=3)

but_2 = Button(main, padx=16,bd=8,fg='black',font=("arial",20,"bold"),text="2",command=lambda:buttonClick(2))
but_2.grid(column=1,row=3)


but_3 = Button(main, padx=16,bd=8,fg='black',font=("arial",20,"bold"),text="3",command=lambda:buttonClick(3))
but_3.grid(column=2,row=3)

but_multi = Button(main, padx=16,bd=8,fg='black',font=("arial",20,"bold"),text="*",command=lambda:buttonClick("*"))
but_multi.grid(column=3,row=3)
 
# forth row

but_0 = Button(main, padx=16,bd=8,fg='black',font=("arial",20,"bold"),text="0",command=lambda:buttonClick(0))
but_0.grid(column=0,row=4)

but_c = Button(main, padx=16,bd=8,fg='black',font=("arial",20,"bold"),text="C",command = buttonClear)
but_c.grid(column=1,row=4)


but_equal = Button(main, padx=16,bd=8,fg='black',font=("arial",20,"bold"),text="=",command = buttonEqual)
but_equal.grid(column=2,row=4)

but_div = Button(main, padx=16,bd=8,fg='black',font=("arial",20,"bold"),text="/",command=lambda:buttonClick("/"))
but_div.grid(column=3,row=4)

main.mainloop()