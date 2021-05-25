import tkinter as tk
import sys

root = tk.Tk()
canvas_1 = tk.Canvas(root, width=800, height=400)
canvas_1.pack()
label2 = tk.Label(root, text='Gasirea pozitiei unui element in vector-Cautare binara')
label2.config(font=('Comic Sans MS', 12))
canvas_1.create_window(400, 50, window=label2)

canvas_1.create_window(200, 25, window=label2)
entry1 = tk.Entry(root)

canvas_1.create_window(100, 140, window=entry1)
entry2 = tk.Entry(root)
canvas_1.create_window(600, 140, window=entry2)


def convert(string):
    li = list(string.split(","))
    return li


canvas_1.create_window(300, 140, window=entry2)


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

        # mark=data[middle]

        def afisare():
            mark = 0
            for i in range(0, (data[middle])):
                mark = mark + 1
            print((mark - 1) * '  ' + '|')
            print((mark - 1) * '  ' + '|')
            print((mark - 1) * '  ' + str(data[middle]))

        afisare()

        if data[middle] == elem:
            return middle
        elif data[middle] > elem:
            high = middle - 1
        else:
            low = middle + 1
    return -1




# elem = 1
# dataa = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# binary_search2(elem, dataa)


prompt = 'Aici vei afla daca vom regasi valoarea ta in vector'
label1 = tk.Label(root, text=prompt)
label1.config(fg='green', font=('Comic Sans MS', 10, 'bold'))
canvas_1.create_window(200, 230, window=label1)


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
    for i in data:
        if i.isnumeric():
            vector.append(int(i))
    element = int(element)
    binary_search2(element, vector)
    sys.stdout.close()
    txtarea_afisare()

def txtarea_afisare():
    txtarea.delete('1.0', tk.END)
    with open('arbore.txt', 'r') as f:
        data = f.read()
        txtarea.insert(tk.END, data)






txtarea = tk.Text(root, width=40, height=20)
txtarea.pack(pady=10)
button1 = tk.Button(text='Cauta', command=afisare, bg='blue', fg='yellow', font=('helvetica', 9, 'bold'))
button_2 = tk.Button(text='Arbore', command= lambda: arbore(entry1.get(),entry2.get()), bg='blue', fg='yellow', font=('helvetica', 9, 'bold'))
canvas_1.create_window(200, 180, window=button1)
canvas_1.create_window(200, 250, window=button_2)


root.mainloop()