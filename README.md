# trial
Added some trial code


sms_scheduler


main module to run this package is sms_scheduler ,give csv file as input to sms scheduler.
sms scheduler will call task scheduler and put the message in queue.

--------
In this repository just added a placehoder for code and created package.

* TODO
-------
- Read csv file -- csv file will contains mobile number and country code
- sms_scheduler will read csv file.
- From sms scheduler will insert CSV file data into mongo or any sqlite with tzinfo.
   --( Need to check should i put in sqlite or mongo)
- Use APScheduler or celery to schedule task at the given input time .
   --(both are new for me so need to read this and then need to take decision which i should use.)
- For APScheduler : https://apscheduler.readthedocs.io/en/latest/userguide.html
- Celery :- http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html
- Need to add logging and error handler for failed sms.
- Need to handle failed job.




