import tkinter as tk

def suma(a, b):
	resultado = a + b 
	return resultado

def resta(a, b):
	resultado = a - b
	return resultado

def multiplicacion(a, b):
	resultado = a * b
	return resultado

def division(a, b):
	resultado = a / b

class Calculadora(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.title("Calculadora")
		
		#Botones para operaciones
		self.restar = tk.Button(self, text="-", width= 8, height=3, fg="red", bg="lightgrey", command= lambda: self.tipo_operacion(1))
		self.sumar = tk.Button(self, text="+", width= 8, height=3, fg="red", bg="lightgrey")
		self.multip = tk.Button(self, text="*", width= 8, height=3, fg="red", bg="lightgrey")
		self.divid = tk.Button(self, text="/", width= 8, height=3, fg="red", bg="lightgrey")
		self.igual = tk.Button(self, text="=", width=8, height=3, fg="red", bg="lightgrey")
		self.geometry("330x360")
		
		self.cuadro = tk.Text(self, width=24, height=2, font="10")
		
		#Espacios en blanco
		self.blank_space1 = tk.Label(self, width=4, height=20)
		self.blank_space2 = tk.Label(self, width=15, height=1)
		self.blank_space3 = tk.Label(self, width=15, height=1)
		
		#Botones para escribir las cantidades
		self.butt_1 = tk.Button(self, text="1", width= 8, height=3, command= lambda: self.escribir(1))
		self.butt_2 = tk.Button(self, text="2", width= 8, height=3, command= lambda: self.escribir(2))
		self.butt_3 = tk.Button(self, text="3", width= 8, height=3, command= lambda: self.escribir(3))
		self.butt_4 = tk.Button(self, text="4", width= 8, height=3, command= lambda: self.escribir(4))
		self.butt_5 = tk.Button(self, text="5", width= 8, height=3, command= lambda: self.escribir(5))
		self.butt_6 = tk.Button(self, text="6", width= 8, height=3, command= lambda: self.escribir(6))
		self.butt_7 = tk.Button(self, text="7", width= 8, height=3, command= lambda: self.escribir(7))
		self.butt_8 = tk.Button(self, text="8", width= 8, height=3, command= lambda: self.escribir(8))
		self.butt_9 = tk.Button(self, text="9", width= 8, height=3, command= lambda: self.escribir(9))
		self.butt_0 = tk.Button(self, text="0", width= 8, height=3, command= lambda: self.escribir(0))
		self.butt_punt = tk.Button(self, text=".", width=8, height=3)

		#Acomodando botones de operaciones 
		self.sumar.grid(row=3, column=4)
		self.restar.grid(row=4, column=4)
		self.multip.grid(row=5, column=4)
		self.divid.grid(row=6, column=4)
		self.igual.grid(row=6, column=3)
		
		self.cuadro.grid(row=1, columnspan=4, column=1)
		
		#Acomoda botones de escribir
		self.butt_1.grid(row=3, column=1)
		self.butt_2.grid(row=3, column=2)
		self.butt_3.grid(row=3, column=3)
		self.butt_4.grid(row=4, column=1)
		self.butt_5.grid(row=4, column=2)
		self.butt_6.grid(row=4, column=3)
		self.butt_7.grid(row=5, column=1)
		self.butt_8.grid(row=5, column=2)
		self.butt_9.grid(row=5, column=3)
		self.butt_0.grid(row=6, column=2)
		self.butt_punt.grid(row=6, column=1)

			
		self.blank_space1.grid(column=0)
		self.blank_space2.grid(columnspan=4, row=2, column=1)
		self.blank_space3.grid(columnspan=4, row=0, column=1)
		
	def escribir(self, numero):
		numero_str = str(numero)
		self.cuadro.insert('end', numero_str)
		
	def tipo_operacion(self, operacion):
		if operacion == 1:
			self.cuadro.insert('end', " + ")
			
		
		
ventana = Calculadora()
ventana.mainloop()
