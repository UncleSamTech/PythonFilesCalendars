import os
from os import path
import shutil
import calendar

#line 1 to 4 imports all the necessary modules needed for running our code

#this class has three functions..one for acessing the calendar details and saving to a file, the other for reading the files and the


class get_calendar_to_files():
#this function creates a file named leap_years_store.txt, gets values from TextCalendar function that are leap years from 1900 -2050
#it then stores it inside the file leap_years_store.txt
      def getCalendar(self):
          store_files = open('leap_years_store.txt', 'w+')
		      calend = calendar.TextCalendar(calendar.SUNDAY)
		      for leap_years in range(1900,2050):
			        if leap_years % 4 == 0:
				         leap_years_in_cal = calend.formatmonth(leap_years,1)
				         store_files.write(leap_years_in_cal)
                 store_files.close()
                 
        def openFiles(self):
            files = open('leap_years_store.txt','r')
            if files.mode == 'r':
               contents = files.read()
               print(contents)
               files.close()
               
         def copyFilesCreated():
              if path.exists('leap_years_store.txt'):
		              src = path.realpath('leap_years_store.txt')
		              real_path = src + '.bak'
		              shutil.copy(src,real_path)
                  
#this fundtion will be used to run our instantiate our class and the run all the functions

def main() :
    cal_class = get_calendar_to_files()
    cal_class.openFiles()
    cal_class.getCalendar()
    cal_class.copyFilesCreated()
   

              
                  
