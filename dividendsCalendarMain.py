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