import requests
import time

URL = "https://discord.com/api/webhooks/1035640435403673660/0MpGfpqFlODT0qaFEencKKltVtJBJjwCv-O4TR8t7ZB3koUQJRztNb9Dkk6AStZAe8LH"
i=0


def genChannelData(channelId):
    global i
    apiget = f"https://www.googleapis.com/youtube/v3/search?order=date&part=snippet&channelId={channelId}&maxResults=1&key=AIzaSyBGX0yQtfRPu9CRBEC4mZ95fnvNj00msik"
    response = requests.get(apiget);
    response_api = response.json();
    #var_dump(response_api)
    channelName = response_api["items"][0]['snippet']['channelTitle']
    videoTitle = response_api["items"][0]['snippet']["title"]
    videoURL = "https://youtu.be/" + response_api["items"][0]['id']['videoId']
    thumbnailURL = response_api["items"][0]['snippet']['thumbnails']['medium']['url']
    print("Country Code: ", response_api.get('regionCode'))
    print('Channel Name:', response_api["items"][0]['snippet']['channelTitle'])
    print('Publish new video:', response_api["items"][0]['snippet']["title"])
    print('Video URL:', "https://youtu.be/"+ response_api["items"][0]['id']['videoId'])
    r = sendWebhook("YouTube", URL, f"Na kanale {channelName}, pojawił się nowy film", videoURL, videoTitle, thumbnailURL)
    i = i + 1
    return r


def sendWebhook(webhookName, webhookURL, webhookMsg, webhookVideoURL, webhookVideoTitle, webhookThumbnailURL):
    global url
    data = {
        #"content" : webhookVideoURL,
        "username" : webhookName
    }
    x = 1
    y = 2
    test = "{x} + {y}"
    data["embeds"] = [
        {   "image": {
                "url": webhookThumbnailURL
            },
            "description" : f"**{webhookVideoTitle}**\nZobacz: {webhookVideoURL}",
            "title" : webhookMsg,
            "video":{
                "url": webhookVideoURL
            }
        }
    ]
    result = requests.post(webhookURL, json = data)
    if(i >= 1):
      if(url == webhookVideoURL):
        #print(url)
        #print(webhookVideoURL)
        print("SAME")
      else:
        print("Adress Changed")
        return "URL (changed): " + url
    else:
        url = webhookVideoURL
        return "URL (first): " + url
    print(i)


#sendWebhook("YouTube", URL, "t")

"""url = genChannelData("UCifZaTQPiHE2QRgEwDNfhug")
print(url)"""

while True:
    try:
        url = genChannelData("UCifZaTQPiHE2QRgEwDNfhug")
        print(url)
    except KeyError as e:
        exit('Daily Limit Expired / Max Limit for few minutes Expired')
    except requests.exceptions.RequestException as e:
        print('Network/Internal Server connect problem')
        print(e)
    time.sleep(3)