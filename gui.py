import Tkinter, tkSimpleDialog

root = Tkinter.Tk()
root.withdraw()

numero = tkSimpleDialog.askinteger("Enero", "Introduce un entero")
print numero
string = tkSimpleDialog.askstring("Enero", "Introduce un String")
print string