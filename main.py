import tkinter as tk
import sys


root = tk.Tk()

canvas_1 = tk.Canvas(root, width=1000, height=400 )
canvas_1.pack()



label2 = tk.Label(root, text='Gasirea pozitiei unui element in vector-Cautare binara' )
label2.config(font=('Comic Sans MS', 12))
canvas_1.create_window(500, 25, window=label2)


label3 = tk.Label(root, text='Element cautat:' )
label3.config(font=('Comic Sans MS', 10,'bold'))
canvas_1.create_window(380, 140, window=label3)

label1 = tk.Label(root, text='Vector:' )
label1.config(font=('Comic Sans MS', 10,'bold'))
canvas_1.create_window(400, 100, window=label1)

label4 = tk.Label(root, text='Algoritmul functioneaza in felul urmator:' )
label4.config(font=('Comic Sans MS', 10,'bold'))
canvas_1.create_window(432, 400, window=label4)

entry1 = tk.Entry(root)
canvas_1.create_window(500, 100, window=entry1)
entry1.config(bg='yellow')
entry2 = tk.Entry(root)
canvas_1.create_window(500, 140, window=entry2)
entry2.config(bg='yellow')


def convert(string):
    li = list(string.split(","))
    return li


def binary_search1(elem, data):
    low = 0
    high = len(data) - 1

    while low <= high:

        middle = (low + high) // 2
        if data[middle] == elem:
            return middle
        elif data[middle] > elem:
            high = middle - 1
        else:
            low = middle + 1
    return -1



def binary_search2(elem, data):
    low = 0
    high = len(data) - 1
    for i in data:
        print(i, end=' ')
    print(' ')
    while low <= high:

        middle = int((low + high) / 2)



        def afisare():
            if(elem>10):
               print((middle ) * '   ' + '|')
               print((middle ) * '   ' + '|')
               print((middle ) * '   ' + str(data[middle]))
            elif(elem<10):
                print((middle) * '  ' + '|')
                print((middle) * '  ' + '|')
                print((middle) * '  ' + str(data[middle]))

        afisare()

        if data[middle] == elem:
            return middle
        elif data[middle] > elem:
            high = middle - 1
        else:
            low = middle + 1
    return -1



prompt = 'Aici vei afla daca vom regasi valoarea ta in vector'
label1 = tk.Label(root, text=prompt)
label1.config(fg='black', font=('Comic Sans MS', 10, 'bold'))
canvas_1.create_window(500, 250, window=label1)


def afisare():
    if binary_search1(entry2.get(), convert(entry1.get())) != -1:
        result = 'Am gasit valoarea ta la pozitia: ' + str(binary_search1(entry2.get(), convert(entry1.get())) + 1)
    else:
        result = 'Nu am gasit valoarea ta'
    label1.config(text=result, width=50)
    label1.update_idletasks()


def arbore(data,element):
    sys.stdout = open('arbore.txt', 'w')
    vector = []
    for i in convert(data):
        if i.isnumeric():
            vector.append(int(i))
    element = int(element)

    if binary_search1(entry2.get(), convert(entry1.get())) != -1:
           binary_search2(element, vector)
    else:
        print('Valoarea ta nu se regaseste in vector,'+'\n'+ 'asadar nu putem genera un arbore')
    sys.stdout.close()
    txtarea_afisare()

def txtarea_afisare():
    txtarea.delete('1.0', tk.END)
    with open('arbore.txt', 'r') as f:
        data = f.read()
        txtarea.insert(tk.END, data)


txtarea = tk.Text(root ,width=50, height=20,bg='black',fg='yellow')
txtarea.pack(pady=20)
button1 = tk.Button(text='Cauta', command=afisare, bg='black', fg='yellow', font=('helvetica', 9, 'bold'))
button_2 = tk.Button(text='Arbore', command= lambda: arbore(entry1.get(),entry2.get()), bg='black', fg='yellow', font=('helvetica', 9, 'bold'))
canvas_1.create_window(500, 200, window=button1)
canvas_1.create_window(500, 300, window=button_2)


root.mainloop()