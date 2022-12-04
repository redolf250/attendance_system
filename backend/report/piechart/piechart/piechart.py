
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Canvas(FigureCanvas):
    def __init__(self):
        self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(5, 5),
        sharey = True, facecolor='white')
        super().__init__(self.fig)

        total = [20, 30, 46, 10, 15, 50]
        explode = [0.1, 0.0, 0.0, 0.0, 0.0, 0.0]
        names = ['Redolf', 'Greenolf', 'Blueolf', 'Magentaolf', 'Yellowolf', 'Cyanolf']
        plt.title('Piechart', size= 9, family = 'Arial' )
        
        self.ax.pie(total, labels=names, autopct = '%1.1f',shadow = True, labeldistance = 1.1
        , radius=0.8, startangle = 90, pctdistance = 0.6, explode = explode)
        self.ax.axis('equal')
        plt.savefig(r'D:\\Commons\\backend\\report\\piechart\\piechart\\pie.png',dpi = 300)

    

