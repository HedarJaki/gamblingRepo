import tkinter as tk

def tekan(tombol) :
    if tombol == "=":
        try:
            hasil = str(eval(entry.get()))
            entry.delete (0,tk.END)
            entry.insert(tk.END, hasil)
        except:
            entry.Delete(0,tk.END)
            entry.Insert(tk.END,"error")
    elif tombol == "C":
        entry.delete(0,tk.END)
    else :
        entry.insert(tk.END, tombol)

root = tk.Tk()
root.title("kalkulator")

entry = tk.Entry(root, width=16, font=("Arial,24"), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

tombol_list = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for tombol in tombol_list:
    btn=tk.Button(root, text=tombol, width=5, height=2,font=("Arial",18), command=lambda t=tombol: tekan(t))
    btn.grid(row=row_val, column=col_val)
    col_val += 1
    if col_val>3 :
        col_val = 0
        row_val += 1

root.mainloop()