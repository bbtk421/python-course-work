import shutil
import os
import datetime

source = 'C:/Users/bbtk4/Documents/GitHub/python-course-work/file trasfer/A/'
dest = 'C:/Users/bbtk4/Documents/GitHub/python-course-work/file trasfer/B/'

files = os.listdir(source)

for i in files:
      modifyDate = datetime.datetime.fromtimestamp(os.path.getmtime(i))
      todaysDate = datetime.datetime.today()

      modifyDateLimit = modifyDate + datetime.timedelta(days=1)

      if modifyDateLimit > todaysDate:                                             
            shutil.copy(source+i, dest)
