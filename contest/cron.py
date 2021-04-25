from .views import * 
from date import *
def my_scheduled_job():
    try:
        startdate = datetime.today()
        contest = GroferContest().All_Contests.objects.filter(end_date = startdate ) 
        ().find_winner(contest)
    except:
        pass