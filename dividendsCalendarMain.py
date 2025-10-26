import tkinter as tk 
from tkinter import ttk, messagebox
import yfinance as yf
import pandas as pd 


class DividendsCalendar:
    def __init__(self,root):

        self.root=root
        self.root.title("Dividends Calendar")
        self.root.geometry("400x300")

        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="Enter LOT-Code: ").pack(pady=5)
        self.entry=tk.Entry(self.root,width=60)
        self.entry.pack(pady=5)

    tk.Button(self.root, text="Get a Dividend",command=self.getDividends).pack(pady=5)

    self.tree=ttk.Treeview(self.root, column=("Date","Dividend"),show="headings")

    self.tree.heading("Date", text("DD/MM/YYYY"))    
    self.tree.heading("Dividends", text="Cumulative Dividends")

    self.tree.pack(expand=true, fill="both",padx=10)

    def getDividends(self):
        lotCode = self.entry.get().upper()
        if not lotCode:
            messagebox.showwarning("Caution!", "Please Enter a Valid Code of Lot")
            return
        
        try:
            stock=yf.ticker(lotCode)
            df.stock.dividend

            self.tree.delete(*self.tree.get_children())


        if df.empty:
            messagebox.showinfo("Info:","Dividends Data Could Not Be Found!")
            return 
        
        df=df.tail(20)

        for date,divid in df.items():
            self.tree.insert("", "End", values=(date.strftime("%Y-%M-%D"),f"{divid:.2f}"))

    except Exception as e :
    messagebox.showerror("Error", f"Data Cannot Be Received:{str(e)}")
        
if __name__=="__main__":
    root=tk.Tk()
    app=DividendsCalendar(root)
    root.mainloop()
