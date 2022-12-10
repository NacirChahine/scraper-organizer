from apscheduler.schedulers.background import BackgroundScheduler
from .something_update import update_something
from Auction.models import *

def start():
    scheduler = BackgroundScheduler()
    mysecond = 5
    myauction = Auction.objects.all()

    scheduler.add_job(update_something, 'interval', seconds=mysecond)
    scheduler.start()