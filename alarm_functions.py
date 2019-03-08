

def playPodcast():

	from subprocess import call
	import os
	from random import randint
	import datetime



	podcastDirectory = '/home/pi/Documents/Alarm_clock/podcasts'



	podcastList = os.listdir(podcastDirectory)
	podcastList = list(filter(lambda x: '.mp3' in x, podcastList))

	while datetime.datetime.now().hour <= 8:


		randomPodcast = randint(0, len(podcastList) - 1)

		toBePlayed = podcastList.pop(randomPodcast)
		fullPathToPodcast = podcastDirectory + '/' + toBePlayed
		playedList = podcastDirectory + '/' + 'playedlist.txt'

		f = open(playedList, 'r')
		played = f.readlines()
		f.close()
		
		played = [x.replace('\n', '') for x in played]

		if fullPathToPodcast in played:
			pass
		else:

			call(['ffplay', '-autoexit', fullPathToPodcast])

			f = open(playedList, 'a')
			f.write(fullPathToPodcast)
			f.write('\n')
			f.close()

	return None


def downloadPodcast():
    from subprocess import call

    call(['bash', '/home/pi/Documents/Alarm_clock/podcast_downloads.sh'])

    return None



def deleteDownloadedPodcasts():
    #from subprocess import call
    import os

    #call(['rm', '/home/pi/Documents/Alarm_clock/podcasts/*.mp3'])
    
    podcastDirectory = '/home/pi/Documents/Alarm_clock/podcasts'
    podcastList = os.listdir(podcastDirectory)
    podcastList = list(filter(lambda x: '.mp3' in x, podcastList))
    
    # remove newline character
    podcastList = [x.replace('\n', '') for x in podcastList]
    
    # remove duplicates
    podcastList = list(set(podcastList))
    
    for podcast in podcastList:
        try:
            os.remove(podcast)
        except:
            pass


    return None
    

def deletePlayedPodcasts():
    import os
    
    podcastDirectory = '/home/pi/Documents/Alarm_clock/podcasts'
    playedList = podcastDirectory + '/' + 'playedlist.txt'
    
    f = open(playedList, 'r')
    played = f.readlines()
    f.close()
    
    # delete new line characters
    played = [x.replace('\n', '') for x in played]
    
    # remove duplicates
    played = list(set(played))
    
    for podcast in played:
        try:
            os.remove(podcast)
        except:
            x = 2


    return None



def funkyMusic():
    from subprocess import call

    url = 'https://tunein.com/radio/100hitz---Urban-Hitz-s111383/'
    
    # skepta blocboy remix playlist
    url2 = 'https://www.youtube.com/watch?v=rYCD05L9NSk&list=RDrYCD05L9NSk&start_radio=1'
    
    # Drake nice for what mix
    url3 = 'https://www.youtube.com/watch?v=U9BwWKXjVaI&list=RDU9BwWKXjVaI'
    
    # Tyga taste mix
    url4 = 'https://www.youtube.com/watch?v=LjxulQ1bEWg&list=RDLjxulQ1bEWg'
    
    call(['x-www-browser', url])

    return None


def stopFunkyMusic():
    from subprocess import call

    call(['wmctrl', '-c', 'firefox'])
    call(['wmctrl', '-c', 'chrome'])
    call(['wmctrl', '-c', 'chromium'])

    return None
    
    
def playMusicOnDisk():
    from subprocess import call
    import os
    from random import randint
    import datetime

    # music_directory = '/media/fuzzylumpkins/MUSIC_USB/music_alarm'
    music_directory = '/media/pi/MUSIC_USB/music_alarm'

    song_list = os.listdir(music_directory)

    while datetime.datetime.now().hour <= 9:
        songnum = randint(0, len(song_list))
        full_path = music_directory + '/' + song_list[songnum]

        try:
            call(['ffplay', '-autoexit', full_path])
        except:
            x = 7
            # some logging function... or delete track?!

    return None
    
    

