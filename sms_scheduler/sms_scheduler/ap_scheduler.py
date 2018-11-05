from pytz import utc

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ProcessPoolExecutor



class APScheduler(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(APScheduler, self).__init__()
		self.arg = arg

	
	def config_Scheduler(self,timezone):
		jobstores = {
		    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
		}
		executors = {
		    'processpool': ProcessPoolExecutor(max_workers=5)
		}
		job_defaults = {
		    'coalesce': False,
		    'max_instances': 3
		}
		scheduler = BackgroundScheduler()
		scheduler.configure(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=timezone)
		sched.add_job(job_function, 'interval', seconds = 1)
	
	def job_function():
		for num in listnums:
			message = client.messages.create(
  				to= num,
    			from_= outbound,
    			body=  text)

			print('Id # ' + message.sid + " has sent: " + str(text))

		#Schedule job function to be called every 60 seconds
	
