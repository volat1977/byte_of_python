from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# date = ['22-02-2020', '22-02-2020']

def date_list():
      dates = []
      for i in range(2):

            date_entry = dates.append(input('Enter a date in DD-MM-YYYY format :'))

      # print(dates)
      return  dates
# test = list(date_list())
# # print(type(test[0]))
# print(test[0])
date_list = date_list()
def convert_dates(date_list):
         for i in date_list:
             print(datetime.strptime(i, '%d-%m-%Y').date())

convert_dates(date_list)



