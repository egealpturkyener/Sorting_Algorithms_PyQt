import random
import numpy as np
import time
from PyQt5 import  QtWidgets, uic

from matplotlib.backends.backend_qt5agg import FigureCanvas
from PyQt5 import QtCore
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtWidgets import QVBoxLayout
import sys

#import matplotlib.animation as animation
#from IPython.display import HTML

class MplWidget(QWidget):
    
    def __init__(self, parent = None):

        QWidget.__init__(self, parent)
        
        self.canvas = FigureCanvas(Figure())
        
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)


class MainWindow(QtWidgets.QMainWindow):
    array="global"
    stop_variable = "global" 

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        #Load the UI Page
        uic.loadUi('mainwindow.ui', self)
        self.MplWidget.canvas.axes.get_xaxis().set_visible(False)
        self.MplWidget.canvas.axes.get_yaxis().set_visible(False)
        self.pushButton.clicked.connect(self.create_array) 
        self.pushButton_2.clicked.connect(self.insertion_sort) 
        self.pushButton_3.clicked.connect(self.bubble_sort) 
        self.pushButton_4.clicked.connect(self.merge_sort) 
        self.pushButton_5.clicked.connect(self.heap_sort) 
        self.pushButton_6.clicked.connect(self.quick_sort) 
        self.pushButton_8.clicked.connect(self.counting_sort)
        self.pushButton_12.clicked.connect(self.Finish)


        self.pushButton_7.clicked.connect(self.bucketSort) 
        self.pushButton_9.clicked.connect(self.radixSort) 
        self.pushButton_10.clicked.connect(self.start_stop)
        self.pushButton_11.clicked.connect(self.Contbutton)

    def start_stop(self):
        global stop_variable
        self.stop_variable = int(1)
            
    def Finish(self):
        global array
        global stop_variable
        self.MplWidget.canvas.axes.clear()
        self.stop_variable = int(2)
        
        if self.stop_variable == 2:
            finished_array = self.array
            finished_array.sort()
            
            self.MplWidget.canvas.axes.bar(np.linspace(1,len(finished_array),len(finished_array)),finished_array,color=['yellow'])
            for m, v in enumerate(finished_array):
                    self.MplWidget.canvas.axes.text(m+.70, v+1, " "+str(v), color='black', va='center', fontweight='bold')
            self.MplWidget.canvas.axes.set_title('Sorting Visualization')
            self.MplWidget.canvas.draw()
            str2 = " ".join(str(e) for e in finished_array) #make array string
            self.textEdit_2.setText(str2) #display the unsortedarray
            
            
            
            
    def Contbutton(self):
        global stop_variable
        self.stop_variable = int(0)
            
    def create_array(self):
        global array
        global stop_variable
        range_num = int(self.spinBox.value())#getting range from user
        num_elements = int(self.spinBox_2.value())#getting number of elements from user
        if num_elements > range_num:
            self.textEdit.setText("Invalid input")
            self.textEdit_2.setText("Invalid input")

        else:
            self.array = random.sample(range(1,int(range_num)), int(num_elements))#creating random arrayreating random array         
           
            str2 = " ".join(str(e) for e in self.array) #make array string
            self.textEdit.setText(str2) #display the unsortedarray
            self.textEdit_2.clear()
            
            self.MplWidget.canvas.axes.clear()
            for m, v in enumerate(self.array):
                    self.MplWidget.canvas.axes.text(m+.70, v+1, " "+str(v), color='black', va='center', fontweight='bold')
            self.MplWidget.canvas.axes.bar(np.linspace(1,len(self.array),len(self.array)),self.array,color=['yellow'])
            #self.MplWidget.canvas.axes.legend(('cosinus', 'sinus'),loc='upper right')
            self.MplWidget.canvas.axes.set_title('Sorting Visualization')
            self.MplWidget.canvas.draw()
            self.stop_variable = 0
    def insertion_sort(self):#We define our function with 2 variables
        global array
        global stop_variable

        array_current = self.array
        for j in range(1,len(array_current)):#Starting from 2nd element of the array goes through the last one
         
            
            key=array_current[j]#Saving the current element to temporary variable
            i=j-1#Setting i as j-1
            while i>=0 and array_current[i]>key:#If the ith element is greater than the temporary key element they change places
                array_current[i+1]=array_current[i]#Assigning the ith element to i+1=j th element 
                i=i-1
                 ######FOR STOP ####
                while self.stop_variable == 1: 
                        if self.stop_variable == 0:
                               if self.stop_variable == 2:
                                   self.MplWidget.canvas.axes.clear()
                                   break
                               break
                        time.sleep(0.8)
                        QtCore.QCoreApplication.processEvents()
                if self.stop_variable == 2:
                                   self.MplWidget.canvas.axes.clear()
                                   break
          ######FOR STOP ####
          
                array_current[i+1]=key 
                self.MplWidget.canvas.axes.get_xaxis().set_visible(False)
                self.MplWidget.canvas.axes.get_yaxis().set_visible(False)
                self.MplWidget.canvas.axes.clear()
                for m, v in enumerate(array_current):
                    self.MplWidget.canvas.axes.text(m+.70, v+1, " "+str(v), color='black', va='center', fontweight='bold')
                self.MplWidget.canvas.axes.bar(np.linspace(1,len(array_current),len(array_current)),array_current,color=['yellow'])
                self.MplWidget.canvas.axes.bar(i+2,array_current[i+2],color='black')
                self.MplWidget.canvas.axes.set_title('Sorting Visualization')
                self.MplWidget.canvas.draw()
                speed_value = self.horizontalSlider.value()
                speed = (100-speed_value)/150
                time.sleep(speed)
                QApplication.processEvents()
            
                
                
                
            
               #Assigning the ith element to i+1=j th element which is the one it is temporary
            
            self.MplWidget.canvas.axes.get_xaxis().set_visible(False) #make axis invisible
            self.MplWidget.canvas.axes.get_yaxis().set_visible(False) #make axis invisible
            self.MplWidget.canvas.axes.clear()
            for m, v in enumerate(array_current):
                    self.MplWidget.canvas.axes.text(m+.70, v+1, " "+str(v), color='black', va='center', fontweight='bold')
            self.MplWidget.canvas.axes.bar(np.linspace(1,len(array_current),len(array_current)),array_current,color=['yellow'])
            self.MplWidget.canvas.axes.bar(i+1,array_current[i+1],color='black')
            self.MplWidget.canvas.axes.set_title('Sorting Visualization')
            self.MplWidget.canvas.draw()
            speed_value = self.horizontalSlider.value()
            speed = (100-speed_value)/150
            time.sleep(speed)
            QApplication.processEvents()
            
        Sorted_Array = array_current
            
         #We are using this block to print the array inside an textbox :  
        str2 = " ".join(str(e) for e in Sorted_Array) #make array string
        self.textEdit_2.setText(str2) #display the unsortedarray
        
    def bubble_sort(self):
        global array
        size = len(self.array)
        for i in range(0,size-2):#Staring from first element of the array to the last ekement of the array
            for j in range(size-1,i,-1):#Starting from the last element of the array to ith element of the array
               
                if self.array[j]<self.array[j-1]: #Checking the jth element is less than the j-1 th element
                    ######FOR STOP ####
                    while self.stop_variable == 1: 
                               if self.stop_variable == 0:
                                       if self.stop_variable == 2:
                                           self.MplWidget.canvas.axes.clear()
                                           break
                                       break
                               time.sleep(0.8)
                               QtCore.QCoreApplication.processEvents()
                    if self.stop_variable == 2:
                                           self.MplWidget.canvas.axes.clear()
                                           break
                    ######FOR STOP ####
                    
                    key=self.array[j]#Assigning a temporary key variable and saving the th element in it
                    self.array[j]=self.array[j-1] #Changing the jth element with j-1 th element
                    self.array[j-1]=key #Assigning the temporary key to j-1 th element
                    self.MplWidget.canvas.axes.get_xaxis().set_visible(False) #make axis invisible
                    self.MplWidget.canvas.axes.get_yaxis().set_visible(False) #make axis invisible
                    self.MplWidget.canvas.axes.clear()
                    for i, v in enumerate(self.array):
                        self.MplWidget.canvas.axes.text(i+.70, v+1, " "+str(v), color='black', va='center', fontweight='bold')
                    self.MplWidget.canvas.axes.bar(np.linspace(1,len(self.array),len(self.array)),self.array,color = 'yellow')
                    self.MplWidget.canvas.axes.bar(j,self.array[j-1],color='black')
                    #self.MplWidget.canvas.axes.bar(j-2,self.array[j-2],color='black')

                    self.MplWidget.canvas.axes.set_title('Sorting Visualization')
                    self.MplWidget.canvas.draw()
                    speed_value = self.horizontalSlider.value()
                    speed = (100-speed_value)/150
                    time.sleep(speed)
                    QApplication.processEvents()
        
        str2 = " ".join(str(e) for e in self.array) #make array string
        self.textEdit_2.setText(str2) #display the unsortedarray
        
    def merge_sort(self):
        global array
        self.mergesort(self.array,0,len(self.array)-1)#Divding array to two parts
        
        
    def mergesort(self, A, p, r):
        if p<r:#first element of the array must be smaller than the last element of to array to continue
            q=(r+p)//2#Assignning a variable as equal to half of the array. We rolled down with using //
            self.mergesort(A,p,q)# Sending the first part of the array back inside this dunction to divide it again
            self.mergesort(A,q+1,r)# Sending the second part of the array back inside this dunction to divide it again
            self.merge(A,p,q,r)# Sending our divided arrays to our third and final function. 
        
        
    def merge(self, A, first_input, mid_input, last_input):
        L=A[first_input:mid_input+1]#Assigning the left side of the array 
        R=A[mid_input+1:last_input+1]#Assigning the rigth side of the array 
        L.append(999999999) # Adding an number as a sentinal value
        R.append(999999999)# Adding an number as a sentinal value
        i=0
        j=0
        for k in range(first_input,last_input+1):# Goes through the firs element to last element
            if L[i]<=R[j]:# If left array's ith number is less than right array's jth number 
                A[k]=L[i]#It sets k'th element of the main array equal to left array's i'th number
                i=i+1# Increasing the i by one
                        ######FOR STOP ####
                while self.stop_variable == 1: 
                           if self.stop_variable == 0:
                                   if self.stop_variable == 2:
                                       self.MplWidget.canvas.axes.clear()
                                       break
                                   break
                           time.sleep(0.8)
                           QtCore.QCoreApplication.processEvents()
                if self.stop_variable == 2:
                                       self.MplWidget.canvas.axes.clear()
                                       break
              ######FOR STOP ####
          
                speed_value = self.horizontalSlider.value()
                speed = (100-speed_value)/150
                time.sleep(speed)
               
                self.MplWidget.canvas.axes.get_xaxis().set_visible(False) #make axis invisible
                self.MplWidget.canvas.axes.get_yaxis().set_visible(False) #make axis invisible     
                self.MplWidget.canvas.axes.clear()
                for m, v in enumerate(self.array):
                        self.MplWidget.canvas.axes.text(m+.70, v+1, " "+str(v), color='black', va='center', fontweight='bold')
                self.MplWidget.canvas.axes.bar(np.linspace(1,len(A),len(A)),A,color = 'yellow')
                self.MplWidget.canvas.axes.bar(k+1,self.array[k],color='black')
                self.MplWidget.canvas.axes.set_title('Sorting Visualization')
                self.MplWidget.canvas.draw()
                speed_value = self.horizontalSlider.value()
                speed = (100-speed_value)/150
                time.sleep(speed)
                QApplication.processEvents()
            else:
                A[k]=R[j]#Sets k'th number to j'th number of the  rigth array 
                j=j+1# Increasing the i by one
                
                speed_value = self.horizontalSlider.value()
                speed = (100-speed_value)/150
                time.sleep(speed)
                self.MplWidget.canvas.axes.get_xaxis().set_visible(False) #make axis invisible
                self.MplWidget.canvas.axes.get_yaxis().set_visible(False) #make axis invisible    
                
                self.MplWidget.canvas.axes.clear()
                for m, v in enumerate(self.array):
                        self.MplWidget.canvas.axes.text(m+.70, v+1, " "+str(v), color='black', va='center', fontweight='bold')
                self.MplWidget.canvas.axes.bar(np.linspace(1,len(A),len(A)),A,color = 'yellow')
                self.MplWidget.canvas.axes.bar(k+1,self.array[k],color='black')

                #self.MplWidget.canvas.axes.legend(('cosinus', 'sinus'),loc='upper right')
                self.MplWidget.canvas.axes.set_title('Sorting Visualization')
                self.MplWidget.canvas.draw()
                speed_value = self.horizontalSlider.value()
                speed = (100-speed_value)/150
                time.sleep(speed)
                QApplication.processEvents()
            str2 = " ".join(str(e) for e in self.array) #make array string
            self.textEdit_2.setText(str2) #display the unsortedarray
      
    def partition(self,arr,low,high): 
       
        
        i = ( low-1 )         # index of smaller element 
        pivot = arr[high]     # pivot 
      
        for j in range(low , high): 
            speed_value = self.horizontalSlider.value()
            speed = (100-speed_value)/150
            time.sleep(speed)
            # If current element is smaller than or 
            # equal to pivot 
            if   arr[j] <= pivot: 
              
                # increment index of smaller element 
                i = i+1 
                arr[i],arr[j] = arr[j],arr[i] 
                        ######FOR STOP ####
                while self.stop_variable == 1: 
                           if self.stop_variable == 0:
                                   if self.stop_variable == 2:
                                       self.MplWidget.canvas.axes.clear()
                                       break
                                   break
                           time.sleep(0.8)
                           QtCore.QCoreApplication.processEvents()
                if self.stop_variable == 2:
                                       self.MplWidget.canvas.axes.clear()
                                       break
              ######FOR STOP ####
          ######FOR STOP ####
                while self.stop_variable == 1: 
                        if self.stop_variable == 0:
                               if self.stop_variable == 2:
                                   self.MplWidget.canvas.axes.clear()
                                   break
                               break
                        time.sleep(0.8)
                        QtCore.QCoreApplication.processEvents()
                if self.stop_variable == 2:
                                   self.MplWidget.canvas.axes.clear()
                                   break
          ######FOR STOP ####
                self.MplWidget.canvas.axes.get_xaxis().set_visible(False) #make axis invisible
                self.MplWidget.canvas.axes.get_yaxis().set_visible(False) #make axis invisible
                self.MplWidget.canvas.axes.clear()
                for m, v in enumerate(arr):
                        self.MplWidget.canvas.axes.text(m+.70, v+1, " "+str(v), color='black', va='center', fontweight='bold')
                self.MplWidget.canvas.axes.bar(np.linspace(1,len(arr),len(arr)),arr,color = 'yellow')
                self.MplWidget.canvas.axes.bar(j+1,arr[j],color='black')
                self.MplWidget.canvas.axes.set_title('Sorting Visualization')
                self.MplWidget.canvas.draw()
                speed_value = self.horizontalSlider.value()
                speed = (100-speed_value)/150
                time.sleep(speed)
                QApplication.processEvents()
                
                
            ######FOR STOP ####
                while self.stop_variable == 1: 
                        if self.stop_variable == 0:
                               if self.stop_variable == 2:
                                   self.MplWidget.canvas.axes.clear()
                                   break
                               break
                        time.sleep(0.8)
                        QtCore.QCoreApplication.processEvents()
       
                if self.stop_variable == 2:
                                   self.MplWidget.canvas.axes.clear()
                                   break
          ######FOR STOP ####    
        arr[i+1],arr[high] = arr[high],arr[i+1] 
        self.MplWidget.canvas.axes.get_xaxis().set_visible(False) #make axis invisible
        self.MplWidget.canvas.axes.get_yaxis().set_visible(False) #make axis invisible
        self.MplWidget.canvas.axes.clear()
        for m, v in enumerate(arr):
                self.MplWidget.canvas.axes.text(m+.70, v+1, " "+str(v), color='black', va='center', fontweight='bold')
        self.MplWidget.canvas.axes.bar(np.linspace(1,len(arr),len(arr)),arr,color = 'yellow')
        self.MplWidget.canvas.axes.bar(j+1,arr[j],color='black')
        self.MplWidget.canvas.axes.set_title('Sorting Visualization')
        self.MplWidget.canvas.draw()
        speed_value = self.horizontalSlider.value()
        speed = (100-speed_value)/150
        time.sleep(speed)
        QApplication.processEvents()
       
        
        return ( i+1 ) 
  
    def quick_sort(self):
        global array
        low = 0
        high = len(self.array)-1
        self.quickSort(self.array,low,high)
