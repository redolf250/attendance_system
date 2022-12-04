import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Barchart(FigureCanvas):
    def __init__(self):
        self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(8, 8),
        sharey = True, facecolor='white')
        super().__init__(self.fig)
        width = 0.2

        students = ['CSE', 'ISE', 'MECH', 'EEE', 'ESC', 'BCH']
        boys = [20, 30, 46, 10, 15, 40]
        girls = [10, 40, 46, 20, 30, 50]
        some = [5, 19, 30, 10, 35, 55]
        bar_1 = np.arange(len(students))
        bar_2 = [i+width for i in bar_1]
        bar_3 = [i+width for i in bar_2]
       
        self.ax.bar(bar_1, boys, width, label = "boys")   
        self.ax.bar(bar_2, girls, width, label = "girls") 
        self.ax.bar(bar_3, some, width, label = "some") 

        self.fig.suptitle("Barchart", fontsize=10)
        plt.xlabel("Courses")
        plt.ylabel("Students")
        plt.xticks(bar_1+width/3, students)
        plt.legend(labelcolor = 'white')
        plt.savefig(r'D:\\Commons\\backend\\report\\piechart\\barchart\\bar.png',dpi = 300)

    