import datetime
from datetime import datetime, timedelta
start_date = datetime.strptime('2019-09-21', '%Y-%m-%d').date()
end_date = datetime.strptime('2019-10-09', '%Y-%m-%d').date()
list_dates=[]
while start_date <= end_date:
    # print(start_date)
    list_dates.append(str(start_date))
    start_date = start_date+timedelta(days=1)


    # return d
print(list_dates)