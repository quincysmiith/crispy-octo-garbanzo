import schedule
import time
import threading

import alarm_functions as af

def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

# schedule.every().friday.at("7:00").do(run_threaded, af.funkyMusic)
# schedule.every().friday.at("9:00").do(run_threaded, af.stopFunkyMusic)
schedule.every().friday.at("7:00").do(run_threaded, af.playMusicOnDisk)

schedule.every().monday.at("7:00").do(af.playPodcast)
schedule.every().tuesday.at("7:00").do(af.playPodcast)
schedule.every().wednesday.at("7:00").do(af.playPodcast)
schedule.every().thursday.at("7:00").do(af.playPodcast)

schedule.every().day.at("1:00").do(af.downloadPodcast)

schedule.every().monday.at("6:00").do(af.deletePlayedPodcasts)
schedule.every().tuesday.at("6:00").do(af.deletePlayedPodcasts)
schedule.every().wednesday.at("6:00").do(af.deletePlayedPodcasts)
schedule.every().thursday.at("6:00").do(af.deletePlayedPodcasts)
schedule.every().friday.at("6:00").do(af.deletePlayedPodcasts)

schedule.every().friday.at("10:00").do(af.deleteDownloadedPodcasts)

while True:
    schedule.run_pending()
    time.sleep(30)
