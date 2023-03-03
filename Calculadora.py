from tkinter import *

vent = Tk()
vent.title('CALCULADORA')

i = 0
#entrada texto
e_t = Entry(vent, font=("Calibri 20"))
e_t.grid(row = 0,column = 0, columnspan = 4, padx = 5, pady =5)

#funciones
def click(valor):
    global i
    e_t.insert(i,valor)
    i+=1

def borrar():
    e_t.delete(0,END)
    i = 0

def operaciones():
    ecuacion = e_t.get()
    resultado = eval(ecuacion)
    e_t.delete(0, END)
    e_t.insert(0,resultado)
    i = 0

#botones
btn1 = Button(vent, text = " 1 ", width = 5,  height = 2, command = lambda: click(1))
btn2 = Button(vent, text = " 2 ", width = 5,  height = 2, command = lambda: click(2))
btn3 = Button(vent, text = " 3 ", width = 5,  height = 2, command = lambda: click(3))
btn4 = Button(vent, text = " 4 ", width = 5,  height = 2, command = lambda: click(4))
btn5 = Button(vent, text = " 5 ", width = 5,  height = 2, command = lambda: click(5))
btn6 = Button(vent, text = " 6 ", width = 5,  height = 2, command = lambda: click(6))
btn7 = Button(vent, text = " 7 ", width = 5,  height = 2, command = lambda: click(7))
btn8 = Button(vent, text = " 8 ", width = 5,  height = 2, command = lambda: click(8))
btn9 = Button(vent, text = " 9 ", width = 5,  height = 2, command = lambda: click(9))
btn0 = Button(vent, text = " 0 ", width = 15,  height = 2, command = lambda: click(0))

btn_del = Button(vent, text = chr(9003), width = 5,  height = 2, command = lambda: borrar())
btn_par1 = Button(vent, text = " ( ", width = 5,  height = 2, command = lambda: click("("))
btn_par2 = Button(vent, text = " ) ", width = 5,  height = 2, command = lambda: click(")"))
btn_dot = Button(vent, text = " . ", width = 5,  height = 2, command = lambda: click("."))

btn_sum = Button(vent, text = " + ", width = 5,  height = 2, command = lambda: click("+"))
btn_res = Button(vent, text = " - ", width = 5,  height = 2, command = lambda: click("-"))
btn_mult = Button(vent, text = " X ", width = 5,  height = 2, command = lambda: click("*"))
btn_div = Button(vent, text = chr(247), width = 5,  height = 2, command = lambda: click("/"))
btn_igu = Button(vent, text = " = ", width = 5,  height = 2, command = lambda: operaciones())

#posicionar botones en pantalla

btn_del.grid(row = 1, column = 0 , padx = 5, pady = 5)
btn_par1.grid(row = 1, column = 1, padx = 5, pady = 5)
btn_par2.grid(row = 1, column = 2, padx = 5, pady = 5)
btn_div.grid(row = 1, column = 3, padx = 5, pady = 5)

btn7.grid(row = 2, column = 0 , padx = 5, pady = 5)
btn8.grid(row = 2, column = 1, padx = 5, pady = 5)
btn9.grid(row = 2, column = 2, padx = 5, pady = 5)
btn_mult.grid(row = 2, column = 3, padx = 5, pady = 5)

btn4.grid(row = 3, column = 0 , padx = 5, pady = 5)
btn5.grid(row = 3, column = 1, padx = 5, pady = 5)
btn6.grid(row = 3, column = 2, padx = 5, pady = 5)
btn_res.grid(row = 3, column = 3, padx = 5, pady = 5)

btn1.grid(row = 4, column = 0 , padx = 5, pady = 5)
btn2.grid(row = 4, column = 1, padx = 5, pady = 5)
btn3.grid(row = 4, column = 2, padx = 5, pady = 5)
btn_sum.grid(row = 4, column = 3, padx = 5, pady = 5)

btn0.grid(row = 5, column = 0 , columnspan = 2, padx = 5, pady = 5)
btn_dot.grid(row = 5, column = 2, padx = 5, pady = 5)
btn_igu.grid(row = 5, column = 3, padx = 5, pady = 5)

vent.mainloop()