import random
import time
import insertion_func, bubble_sort, merge_sort, quick_sort, heap_sort, bucketsort, radix_sort
import statistics
from PyQt5 import QtWidgets
from PyQt5 import QtCore,  uic
#from time import perf_counter 
from PyQt5.QtWidgets import  QApplication

#from application import Ui_MainWindow
import sys
#import matplotlib.pyplot as plt; plt.rcdefaults()
#import pyqtgraph as pg


class Main_Window(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        uic.loadUi("comparasion.ui", self)
        self.pushButton.clicked.connect(self.compare)
        
        self.checkBox.stateChanged.connect(self.insert)
        self.checkBox.stateChanged.connect(self.checkBoxChangedAction)
        
        self.checkBox_2.stateChanged.connect(self.bubble)
        
            
        self.checkBox_3.stateChanged.connect(self.merge)
        
            
        self.checkBox_4.stateChanged.connect(self.quick)
        
            
        self.checkBox_5.stateChanged.connect(self.heap)
        self.checkBox_6.stateChanged.connect(self.radix)

        self.checkBox_7.stateChanged.connect(self.bucket)

     
    def checkBoxChangedAction(self, state):
        if (QtCore.Qt.Checked != state):
           # self.label.setText("Selected.")
        #else:
            self.MplWidget.canvas.axes.clear()
            QApplication.processEvents()

            #self.label.setText("Not Selected.")
    
    def compare(self):
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.set_facecolor("#c6ccff")
        array = []
        amount1 = self.spinBox_3.text()
        amount = int(amount1)
        range1 = self.spinBox.text()
        ran = int(range1)
        num1 = self.spinBox_2.text()
        num_elements = int(num1)
        array1 = [] 
        array2 = []
        array3 = [] 
        array4 = [] 
        array5 = []
        array6 = []
        array7 = []

        
        for i in range(0,amount-1):
            array1.append(0)
            array2.append(0)
            array3.append(0)
            array4.append(0)
            array5.append(0)
            array6.append(0)
            array7.append(0)
            
    
        insert_time=[]
        bubble_time=[]
        merge_time=[]
        quick_time=[]
        radix_time=[]
        bucket_time=[]
        heap_time=[]
 
        
        for index in range(0,amount-1):
            for number in range(5,amount*5,5):
                for number in range(1,amount):
                    random.seed(0)
                    '''
                    for i in range(0,number):
                        i=random.randint(0,ran)
                        array+=[i]
                    '''
                    array = random.sample(range(1,int(ran)), int(num_elements))
                    QApplication.processEvents()
                    
                    start=time.perf_counter()
                    insertion_func.insertion_sort(array)
                    end=time.perf_counter()
                    insert_t=end-start
                    insert_time.append(insert_t)
                    QApplication.processEvents()
                    
                    start=time.perf_counter()
                    bubble_sort.bubble_sort(array)
                    end=time.perf_counter()
                    bubble_t=end-start
                    bubble_time.append(bubble_t)
                    QApplication.processEvents()
                    
                    start=time.perf_counter()
                    merge_sort.mergesort(array)
                    end=time.perf_counter()
                    merge_t=end-start
                    merge_time.append(merge_t)
                    QApplication.processEvents()
                    
                    start=time.perf_counter()
                    quick_sort.quickSort(array,0,len(array)-1)
                    end=time.perf_counter()
                    quick_t=end-start
                    quick_time.append(quick_t)
                    QApplication.processEvents()
                    
                    start=time.perf_counter()
                    radix_sort.radixsort(array)
                    end=time.perf_counter()
                    radix_t=end-start
                    radix_time.append(radix_t)
                    QApplication.processEvents()
                    
                    start=time.perf_counter()
                    bucketsort.bucket_sort(array)
                    end=time.perf_counter()
                    bucket_t=end-start
                    bucket_time.append(bucket_t)
                    QApplication.processEvents()
                    
                    start=time.perf_counter()
                    heap_sort.heapSort(array)
                    end=time.perf_counter()
                    heap_t=end-start
                    heap_time.append(heap_t)
                    QApplication.processEvents()
                        
                    
                    
                    insert_time_avg=statistics.mean(insert_time)
                    bubble_time_avg=statistics.mean(bubble_time)
                    merge_time_avg=statistics.mean(merge_time)
                    quick_time_avg=statistics.mean(quick_time)
                    radix_time_avg=statistics.mean(radix_time)
                    bucket_time_avg=statistics.mean(bucket_time)
                    heap_time_avg=statistics.mean(heap_time)

                    
                    
            array1[index]=insert_time_avg
            array2[index]=bubble_time_avg
            array3[index]=merge_time_avg
            array4[index]=quick_time_avg
            array5[index]=radix_time_avg
            array6[index]=bucket_time_avg
            array7[index]=heap_time_avg
  
        
        
        
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(array1)
        self.MplWidget.canvas.axes.plot(array2)
        self.MplWidget.canvas.axes.plot(array3)
        self.MplWidget.canvas.axes.plot(array4)
        self.MplWidget.canvas.axes.plot(array5)
        self.MplWidget.canvas.axes.plot(array6)
        self.MplWidget.canvas.axes.plot(array7)
        self.MplWidget.canvas.axes.legend(('Insertion', 'Bubble', 'Merge', 'Quick', 'Radix', 'Bucket', 'Heap'))
        self.MplWidget.canvas.axes.set_title('Time Comparison')
        self.MplWidget.canvas.axes.set_facecolor("#c6ccff")
        self.MplWidget.canvas.draw()
        QApplication.processEvents()
        
        
      
        
    
    
    
    
    def insert(self):
        self.MplWidget.canvas.axes.clear()
        if self.checkBox.isChecked():
            array = []
            amount1 = self.spinBox_3.text()
            amount = int(amount1)
            range1 = self.spinBox.text()
            ran = int(range1)
            num1 = self.spinBox_2.text()
            num_elements = int(num1)
            array1 = [] 
            
            
            
            for i in range(0,amount-1):
                array1.append(0)
                
                
                
            insert_time=[]
            
            for index in range(0,amount-1):
                for number in range(5,amount*5,5):
                    for number in range(1,amount):
                        random.seed(0)
                        
                        
                        array = random.sample(range(1,int(ran)), int(num_elements))
                        QApplication.processEvents()
                                
                        start=time.perf_counter()
                        insertion_func.insertion_sort(array)
                        end=time.perf_counter()
                        insert_t=end-start
                        insert_time.append(insert_t)
                        QApplication.processEvents()
                        
                        
                        
                        insert_time_avg=statistics.mean(insert_time)
                        
                       
                        
                array1[index]=insert_time_avg
                

            
            
            self.MplWidget.canvas.axes.plot(array1)
            

            self.MplWidget.canvas.axes.legend(('Insertion'))
            self.MplWidget.canvas.axes.set_title('Time Comparison')
            self.MplWidget.canvas.axes.set_facecolor("#c6ccff")
            self.MplWidget.canvas.draw()
            QApplication.processEvents()
        else:
            self.MplWidget.canvas.axes.clear()
    
        
    def bubble(self):
        if self.checkBox_2.isChecked():
                array = []
                amount1 = self.spinBox_3.text()
                amount = int(amount1)
                range1 = self.spinBox.text()
                ran = int(range1)
                num1 = self.spinBox_2.text()
                num_elements = int(num1)
                bubble_time=[]
                array2 = [] 
                
                
                
                for i in range(0,amount-1):
                    array2.append(0)
                
                
                for index in range(0,amount-1):
                    for number in range(5,amount*5,5):
                        for number in range(1,amount):
                            random.seed(0)
                            
                            
                            array = random.sample(range(1,int(ran)), int(num_elements))
                            QApplication.processEvents()
                                    
                            start=time.perf_counter()
                            bubble_sort.bubble_sort(array)
                            end=time.perf_counter()
                            bubble_t=end-start
                            bubble_time.append(bubble_t)
                            QApplication.processEvents()
                            
                            bubble_time_avg=statistics.mean(bubble_time)
                            
                    array2[index]=bubble_time_avg
                
                
                
                self.MplWidget.canvas.axes.plot(array2)
                self.MplWidget.canvas.axes.legend(('Bubble'))
                self.MplWidget.canvas.axes.set_title('Time Comparison')
                self.MplWidget.canvas.axes.set_facecolor("#c6ccff")
                self.MplWidget.canvas.draw()
                QApplication.processEvents()
                
        else:
                self.MplWidget.canvas.axes.clear()   
    
    
    
    
    
    
    
    
    def merge(self):
        if self.checkBox_3.isChecked():
            array = []
            amount1 = self.spinBox_3.text()
            amount = int(amount1)
            range1 = self.spinBox.text()
            ran = int(range1)
            num1 = self.spinBox_2.text()
            num_elements = int(num1)
            merge_time=[]
            array3 = [] 
            
            
            
            for i in range(0,amount-1):
                array3.append(0)
            
            
            for index in range(0,amount-1):
                for number in range(5,amount*5,5):
                    for number in range(1,amount):
                        random.seed(0)
                        
                        
                        array = random.sample(range(1,int(ran)), int(num_elements))
                        QApplication.processEvents()
                                
                        start=time.perf_counter()
                        merge_sort.mergesort(array)
                        end=time.perf_counter()
                        merge_t=end-start
                        merge_time.append(merge_t)
                        QApplication.processEvents()
                            
                        merge_time_avg=statistics.mean(merge_time)
                        
                array3[index]=merge_time_avg
            
            
            
            self.MplWidget.canvas.axes.plot(array3)
            self.MplWidget.canvas.axes.legend(('Merge'))
            self.MplWidget.canvas.axes.set_title('Time Comparison')
            self.MplWidget.canvas.axes.set_facecolor("#c6ccff")
            self.MplWidget.canvas.draw()
            QApplication.processEvents()
            
        else:
            self.MplWidget.canvas.axes.clear()    
            
            
            
    def quick(self):
        if self.checkBox_4.isChecked():
            array = []
            amount1 = self.spinBox_3.text()
            amount = int(amount1)
            range1 = self.spinBox.text()
            ran = int(range1)
            num1 = self.spinBox_2.text()
            num_elements = int(num1)
            quick_time=[]
            array4 = [] 
            
            
            
            for i in range(0,amount-1):
                array4.append(0)
            
            
            for index in range(0,amount-1):
                for number in range(5,amount*5,5):
                    for number in range(1,amount):
                        random.seed(0)
                        
                        
                        array = random.sample(range(1,int(ran)), int(num_elements))
                        QApplication.processEvents()
                                
                        start=time.perf_counter()
                        quick_sort.quickSort(array,0,len(array)-1)
                        end=time.perf_counter()
                        quick_t=end-start
                        quick_time.append(quick_t)
                        QApplication.processEvents()
                            
                        quick_time_avg=statistics.mean(quick_time)
                        
                array4[index]=quick_time_avg
            
            
            
            self.MplWidget.canvas.axes.plot(array4)
            self.MplWidget.canvas.axes.legend(('Quick'))
            self.MplWidget.canvas.axes.set_title('Time Comparison')
            self.MplWidget.canvas.axes.set_facecolor("#c6ccff")
            self.MplWidget.canvas.draw()
            QApplication.processEvents()
            
        else:
            self.MplWidget.canvas.axes.clear()    
            
            
    def heap(self):
        if self.checkBox_5.isChecked():
            array = []
            amount1 = self.spinBox_3.text()
            amount = int(amount1)
            range1 = self.spinBox.text()
            ran = int(range1)
            num1 = self.spinBox_2.text()
            num_elements = int(num1)
            heap_time=[]
            array5 = [] 
            
            
            
            for i in range(0,amount-1):
                array5.append(0)
            
            
            for index in range(0,amount-1):
                for number in range(5,amount*5,5):
                    for number in range(1,amount):
                        random.seed(0)
                        
                        
                        array = random.sample(range(1,int(ran)), int(num_elements))
                        QApplication.processEvents()
                                
                        start=time.perf_counter()
                        heap_sort.heapSort(array)
                        end=time.perf_counter()
                        heap_t=end-start
                        heap_time.append(heap_t)
                        QApplication.processEvents()
                            
                        heap_time_avg=statistics.mean(heap_time)
                        
                array5[index]=heap_time_avg
            
            
            
            self.MplWidget.canvas.axes.plot(array5)
            self.MplWidget.canvas.axes.legend(('Heap'))
            self.MplWidget.canvas.axes.set_title('Time Comparison')
            self.MplWidget.canvas.axes.set_facecolor("#c6ccff")
            self.MplWidget.canvas.draw()
            QApplication.processEvents()        
            
            
        else:
            self.MplWidget.canvas.axes.clear()
    
    
    def radix(self):
        if self.checkBox_6.isChecked():
            array = []
            amount1 = self.spinBox_3.text()
            amount = int(amount1)
            range1 = self.spinBox.text()
            ran = int(range1)
            num1 = self.spinBox_2.text()
            num_elements = int(num1)
            radix_time=[]
            array6 = [] 
            
            
            
            for i in range(0,amount-1):
                array6.append(0)
            
            
            for index in range(0,amount-1):
                for number in range(5,amount*5,5):
                    for number in range(1,amount):
                        random.seed(0)
                        
                        
                        array = random.sample(range(1,int(ran)), int(num_elements))
                        QApplication.processEvents()
                                
                        start=time.perf_counter()
                        radix_sort.radixsort(array)
                        end=time.perf_counter()
                        radix_t=end-start
                        radix_time.append(radix_t)
                        QApplication.processEvents()
                            
                        radix_time_avg=statistics.mean(radix_time)
                        
                array6[index]=radix_time_avg
            
            
            
            self.MplWidget.canvas.axes.plot(array6)
            self.MplWidget.canvas.axes.legend(('Radix'))
            self.MplWidget.canvas.axes.set_title('Time Comparison')
            self.MplWidget.canvas.axes.set_facecolor("#c6ccff")
            self.MplWidget.canvas.draw()
            QApplication.processEvents()
            
        else:
            self.MplWidget.canvas.axes.clear()   
    
    
    def bucket(self):
        if self.checkBox_7.isChecked():
            array = []
            amount1 = self.spinBox_3.text()
            amount = int(amount1)
            range1 = self.spinBox.text()
            ran = int(range1)
            num1 = self.spinBox_2.text()
            num_elements = int(num1)
            bucket_time=[]
            array7 = [] 
            
            
            
            for i in range(0,amount-1):
                array7.append(0)
            
            
            for index in range(0,amount-1):
                for number in range(5,amount*5,5):
                    for number in range(1,amount):
                        random.seed(0)
                        
                        
                        array = random.sample(range(1,int(ran)), int(num_elements))
                        QApplication.processEvents()
                                
                        start=time.perf_counter()
                        bucketsort.bucket_sort(array)
                        end=time.perf_counter()
                        bucket_t=end-start
                        bucket_time.append(bucket_t)
                        QApplication.processEvents()
                            
                        bucket_time_avg=statistics.mean(bucket_time)
                array7[index]=bucket_time_avg
      
            
            
            
            self.MplWidget.canvas.axes.plot(array7)
            self.MplWidget.canvas.axes.legend(('Radix'))
            self.MplWidget.canvas.axes.set_title('Time Comparison')
            self.MplWidget.canvas.axes.set_facecolor("#c6ccff")
            self.MplWidget.canvas.draw()
            QApplication.processEvents()
            
        else:
            self.MplWidget.canvas.axes.clear()   
    
    
    
    
    
    
def main():
    app = QtWidgets.QApplication(sys.argv)
    main = Main_Window()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()       
    
    
    
    
    
    
    