# Function to do Quick sort 
    def quickSort(self,arr,low,high): 
        if low < high: 
      
            # pi is partitioning index, arr[p] is now 
            # at right place 
            pi = self.partition(arr,low,high) 
      
            # Separately sort elements before 
            # partition and after partition 
            self.quickSort(arr, low, pi-1) 
            self.quickSort(arr, pi+1, high) 
            str2 = " ".join(str(e) for e in arr) #make array string
            self.textEdit_2.setText(str2) #display the unsortedarray
#####################################################################################
    def heap_sort(self):
        global array
        self.heapSort(self.array)
      
    def heapify(self,arr, n, i): 
        pivot = i     # Initialize largest as pivot
        l = 2 * i + 1     # left = 2*i + 1 
        r = 2 * i + 2     # right = 2*i + 2 
          
        # See if left side of root exists and is 
        # greater than pivot 
        if l < n and arr[i] < arr[l]: 
            pivot = l 
          
        # See if right child of pivot exists and is 
        # greater than root 
        if r < n and arr[pivot] < arr[r]: 
            pivot = r 
          
        # Change root, if needed 
        if pivot != i: 
            arr[i],arr[pivot] = arr[pivot],arr[i]  # swap 
              ######FOR STOP ####
            while self.stop_variable == 1: 
                       if self.stop_variable == 0:
                               if self.stop_variable == 2:
                                   self.MplWidget.canvas.axes.clear()
                                   break
                               break
                       time.sleep(0.8)
                       QtCore.QCoreApplication.processEvents()
            if self.stop_variable == 2:
                                   self.MplWidget.canvas.axes.clear()
                                 
          ######FOR STOP ####
          
            # Heapify the root. 
            self.heapify(arr, n, pivot)
            self.MplWidget.canvas.axes.get_xaxis().set_visible(False) #make axis invisible
            self.MplWidget.canvas.axes.get_yaxis().set_visible(False) #make axis invisible       
            self.MplWidget.canvas.axes.clear()
            for m, v in enumerate(arr):
                self.MplWidget.canvas.axes.text(m+.70, v+1, " "+str(v), color='black', va='center', fontweight='bold')
            self.MplWidget.canvas.axes.bar(np.linspace(1,len(arr),len(arr)),arr, color = 'yellow')
            self.MplWidget.canvas.axes.bar(i+2,arr[i+1],color='black')
            self.MplWidget.canvas.axes.set_title('Sorting Visualization')
            self.MplWidget.canvas.draw()
            speed_value = self.horizontalSlider.value()
            speed = (100-speed_value)/150
            time.sleep(speed)
            QApplication.processEvents()
            
    def heapSort(self,arr): 
        n = len(arr) 
          
        # Build a maxheap. 
        for i in range(n, -1, -1): 
            self.heapify(arr, n, i) 
          
        # One by one extract elements 
        for i in range(n-1, 0, -1): 
            arr[i], arr[0] = arr[0], arr[i]   # swap 
            self.heapify(arr, i, 0) 
        str2 = " ".join(str(e) for e in self.array) #make array string
      ######FOR STOP ####
        while self.stop_variable == 1: 
                   if self.stop_variable == 0:
                           if self.stop_variable == 2:
                               self.MplWidget.canvas.axes.clear()
                               break
                           break
                   time.sleep(0.8)
                   QtCore.QCoreApplication.processEvents()
        if self.stop_variable == 2:
                               self.MplWidget.canvas.axes.clear()
      ######FOR STOP ####
        
      
        self.textEdit_2.setText(str2) #display the unsortedarray
        self.MplWidget.canvas.axes.get_xaxis().set_visible(False) #make axis invisible
        self.MplWidget.canvas.axes.get_yaxis().set_visible(False) #make axis invisible
        self.MplWidget.canvas.axes.clear()
        for m, v in enumerate(self.array):
                        self.MplWidget.canvas.axes.text(m+.70, v+1, " "+str(v), color='black', va='center', fontweight='bold')
        self.MplWidget.canvas.axes.bar(np.linspace(1,len(arr),len(arr)),arr,color = 'yellow')
        self.MplWidget.canvas.axes.bar(i+2,arr[i+1],color='black')
        self.MplWidget.canvas.axes.set_title('Sorting Visualization')
        self.MplWidget.canvas.draw()
        speed_value = self.horizontalSlider.value()
        speed = (100-speed_value)/150
        time.sleep(speed)
        QApplication.processEvents()
    ##########################################33        
    def bucketSort(self):
        global array
        self.bucket_sort(self.array)
        
    def bucket_sort(self,array,bucketSize = 100):
              import math
              if len(array) == 0: #if length of array 0 return array
                return array
            
              # Determine minimum and maximum values of the array 
              min_val = array[0]
              max_val = array[0]
              for i in range(1, len(array)):
                if array[i] < max_val:
                  min_val = array[i]
                elif array[i] > max_val:
                  max_val = array[i]
            
              # Initialize buckets
              bucketCount = math.floor((max_val - min_val) / bucketSize) + 1
              buckets = []
              for i in range(0, bucketCount):
                buckets.append([])
            
              # Distribute input array values into buckets
              for i in range(0, len(array)):
                buckets[math.floor((array[i] - min_val) / bucketSize)].append(array[i])
            
              # Sort buckets and place back into input array
              array = []
              for i in range(0, len(buckets)):
                self.insertion_sort2(buckets[i])
                for j in range(0, len(buckets[i])):
                  array.append(buckets[i][j])
                  
              return array
              
    def insertion_sort2(self,A):#We define our function with 2 variables
        
        for j in range(1, len(A)): #for the numbers from 1 to len(A)

                key = A[j] #save A[j] element to a temporary constant.
            
            
                i = j - 1
            
                # move the elements of array A if
                # it is greater than key.
            
                while i >= 0 and key < A[i]:
                    A[i + 1] = A[i]
                    i -= 1
                A[i + 1] = key
        ######FOR STOP ####
                while self.stop_variable == 1: 
                           if self.stop_variable == 0:
                                   if self.stop_variable == 2:
                                       self.MplWidget.canvas.axes.clear()
                                       break
                                   break
                           time.sleep(0.8)
                           QtCore.QCoreApplication.processEvents()
                if self.stop_variable == 2:
                                       self.MplWidget.canvas.axes.clear()
                                       break
              ######FOR STOP ####
          
                self.MplWidget.canvas.axes.get_xaxis().set_visible(False) #make axis invisible
                self.MplWidget.canvas.axes.get_yaxis().set_visible(False) #make axis invisible
                
                self.MplWidget.canvas.axes.clear()
                for m, v in enumerate(A):
                        self.MplWidget.canvas.axes.text(m+.70, v+1, " "+str(v), color='black', va='center', fontweight='bold')
                self.MplWidget.canvas.axes.bar(np.linspace(1,len(A),len(A)),A,color = 'yellow')
                self.MplWidget.canvas.axes.bar(j+1,A[j],color='black')
                self.MplWidget.canvas.axes.set_title('Sorting Visualization')
                self.MplWidget.canvas.draw()
                speed_value = self.horizontalSlider.value()
                speed = (100-speed_value)/150
                time.sleep(speed)
                QApplication.processEvents()
        str2 = " ".join(str(e) for e in A) #make array string
        self.textEdit_2.setText(str2) #display the unsortedarray
        
            ##########################################33        

    
    def countingSort(self,array, place):
        size = len(array)
        output = [0] * size
        count = [0] * 10
        
        self.MplWidget.canvas.axes.get_xaxis().set_visible(False)
        self.MplWidget.canvas.axes.get_yaxis().set_visible(False)
        self.MplWidget.canvas.axes.clear()
        for m, v in enumerate(self.array):
                       self.MplWidget.canvas.axes.text(m+.70, v+1, " "+str(v), color='black', va='center', fontweight='bold')
        self.MplWidget.canvas.axes.bar(np.linspace(1,len(self.array),len(self.array)),self.array,color=['yellow'])
        #self.MplWidget.canvas.axes.legend(('cosinus', 'sinus'),loc='upper right')
        self.MplWidget.canvas.axes.set_title('Sorting Visualization')
        self.MplWidget.canvas.draw()
        speed_value = self.horizontalSlider.value()
        speed = (100-speed_value)/150
        time.sleep(speed)
        QApplication.processEvents()
        #We are using this block to print the array inside an textbox :  
        str2 = " ".join(str(e) for e in self.array) #make array string
        self.textEdit_2.setText(str2) #display the unsortedarray
        ##### 
        for i in range(0, size):
            index = array[i] // place
            count[index % 10] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        i = size - 1
        while i >= 0:
            index = array[i] // place
            output[count[index % 10] - 1] = array[i]
            count[index % 10] -= 1
            i -= 1
            
            self.MplWidget.canvas.axes.get_xaxis().set_visible(False)
            self.MplWidget.canvas.axes.get_yaxis().set_visible(False)
            self.MplWidget.canvas.axes.clear()
            for m, v in enumerate(self.array):
                        self.MplWidget.canvas.axes.text(m+.70, v+1, " "+str(v), color='black', va='center', fontweight='bold')
            self.MplWidget.canvas.axes.bar(np.linspace(1,len(self.array),len(self.array)),self.array,color=['yellow'])
            #self.MplWidget.canvas.axes.legend(('cosinus', 'sinus'),loc='upper right')
            self.MplWidget.canvas.axes.set_title('Sorting Visualization')
            self.MplWidget.canvas.draw()
            speed_value = self.horizontalSlider.value()
            speed = (100-speed_value)/150
            time.sleep(speed)
            QApplication.processEvents()
            str2 = " ".join(str(e) for e in self.array) #make array string
            self.textEdit_2.setText(str2) #display the unsortedarray
            ##### 
        for i in range(0, size):
            array[i] = output[i]
            
            self.MplWidget.canvas.axes.get_xaxis().set_visible(False)
            self.MplWidget.canvas.axes.get_yaxis().set_visible(False)
            self.MplWidget.canvas.axes.clear()
            for m, v in enumerate(self.array):
                        self.MplWidget.canvas.axes.text(m+.70, v+1, " "+str(v), color='black', va='center', fontweight='bold')
            self.MplWidget.canvas.axes.bar(np.linspace(1,len(self.array),len(self.array)),self.array,color=['yellow'])
            #self.MplWidget.canvas.axes.legend(('cosinus', 'sinus'),loc='upper right')
            self.MplWidget.canvas.axes.set_title('Sorting Visualization')
            self.MplWidget.canvas.draw()
            speed_value = self.horizontalSlider.value()
            speed = (100-speed_value)/150
            time.sleep(speed)
            QApplication.processEvents()
            #We are using this block to print the array inside an textbox :  
            str2 = " ".join(str(e) for e in self.array) #make array string
            self.textEdit_2.setText(str2) #display the unsortedarray 
            
            ##### 
    
    def radixSort(self):
        global array
        max_element = max(self.array)
        place = 1
        while max_element // place > 0:
           self.countingSort(self.array, place)
           place *= 10
    
    
    
    
    
    ################################################
   
    ######################################################
    def counting_sort(self):
        global array
        array1 = self.array
        max_val = max(array1)
        m = max_val + 1
        count = [0] * m

        self.MplWidget.canvas.axes.get_xaxis().set_visible(False)
        self.MplWidget.canvas.axes.get_yaxis().set_visible(False)
        self.MplWidget.canvas.axes.clear()
       # for m, v in enumerate(array1):
         #               self.MplWidget.canvas.axes.text(m+.70, v+1, " "+str(v), color='black', va='center', fontweight='bold')
        self.MplWidget.canvas.axes.bar(np.linspace(1,len(array1),len(array1)),array1,color=['yellow'])
        self.MplWidget.canvas.axes.set_title('Sorting Visualization')
        self.MplWidget.canvas.draw()
        speed_value = self.horizontalSlider.value()
        speed = (100-speed_value)/150
        time.sleep(speed)
        QApplication.processEvents()
                     
    
        for a in array1:
        # count occurences
            count[a] += 1             
        i = 0
        for a in range(m):            
            for c in range(count[a]):  
                array1[i] = a
                i += 1
                
                self.MplWidget.canvas.axes.get_xaxis().set_visible(False)
                self.MplWidget.canvas.axes.get_yaxis().set_visible(False)
                self.MplWidget.canvas.axes.clear()
              #  for m, v in enumerate(array1):
               #         self.MplWidget.canvas.axes.text(m+.70, v+1, " "+str(v), color='black', va='center', fontweight='bold')
                self.MplWidget.canvas.axes.bar(np.linspace(1,len(array1),len(array1)),array1,color=['yellow'])
                self.MplWidget.canvas.axes.set_title('Sorting Visualization')
                self.MplWidget.canvas.draw()
                speed_value = self.horizontalSlider.value()
                speed = (100-speed_value)/150
                time.sleep(speed)
                QApplication.processEvents()
        str2 = " ".join(str(e) for e in array1) #make array string
        self.textEdit_2.setText(str2) #display the unsortedarray
  
            
def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':     
    main()