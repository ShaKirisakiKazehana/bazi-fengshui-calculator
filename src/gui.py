import tkinter as tk
from bazi_calculator import generate_bazi_chart
from fortune_advisor import get_daily_advice

class FengShuiApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bazi Feng Shui Calculator")

        self.label = tk.Label(self.root, text="Enter Birth Date (YYYY-MM-DD):")
        self.label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.button = tk.Button(self.root, text="Calculate", command=self.calculate)
        self.button.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def calculate(self):
        birth_date = self.entry.get()
        bazi_chart = generate_bazi_chart(birth_date)
        advice = get_daily_advice(bazi_chart)
        self.result_label.config(text=f"Bazi: {bazi_chart}\nAdvice: {advice}")

    def run(self):
        self.root.mainloop()
