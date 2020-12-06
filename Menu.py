
from PyQt5 import QtWidgets
from PyQt5 import  uic

from PyQt5.QtWidgets import QWidget


import sys

import comparision
import my_app
import search
import webbrowser












class Main_Window_2(QtWidgets.QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #Load UI PAGE
        self.main_window=uic.loadUi("Menu.ui", self)
        self.sorting_widget = my_app.MainWindow()
        self.compare_widget = comparision.Main_Window()
        self.binary_widget = search.MainWindow()

        
        change_widget=QWidget()
        self.stackedWidget.addWidget(change_widget)
        self.stackedWidget.addWidget(self.sorting_widget)
        self.stackedWidget.addWidget(self.compare_widget)
        self.stackedWidget.addWidget(self.binary_widget)

        self.pushButton.clicked.connect(self.connection_sorting_widget)
        self.pushButton_2.clicked.connect(self.connection_comparison_widget)
        self.pushButton_3.clicked.connect(self.back_to_mainmenu)
        self.pushButton_4.clicked.connect(self.connection_binary_widget)
        self.pushButton_5.clicked.connect(self.university_web)
        self.pushButton_6.clicked.connect(self.exit)

        
        
        self.main_window.show()
    






    
    def connection_sorting_widget(self):
        self.stackedWidget.setCurrentIndex(3)
            
    def connection_comparison_widget(self):
        self.stackedWidget.setCurrentIndex(2)
        
    def connection_binary_widget(self):
        self.stackedWidget.setCurrentIndex(4)                                
    
    def back_to_mainmenu(self):
        self.stackedWidget.setCurrentIndex(0)

    def university_web(self):
        webbrowser.open_new("https://www.ikcu.edu.tr/")

    def exit(self):
        import sys
        sys.exit()
        










































def main():
    app = QtWidgets.QApplication(sys.argv)
    main = Main_Window_2()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()       
        












