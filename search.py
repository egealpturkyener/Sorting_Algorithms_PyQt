from PyQt5 import  QtWidgets, uic
import sys
import binary_search
import random
import Fibonacci


  
class MainWindow(QtWidgets.QMainWindow):
    array="global"
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        #Load the UI Page
        uic.loadUi('fibonacci.ui', self)
        
        self.pushButton.clicked.connect(self.create_array_and_sort)  
        self.pushButton_2.clicked.connect(self.binary_search)
        self.pushButton_3.clicked.connect(self.Fibonacci)
    def create_array_and_sort(self):
        global array
        range_num = int(self.spinBox.value())#getting range from user
        num_elements = int(self.spinBox_2.value())#getting number of elements from user
        if num_elements > range_num:
            self.textEdit.setText("Invalid input")
            self.textEdit_2.setText("Invalid input") 
        else:
            self.array = random.sample(range(1,int(range_num)), int(num_elements))#creating random arrayreating random array         
            str2 = " ".join(str(e) for e in self.array) #make array string
            self.textEdit_4.clear()
            self.textEdit.setText(str2) #display the unsortedarray
            self.array.sort() # sort array    
            str2 = " ".join(str(e) for e in self.array) #make array string
            self.textEdit_3.setText(str2) #display the unsortedarray
            
    def binary_search(self):
        global array
        searched_number = int(self.spinBox_3.value())

        answer = binary_search.binary_search(self.array,int(searched_number))
        answer = answer + 1
        
        self.textEdit_4.setText(str(answer)) #display the unsortedarray
        
    # Function for nth Fibonacci number 
  
    def Fibonacci(self):
        fibonacci_input = int(self.spinBox_3.value())
        answer = Fibonacci.Fibonacci(int(fibonacci_input))
        self.textEdit.clear()
        self.textEdit_3.clear()
        self.textEdit_4.clear()
        self.spinBox.clear()
        self.spinBox_2.clear()

        self.textEdit_4.setText(str(answer)) #display the unsortedarray
        
    
    
def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':     
    main()