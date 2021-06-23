import tkinter as tk
import math

def add_digit(digit):
	value = calc.get()
	if value [0]=='0' and len(value)==1:
		value = value[1:]
	calc.delete(0, tk.END)
	calc.insert(0, digit)

def add_op(operation):
	value = calc.get()
	if value[-1] in '-+/*':
		value = value[:-1]
	elif '+' in value or '-' in value or '*' in value or '/' in value:
		calculate()
		value = calc.get()
	calc.delete(0, tk.END)
	calc.insert(0, digit)

def calculate():
	value = calc.get()
	if value[-1] in '+-/*':
		value = value + value[:-1]
	calc.delete(0, tk.END)
	calc.insert(0, eval(value))

def clear():
	calc.delete(0,tk.END)
	calc.insert(0,0)


def make_op_button(operation):
	return tk.Buttton (text=operation, command = lambda: add.digit(operation))

def make_calc_button(operation):
	return tk.Buttton (text=operation, command = lambda: add.op(operation))

def make_calc_button(operation):
	return tk.Buttton (text=operation, command =calculate)

def make_del_button(operation):
	return tk.Buttton (text=operation, command =clear)

def oper_button(operation):
	value=calc.get()
	if value[-1] in '+-*/%':
		value=value[:-1]
	if operation == 'sin':
		value= math.sin(int(value))
	elif operation == 'cos':
		value= math.cos(int(value))
	elif operation == 'tan':
		value= math.tan(int(value))
	elif operation == 'ctg':
		value= math.ctg(int(value))
	elif operation == 'log':
		value= math.log10(int(value))
		print("log")
	elif operation == 'ln':
		value= math.log1(int(value))
	if operation == '%':
		value= math.percent(int(value))
	calc.delete(0, tk.END)
	calc.insert(0, eval(value))


win = tk.Tk()
win.geometry(f"540x550+100+200")
win['bg'] = '#33ffe6'
win.title('Калькулятор')


calc = tk.Entry(win, justify = tk.RIGHT)
calc.insert(0, '0')
calc.grid(row = 0, column = 0, columnspan=4, stick = 'wid')

tk.Button(text = '1', command=lambda: add_digit(1)).grid(row=1, column=0, stick='wens')
tk.Button(text = '2', command=lambda: add_digit(2)).grid(row=1, column=1, stick='wens')
tk.Button(text = '3', command=lambda: add_digit(3)).grid(row=1, column=2, stick='wens')
tk.Button(text = '4', command=lambda: add_digit(4)).grid(row=2, column=0, stick='wens')
tk.Button(text = '5', command=lambda: add_digit(5)).grid(row=2, column=1, stick='wens')
tk.Button(text = '6', command=lambda: add_digit(6)).grid(row=2, column=2, stick='wens')
tk.Button(text = '7', command=lambda: add_digit(7)).grid(row=3, column=0, stick='wens')
tk.Button(text = '8', command=lambda: add_digit(8)).grid(row=3, column=1, stick='wens')
tk.Button(text = '9', command=lambda: add_digit(9)).grid(row=3, column=2, stick='wens')
tk.Button(text = '0', command=lambda: add_digit(0)).grid(row=4, column=0, stick='wens')

make_op_button('+').grid(row=1, column=3, stick='wens')
make_op_button('-').grid(row=2, column=3, stick='wens')
make_op_button('/').grid(row=3, column=3, stick='wens')
make_op_button('*').grid(row=4, column=3, stick='wens')
make_calc_button('=').grid(row=4, column=2, stick='wens')
make_del_button('C').grid(row=4, column=1, stick='wens')

make_oper_button('sin').grid(row=4, column=3, stick='wens')
make_oper_button('cos').grid(row=4, column=3, stick='wens')
make_oper_button('tan').grid(row=4, column=3, stick='wens')
make_oper_button('ctg').grid(row=4, column=3, stick='wens')
make_oper_button('ln').grid(row=4, column=3, stick='wens')
make_oper_button('log').grid(row=4, column=3, stick='wens')
make_oper_button('%').grid(row=4, column=3, stick='wens')

win.grid_columnconfigure(0, minsize = 60)
win.grid_colunmconfigure(1, minsize = 60)
win.grid_columnconfigure(2, minsize = 60)
win.grid_columnconfigure(3, minsize = 60)


win.grid_rowconfigure(1, minsize = 60)
win.grid_rowconfigure(2, minsize = 60)
win.grid_rowconfigure(3, minsize = 60)
win.grid_rowconfigure(4, minsize = 60)
win.mainloop()




 