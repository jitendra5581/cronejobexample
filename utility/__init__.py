from datetime import datetime

from apscheduler.scheduler import Scheduler

# Start the scheduler



from datetime import datetime

from apscheduler.scheduler import Scheduler
from myapp1.views import *
from myapp2.views import *


# Start the scheduler
sched = Scheduler()
sched.start()

# def job_function():
#     print ("Hello World")

# Schedule job_function to be called every two hours
sched.add_interval_job(getdata, seconds=2)

# The same as before, but start after a certain time point
sched.add_interval_job(getdata, seconds=2, start_date='2019-11-22 07:00')

sched.add_interval_job(getapp2data, seconds=2)

# The same as before, but start after a certain time point
sched.add_interval_job(getapp2data, seconds=2, start_date='2019-11-22 07:00')

