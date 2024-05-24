import openpyxl
import tkinter as tk
import pandas as pd

root = tk.Tk()
root.title('Globle')
root.geometry('500x200')

wb = openpyxl.load_workbook('Globle.xlsx')
ws = wb.active

entry = tk.Entry(root)
entry.pack()

df = pd.read_excel('Globle.xlsx', sheet_name='Sheet1')

def add():
    country = (entry.get()).capitalize()
    countries = df['Countries'].dropna().tolist()
    if country not in countries:
        ws.append([country])
        wb.save('Globle.xlsx')
    else:
        print('You already added that country and all these ones too:\n '+'\n'.join(countries.remove(country)))
    if len(countries) == 195:
        print('you did it, you got all countries in globle')
    
    
button = tk.Button(root, text='add', command=add)
button.pack()

root.mainloop()