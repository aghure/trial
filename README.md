# trial
Added some trial code

=============
sms_scheduler
=============
main module to run this package is sms_scheduler ,give csv file as input to sms scheduler.
sms scheduler will camm task scheduler and put the message in queue.
--------
In this repository just added a placehoder for code and created package.

* TODO
-------
1)Read csv file -- csv file will contains mobile number and country code
2)sms_scheduler will read csv file.
3)From sms scheduler will insert CSV file data into mongo or any sqlite with tzinfo.
   -- Need to check should i put in sqlite or mongo
4)Use APScheduler or celery to schedule task at the given input time .
   -- both are new for me so need to read this and then need to take decision which i should use.
5)For APScheduler : https://apscheduler.readthedocs.io/en/latest/userguide.html
6)Celery :- http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html
7)Need to add logging and error handler for failed sms.
8)Need to handle failed job.



