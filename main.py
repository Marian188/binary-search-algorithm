import io
from contextlib import redirect_stdout
import tkinter as tk
import platform, time, sys
from tkinter import filedialog, X, RIGHT

root = tk.Tk()

canvas1 = tk.Canvas(root, width=800, height=350)
canvas1.pack()
label2 = tk.Label(root, text='Gasirea pozitiei unui element in vector-Cautare binara')
label2.config(font=('Comic Sans MS', 12))
canvas1.create_window(400, 50, window=label2)
entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)
entry2 = tk.Entry(root)
canvas1.create_window(600, 140, window=entry2)

def convert(string):
    li = list(string.split(","))
    return li

'''def openFile():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/",
        title="Open Text file",
        filetypes=(("Text Files", "*.txt"),)
    )
    pathh.insert(tk.END, tf)
    tf = open(tf)
    data = tf.read()
    txtarea.insert(tk.END, data)
'''



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

sys.stdout = open('C:/Users/John/Desktop/ProiectLP/binary-search-algorithm/arbore.txt' , 'w')

def binary_search1(elem, data):
    low = 0
    high = len(data) - 1
    for i in dataa:
        print(i, end=' ')
    print(' ')
    while low <= high:

        middle = (low + high) // 2

       # mark=data[middle]

        def afisare():
            mark=0
            for i in range(0,(data[middle])):
                mark=mark+1
            print((mark-1)*'  '+'|')
            print((mark-1)*'  '+'|')
            print((mark - 1) * '  ' + str(data[middle]))

        afisare()
        if data[middle] == elem:
            return middle
        elif data[middle] > elem:
            high = middle - 1
        else:
            low = middle + 1
    return -1


elem=1
dataa=[1,2,3,4,5,6,7,8,9,10,11,12,13]

binary_search1(elem,dataa)


prompt = 'Aici vei afla daca vom regasi valoarea ta in vector'
label1 = tk.Label(root, text=prompt)
label1.config(fg='green', font=('Comic Sans MS', 10, 'bold'))
canvas1.create_window(400, 230, window=label1)

'''def sortare(list):
    list=list.sort()
    return list'''



def afisare():
    if binary_search1(entry2.get(),convert(entry1.get()))!= -1:
        result = 'Am gasit valoarea ta la pozitia: ' + str(binary_search1(entry2.get(), convert(entry1.get())) + 1)
    else:
        result = 'Nu am gasit valoarea ta'
    label1.config(text=result, width=50)
    label1.update_idletasks()

'''
prompt = 'Aici vei afla daca vom regasi valoarea ta in fisier'
label2 = tk.Label(root, text=prompt)
label2.config(fg='green', font=('Comic Sans MS', 10, 'bold'))
canvas1.create_window(600, 230, window=label2)


def afisare_din_txt():
    if binary_search1(entry2.get(), txtarea.get("1.0", tk.END)) != -1:
        result = 'From text :  Am gasit valoarea ta la pozitia: ' + str(binary_search1(entry2.get(), txtarea.get("1.0",tk.END)) + 1)
    else:
        result = 'Nu am gasit valoarea ta'
    label2.config(text=result, width=50)
    label2.update_idletasks()
'''






'''pathh = tk.Entry(root)
pathh.pack(side=tk.LEFT, expand=True, fill=X, padx=20)

tk.Button(root, text="Open File", command=openFile).pack(side=RIGHT, expand=True, fill=X, padx=20)'''


#button2 = tk.Button(text='Cauta2', command=afisare_din_txt, bg='blue', fg='yellow', font=('helvetica', 9, 'bold'))
#canvas1.create_window(600, 200, window=button2)
#txtarea = tk.Text(root, width=80, height=20)
#txtarea.pack(pady=20)
button1 = tk.Button(text='Cauta1', command=afisare, bg='blue', fg='yellow', font=('helvetica', 9, 'bold'))
canvas1.create_window(400, 200, window=button1)
#button1 = tk.Button(text='Genereaza arbore', command= aftree, bg='blue', fg='yellow', font=('helvetica', 9, 'bold'))
#canvas1.create_window(400, 300, window=button1)







sys.stdout.close()

with open('arbore.txt', 'r') as f:
    txtarea = tk.Text(root, width=40, height=20)
    txtarea.pack(pady=10)
    data=f.read()
    txtarea.insert(tk.END,data)

root.mainloop()
