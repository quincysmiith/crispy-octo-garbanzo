#!/bin/bash

###
##
## Podcast Downloader
##

downloadDirectory='/home/pi/Documents/Alarm_clock/podcasts'


# download last 3 episodes in podcast series

#planet money
podcast-dl --limit 2 -o $downloadDirectory https://www.npr.org/rss/podcast.php?id=510289

#dave ramsey
podcast-dl --limit 2 -o $downloadDirectory http://daveramsey.ramsey.libsynpro.com/rss

#invisibilia
podcast-dl --limit 1 -o $downloadDirectory https://www.npr.org/rss/podcast.php?id=510307

#reply all
podcast-dl --limit 1 -o $downloadDirectory http://feeds.gimletmedia.com/hearreplyall


# 30 for 30
podcast-dl --limit 1 -o $downloadDirectory http://www.espn.com/espnradio/podcast/feeds/itunes/podCast?id=19472136

#Sandra
podcast-dl --limit 1 -o $downloadDirectory http://feeds.gimletmedia.com/sandrashow

# the allusionist 
podcast-dl --limit 1 -o $downloadDirectory http://feeds.theallusionist.org/Allusionist

# misistry of ideas
podcast-dl --limit 1 -o $downloadDirectory https://rss.simplecast.com/podcasts/3281/rss

# The audio book club
podcast-dl --limit 1 -o $downloadDirectory http://feeds.feedburner.com/SlateAudioBookClub

# Night Call
podcast-dl --limit 1 -o $downloadDirectory https://audioboom.com/channels/4943125.rss

# This is love
podcast-dl --limit 1 -o $downloadDirectory http://feeds.thisiscriminal.com/thisislovepodcast

# self service
#podcast-dl --limit 1 -o $downloadDirectory http://feeds.megaphone.fm/self-service

# endless thread
podcast-dl --limit 1 -o $downloadDirectory http://feeds.wbur.org/endlessthread/podcast

# proof to product
podcast-dl --limit 1 -o $downloadDirectory http://prooftoproduct.libsyn.com/rss

# dissect 
podcast-dl --limit 1 -o $downloadDirectory https://cityscoutmag.com/feed/dissect

# the moth
podcast-dl --limit 1 -o $downloadDirectory http://feeds.feedburner.com/themothpodcast

# where should we begin
podcast-dl --limit 1 -o $downloadDirectory http://esther.audible.libsynpro.com/rss

# stuff you should know
podcast-dl --limit 1 -o $downloadDirectory https://feeds.megaphone.fm/stuffyoushouldknow

# stuff you missed in history class
podcast-dl --limit 1 -o $downloadDirectory https://feeds.megaphone.fm/stuffyoumissedinhistoryclass

# stacking benjamins
podcast-dl --limit 2 -o $downloadDirectory http://stackingbenjamins.libsyn.com/rss

# stuff mom never told you
podcast-dl --limit 1 -o $downloadDirectory https://feeds.megaphone.fm/stuffmomnevertoldyou

# cook the perfect
podcast-dl --limit 1 -o $downloadDirectory https://podcasts.files.bbci.co.uk/p02nrwmn.rss

# caroline pregnancy podcast
# podcast-dl --limit 10 -o $downloadDirectory
