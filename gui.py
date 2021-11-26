import tkinter as TK
import pyperclip
import io
from tkinter.constants import INSERT
from TruthTableGenerator import generateTruthTable
import tkinter.messagebox
 
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
 
# 主窗口
root = TK.Tk( )
root.title("Truth table Caculator")
root.resizable(0, 0)
root.geometry('320x620')
 
result = TK.StringVar( )
equation = TK.StringVar( )
result.set(' ')
equation.set(' ')
 
# get the char
def getnum(num):
    temp = equation.get( )
    temp2 = result.get( )
    print(temp)
    print(temp2)
    if temp2 != ' ' :
        temp = ''
        temp2 = ' '
        result.set(temp2)
    temp = temp + num
    equation.set(temp)
    print(equation)
 
# delete the last char
def back( ):
    temp = equation.get( )
    equation.set(temp[:-1])
 
# clear the string
def clear( ):
    equation.set(' ')
    result.set(' ')
 
# get the truth table for the string
def run( ):
    temp = equation.get( )
    print(temp)
    buffer = io.StringIO()
    generateTruthTable(temp, reverse=False, markdown=False, file=buffer)
    print(buffer.getvalue())
    result.set(buffer.getvalue())
 
def copy_ans():
    pyperclip.copy(result.get())
    tkinter.messagebox.showinfo("successful!", "The result has been copied")

# show the result
show_uresult = TK.Label(root, bg = 'white', fg = 'black', font = ('Arail', '15'), bd = '0', textvariable = equation, anchor = 'se')
show_dresult = TK.Label(root, bg = 'white', fg = 'black', font = ('Arail', '10'), bd = '0', textvariable = result, anchor = 'se')
# show_dresult = TK.Text(root,bg='white',fg = 'black',font = ('Arail','10'),bd='0',)
show_uresult.place(x = '10', y = '10', width = '300', height = '50')
show_dresult.place(x = '10', y = '60', width = '300', height = '250')

# bottom
# first line
button_back = TK.Button(root,text = 'del',bg = 'DarkGray',command = back)
button_back.place(x = '10', y = '350', width = '60', height = '40')
button_double_bracket = TK.Button(root, text = '<->',bg = 'DarkGray',command = lambda : getnum('<->'))
button_double_bracket.place(x = '90', y = '350', width = '60', height = '40')
button_rbracket = TK.Button(root,text = '->', bg = 'DarkGray', command = lambda : getnum('->'))
button_rbracket.place(x = '170', y = '350', width = '60', height = '40')
button_copy = TK.Button(root, text = 'copy', bg = 'DarkGray', command = lambda : copy_ans())
button_copy.place(x = '250', y = '350', width = '60', height = '40')
# second line
button_h = TK.Button(root, text = 'h', bg = 'DarkGray', command = lambda : getnum('h'))
button_h.place(x = '10', y = '405', width = '60', height ='40')
button_i = TK.Button(root, text = 'i', bg = 'DarkGray', command = lambda : getnum('i'))
button_i.place(x = '90', y = '405', width = '60',height = '40')
button_j = TK.Button(root, text = 'j', bg = 'DarkGray', command = lambda : getnum('j'))
button_j.place(x = '170', y ='405', width = '60', height = '40')
button_and = TK.Button(root, text = '&', bg = 'DarkGray', command = lambda : getnum('&'))
button_and.place(x = '250', y = '405', width = '60', height = '40')
# third line
button_e = TK.Button(root,text = 'e',bg = 'DarkGray',command = lambda : getnum('e'))
button_e.place(x = '10',y = '460',width = '60',height = '40')
button_f = TK.Button(root,text = 'f', bg = 'DarkGray', command = lambda : getnum('f'))
button_f.place(x = '90',y = '460',width = '60', height = '40')
button_g = TK.Button(root,text = 'g', bg = 'DarkGray', command = lambda : getnum('g'))
button_g.place(x = '170',y='460', width = '60',height='40')
button_or = TK.Button(root, text = '|', bg = 'DarkGray', command = lambda : getnum('|'))
button_or.place(x = '250', y = '460', width = '60', height = '40')
# forth line
button_b = TK.Button(root, text = 'b',bg = 'DarkGray', command = lambda : getnum('b'))
button_b.place(x = '10',y = '515', width = '60', height = '40')
button_c = TK.Button(root, text = 'c', bg = 'DarkGray', command = lambda : getnum('c'))
button_c.place(x = '90', y = '515', width = '60', height = '40')
button_d = TK.Button(root, text = 'd', bg = 'DarkGray', command = lambda : getnum('d'))
button_d.place(x = '170',y = '515',width = '60', height = '40')
button_xor = TK.Button(root, text = '^', bg = 'DarkGray', command = lambda : getnum('^'))
button_xor.place(x = '250', y = '515', width = '60', height ='40')
# fifth line
button_MC = TK.Button(root, text = 'MC', bg = 'DarkGray', command = clear)
button_MC.place(x = '10', y = '570', width = '60', height = '40')
button_a = TK.Button(root, text = 'a', bg = 'DarkGray', command = lambda : getnum('a'))
button_a.place(x = '90', y = '570', width = '60', height = '40')
button_not = TK.Button(root, text = '¬', bg='DarkGray', command = lambda : getnum('¬'))
button_not.place(x = '170', y = '570', width = '60', height = '40')
button_done = TK.Button(root, text = 'done', bg = 'DarkGray', command = run)
button_done.place(x = '250', y = '570', width = '60', height = '40')
 
root.mainloop( )