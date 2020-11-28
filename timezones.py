from datetime import *
import pytz
from pytz import timezone

dt = datetime.now()
fmt = '%H:%M:%S %Z%z'

tzPDX = pytz.timezone('US/Pacific')
tzNYC = pytz.timezone('US/Eastern')
tzLON = pytz.timezone('Europe/London')

hqTime = dt.astimezone(tzPDX)
convHqTime = hqTime.strftime(fmt)
print("The time in Portland is " + convHqTime)
if (hqTime.hour >= 17 or hqTime.hour <= 9):
      print("We are closed.")
else:
      print("We are open!")

hqTime = dt.astimezone(tzNYC)
convHqTime = hqTime.strftime(fmt)
print("The time in New York City is " + convHqTime)
if (hqTime.hour >= 17 or hqTime.hour <= 9):
      print("We are closed.")
else:
      print("We are open!")

hqTime = dt.astimezone(tzLON)
convHqTime = hqTime.strftime(fmt)
print("The time in London is " + convHqTime)
if (hqTime.hour >= 17 or hqTime.hour <= 9):
      print("We are closed.")
else:
      print("We are open!")

