import pytz
import datetime
#print(pytz.all_timezones) #España es 'Europe/Madrid',
print(datetime.datetime.now(pytz.timezone('Europe/Madrid')))