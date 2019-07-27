import requests 
import json

class SlackNotifier():
    def __init__(self, url, channel, username='SlackNotifier', icon_emoji='thumbsup'):
        self.url = url
        self.channel = channel
        self.username = username
        self.icon_emoji = icon_emoji
        
    def getDTO(self, text):
        DTO = {
            'channel': self.channel,
            'username': self.username,
            'text': text,
            'icon_emoji': self.icon_emoji
        }

        return json.dumps(DTO)
    
    def noti(self, text):
        data = self.getDTO(text)
        result = requests.post(url=self.url, data=data)

if __name__ == '__main__' :
    WebHookUrl = 'https://hooks.slack.com/services/' #  your WebHookUrl
    channel = '#general'
    username='SlackNotifier'
    icon_emoji = 'thumbsup'

    sn = SlackNotifier(WebHookUrl, channel, username, icon_emoji)
    sn.noti('Noti!')