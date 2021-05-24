import tkinter as tk

root = tk.Tk()


canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()
label2 = tk.Label(root, text='Gasirea pozitiei unui element in vector-Cautare binara')
label2.config(font=('helvetica', 12))
canvas1.create_window(200, 25, window=label2)
entry1 = tk.Entry(root)
canvas1.create_window(100, 140, window=entry1)
entry2 = tk.Entry(root)
canvas1.create_window(300, 140, window=entry2)



def binary_search():
    elem = entry2.get()
    data = entry1.get()
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

def afisare():
    if binary_search() != -1:
        result='Am gasit valoarea ta la pozitia: '+ str(binary_search()+1)
    else:
        result='Nu am gasit valoarea ta'
    label1 = tk.Label(root, text=result)
    canvas1.create_window(200, 230, window=label1)




button1 = tk.Button(text='Cauta',command=afisare,bg='blue', fg='yellow', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()