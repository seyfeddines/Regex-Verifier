import tkinter as tk
import os
from tkinter import filedialog
import re
list_numb = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list_ident = ['_', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
list_sper = [':', '(', ')', '.', ',', ';', '.']
list_opr = ['+', '-', '=', '*', '<', '>', '/','||']

def separate_with_hash(input_string):
    result = []
    i = 0

    while i < len(input_string):
        char = input_string[i]

        if char in list_numb:
            while i < len(input_string) and (input_string[i] in list_numb or input_string[i] in list_ident or input_string[i] == '.') and (i+1 == len(input_string) or input_string[i+1] not in list_numb):
                if i> 0 and input_string[i] == '.' and  input_string[i+1]  in list_numb and input_string[i-1] not in list_numb :
                    result.append('#')
                    print("helo")
                    result.append(input_string[i])#3.4
                    result.append('#')
                elif i > 0 and input_string[i-1] in list_numb and input_string[i] == '.' and (i+1 == len(input_string) and input_string[i+1] not in list_numb) :
                    result.append('#')
                    result.append(input_string[i])#3.4
                    result.append('#')
                
                else:
                    result.append(input_string[i])
                    i += 1
             

            result.append('#')

        elif char in list_ident:
            while i < len(input_string) and (input_string[i] in list_ident or input_string[i] in list_numb):#aaaa1
                result.append(input_string[i])
                i += 1
            result.append('#')

        elif char in [':']:            #:=
            result.append(input_string[i])
            i += 1
            if i < len(input_string) and input_string[i] == '=':
                result.append(input_string[i])
                result.append('#')
                i += 1

        elif char in list_sper: #separatore
            result.append(input_string[i])
            result.append('#')
            i += 1

        elif char in ['=']: # ==#=
            result.append(input_string[i])
            i += 1
            if i < len(input_string) and input_string[i] == '=':
                result.append(input_string[i])
                i += 1
            if i < len(input_string) and input_string[i] in list_opr:
                result.append('#')
                result.append(input_string[i])
                i += 1

        elif char in ['>']: #>=
            result.append(input_string[i])
            i += 1
            if i < len(input_string) and input_string[i] == '=':
                result.append(input_string[i])
                result.append('#')
                i += 1

        elif char in ['<']:  #<=
            result.append(input_string[i])
            i += 1
            if i < len(input_string) and input_string[i] == '=':
                result.append(input_string[i])
                result.append('#')
                i += 1

        elif char in ['+']: #+=
            result.append(input_string[i])
            i += 1
            if i < len(input_string) and input_string[i] == '=':
                result.append(input_string[i])
                result.append('#')
                i += 1
            elif i < len(input_string) and input_string[i] == '+':
                if i > 1 and input_string[i-2] in list_numb and i+1 < len(input_string) and input_string[i+1] in list_numb:
                    result.append('#')
                    result.append(input_string[i])
                    i += 1
                elif i > 1 and input_string[i-2] in list_ident and i+1 < len(input_string) and input_string[i+1] in list_ident:
                    result.append('#')
                    result.append(input_string[i])
                    i += 1
                elif i > 1 and input_string[i-2] in list_ident:
                    result.append(input_string[i])
                    result.append('#')
                    i += 1
            elif i < len(input_string) and input_string[i] == '-': ###################
                if i > 1 and input_string[i-2] in list_numb and i+1 < len(input_string) and input_string[i+1] in list_numb:
                    result.append('#')
                    result.append(input_string[i])
                    i += 1
                elif i > 1 and input_string[i-2] in list_ident and i+1 < len(input_string) and input_string[i+1] in list_ident:
                    result.append('#')
                    result.append(input_string[i])
                    i += 1
            elif i < len(input_string) and input_string[i] in list_numb:#new
                if i == 1:
                    result.append(input_string[i])
                    result.append('#')
                    i += 1
                elif i > 1 and input_string[i-2] in list_numb:
                    result.append('#')
                    result.append(input_string[i])
                    i += 1

        elif char in ['-']:
            result.append(input_string[i])
            i += 1
            if i < len(input_string) and input_string[i] == '=':
                result.append(input_string[i])
                result.append('#')
                i += 1
            elif i < len(input_string) and input_string[i] == '-':
                if i > 1 and input_string[i-2] in list_numb and i+1 < len(input_string) and input_string[i+1] in list_numb:
                    result.append('#')
                    result.append(input_string[i])
                    i += 1
                elif i > 1 and input_string[i-2] in list_ident:
                    result.append(input_string[i])
                    result.append('#')
                    i += 1
            elif i < len(input_string) and input_string[i] in list_numb:
                if i == 1:
                    result.append(input_string[i])
                    i += 1
                elif i > 1 and input_string[i-2] in list_numb:
                    result.append('#')
                    result.append(input_string[i])
                    i += 1
            elif i < len(input_string) and input_string[i] == '+':
                if i > 1 and input_string[i-2] in list_numb and i+1 < len(input_string) and input_string[i+1] in list_numb:
                    result.append('#')
                    result.append(input_string[i])
                    i += 1
                elif i > 1 and input_string[i-2] in list_ident and i+1 < len(input_string) and input_string[i+1] in list_ident:
                    result.append('#')
                    result.append(input_string[i])
                    i += 1
            elif i < len(input_string) and input_string[i] in list_numb:
                if i == 1:
                    result.append(input_string[i])
                    result.append('#')
                    i += 1
                elif i > 1 and input_string[i-2] in list_numb:
                    result.append('#')
                    result.append(input_string[i])
                    i += 1

        elif char in list_opr:
            result.append(input_string[i])
            i += 1
            result.append('#')

        else:
            result.append(char)
            i += 1

    return ''.join(result)

def delete_comntaire(input_1) :
    clean=""
    startIndx = 0
    endIndx = 0
    while endIndx < len(input_1) :
        if input_1[endIndx] == '%' :
            clean += input_1[startIndx:endIndx] + ''
            startIndx = endIndx = endIndx + 1
            while endIndx < len(input_1) and input_1[endIndx] != '%' :
                endIndx += 1
            if endIndx < len(input_1) :
                startIndx = endIndx + 1
        else:
            endIndx += 1
    clean += input_1[startIndx:endIndx]
    return clean

def past() :
    s = iput.get("1.0",tk.END)
    s = delete_comntaire(s)
    s = re.sub('\s+',' ',s)
    s=separate_with_hash(s)
    oput.delete("1.0",tk.END)
    oput.insert(tk.END,s)

def separate_characters_manually(word):
    separated_word = ''
    for i, char in enumerate(word):
        if i > 0:
            separated_word += '#'
        separated_word += char
    return separated_word

    print(tranlatestring)
def save_to_file():
    content = iput.get()  
    with open('output.txt', 'w') as file:
        file.write(content)
def show_input():
    input_text = iput.get()
    label = tk.Label(root, text="You entre: " + input_text)
    label.pack()
def open_dosser():
    os.system('open output.txt')
def new_dosser():
    folder_path = filedialog.askopenfilename(title="select file",filetypes=(("txt files","*.txt"),("all filles","*.*")))  
    with open(folder_path, 'r') as file:
        vars=file.read(str)
        iput.insert(vars)
def suprimer():
     iput.delete("1.0", tk.END)
     oput.delete("1.0", tk.END)
     
root = tk.Tk()
path="/Users/user/Desktop/output.txt"
root.geometry("500x500")
root.title("Input String")
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
file_menu = tk.Menu(menu_bar, tearoff=0)  
menu_bar.add_cascade(label="File", menu=file_menu)  
file_menu.add_command(label="suprimer",command=suprimer)  
file_menu.add_command(label="new",command=new_dosser)  
file_menu.add_command(label="Open",command=open_dosser) 
file_menu.add_command(label="save",command=save_to_file)  
file_menu.add_separator()  
file_menu.add_command(label="Exit", command=root.quit)
iput = tk.Text(root,height=20,width=20)
iput.place(x=20,y=20)
oput = tk.Text(root,height=20,width=20)
oput.place(x=390,y=20)
btn = tk.Button(root,text="translate",width=10,command=past)
btn.place(x=200,y=330)
root.mainloop()
