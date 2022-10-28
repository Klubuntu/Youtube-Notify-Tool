import time
from urllib import response
import requests
from var_dump import var_dump
from webhook_bot import *

#UCifZaTQPiHE2QRgEwDNfhug

def genChannelData(channelId):
    apiget = f"https://www.googleapis.com/youtube/v3/search?order=date&part=snippet&channelId={channelId}&maxResults=1&key=AIzaSyBGX0yQtfRPu9CRBEC4mZ95fnvNj00msik"
    response = requests.get(apiget);
    response_api = response.json();
    #var_dump(response_api)
    print("Country Code: ", response_api.get('regionCode'))
    print('Channel Name:', response_api["items"][0]['snippet']['channelTitle'])
    print('Publish new video:', response_api["items"][0]['snippet']["title"])
    print('Video URL:', "https://youtu.be/"+ response_api["items"][0]['id']['videoId'])

genChannelData("UCifZaTQPiHE2QRgEwDNfhug")

"""while True:
    time.sleep(3)
"""

