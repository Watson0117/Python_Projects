from datetime import datetime
import pytz
  

PORT = pytz.timezone('America/Los_Angeles')
lon = pytz.timezone('Europe/London')
NY = pytz.timezone('America/New_York')
DEN = pytz.timezone('America/Denver')


datetime_DEN = datetime.now(DEN)
print("Date & Time in Denver is : ",
      datetime_DEN.strftime('%Y:%m:%d %H:%M:%S %Z %z'))

datetime_PORT = datetime.now(PORT)
print("Date & Time in Portland is : ",
      datetime_PORT.strftime('%Y:%m:%d %H:%M:%S %Z %z'))
  
datetime_lon = datetime.now(lon)
print("Date & Time in London is: ", 
      datetime_lon.strftime('%Y:%m:%d %H:%M:%S %Z %z'))

datetime_NY = datetime.now(NY)
print("Date & Time in New York is : ", 
      datetime_NY.strftime('%Y:%m:%d %H:%M:%S %Z %z'))
