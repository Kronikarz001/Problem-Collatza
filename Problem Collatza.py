#Problem Collatza - PROBLEM COLLATZA, ZWANY RÓWNIEŻ PROBLEMEM 3N + 1, TO NAJPROSTSZY, NIEMOŻLIWY
#DO UDOWODNIENIA PROBLEM MATEMATYCZNY. (ALE NIE MARTW SIĘ, PROGRAM SAM W
#SOBIE JEST WYSTARCZAJĄCO łatwy dla początkujących). Zaczynając od liczby n, zastosuj trzy zasady, by otrzymać
#kolejną liczbę w ciągu:
#(a) Jeśli liczba n jest parzysta, kolejna liczba n to n : 2.
#(b) Jeśli liczba n jest nieparzysta, kolejna liczba n to n ∗ 3c + 1.
#(c) Jeśli liczba n to 1, zatrzymaj. W przeciwnym razie powtórz.
#To ogólne sformułowanie, ale jak dotąd nieudowodnione matematycznie — każda liczba początkowa wcześniej czy później
#będzie miała wartość 1. Więcej informacji na temat problemu Collatza znajdziesz na stronie a.
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class CollatzCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Problem Collatza")
        self.root.attributes("-fullscreen", True)
        
        self.root.configure(bg='#8e44ad')
        
        self.frame = ttk.Frame(root, style='My.TFrame')
        self.frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.label_liczba = ttk.Label(self.frame, text="Podaj liczbę:", font=('Arial', 14), background='#8e44ad', foreground='white')
        self.label_liczba.grid(row=0, column=0, padx=10, pady=10)
        
        self.entry_liczba = ttk.Entry(self.frame, font=('Arial', 14))
        self.entry_liczba.grid(row=0, column=1, padx=10, pady=10)
        
        self.button_oblicz = ttk.Button(self.frame, text="Oblicz", command=self.oblicz_i_wyswietl_ciag, style='My.TButton', cursor='hand2')
        self.button_oblicz.grid(row=1, column=0, columnspan=2, pady=10)
        
        self.button_zamknij = ttk.Button(self.frame, text="Zamknij", command=self.zamknij_aplikacje, style='My.TButton', cursor='hand2')
        self.button_zamknij.grid(row=3, column=0, columnspan=2, pady=10)
        
        self.figure_frame = ttk.Frame(root, style='My.TFrame')
        self.figure_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.plot_area = self.figure.add_subplot(111)
        
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.figure_frame)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(fill=tk.BOTH, expand=True)
        
        self.wynik_treeview = ttk.Treeview(self.frame, columns=("L.p.", "Wartość ciągu"), show="headings", style='My.Treeview')
        self.wynik_treeview.heading("L.p.", text="L.p.")
        self.wynik_treeview.heading("Wartość ciągu", text="Wartość ciągu")
        self.wynik_treeview.grid(row=2, column=0, columnspan=2, pady=10, sticky="nsew")
        
        self.wynik_scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.wynik_treeview.yview)
        self.wynik_treeview.configure(yscrollcommand=self.wynik_scrollbar.set)
        self.wynik_scrollbar.grid(row=2, column=2, pady=10, sticky="ns")
    
    def Collatz(self, x):
        y = x % 2
        if y == 0:
            x = x / 2
            return x
        else:
            x = x * 3 + 1
            return x
    
    def generuj_ciag_collatza(self, liczba_poczatkowa):
        ciag_collatza = []
        liczba = liczba_poczatkowa
        
        while liczba != 1:
            ciag_collatza.append(int(liczba))
            liczba = self.Collatz(liczba)
        
        ciag_collatza.append(1)
        return ciag_collatza
    
    def oblicz_i_wyswietl_ciag(self):
        try:
            liczba_poczatkowa = int(self.entry_liczba.get())
            if liczba_poczatkowa <= 0:
                raise ValueError("Podana liczba musi być dodatnia.")
            
            self.plot_area.clear()
            
            ciag_collatza = self.generuj_ciag_collatza(liczba_poczatkowa)
            
            self.wynik_treeview.delete(*self.wynik_treeview.get_children())
            
            for index, value in enumerate(ciag_collatza, start=1):
                self.wynik_treeview.insert("", "end", values=(index, value))
            
            self.plot_area.plot(ciag_collatza, marker='o', linestyle='-')
            self.plot_area.set_title('Ciąg Collatza')
            self.plot_area.set_xlabel('Krok')
            self.plot_area.set_ylabel('Wartość')
            self.canvas.draw()
        
        except ValueError as e:
            messagebox.showerror("Błąd", str(e))
    
    def zamknij_aplikacje(self):
        self.root.destroy()

root = tk.Tk()
app = CollatzCalculator(root)
root.mainloop()
