from datetime import timedelta
import datetime

# def timeSpan(start, end):
#         while start < end:
#             yield start
#             start += timedelta(minutes=15)
            
            
# for gio in timeSpan(datetime(year=2024,month=1,day=6,hour=8, minute=15), datetime(2024,1,6,12)):
#     print(gio.hour, gio.minute)
    


# def get_available():
#     start = datetime.datetime(2024,1,7,hour=10, minute=0)
#     end = datetime.datetime(2024,1,7,hour=16, minute=0)
#     sos = datetime.time(hour=11, minute=0)
#     ket = datetime.time(hour=12, minute=0)
#     while start < end:
#         if start.time() < sos:
#             yield start
#         elif start.time() > ket:
#             yield start
#         start += timedelta(minutes=30)


        
# for gio in get_available():
#     print(gio.hour, gio.minute)

gio = datetime.datetime.now().hour

ngay = datetime.date.today()
print(ngay)
