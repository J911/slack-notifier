<div align="CENTER">
    <h1>파이썬에서 쉽게 Slack으로 Noti를 보내세요!</h1>
    <p>📮WebHook 기반 Slack 알리미</p>
</div>

<div align="CENTER">
    <img src="assets/demo.gif" alt="demo" />    
</div>

```python
from SlackNotifier.notifier import SlackNotifier

api_url = 'https://hooks.slack.com/services/' #  your WebHookUrl
channel = '#your-channel'
sn = SlackNotifier(api_url, channel)

# ... 

sn.noti('Noti!') # 당신이 원하는 위치에 추가하세요.

# ...
```

## Usage

1. WebHookUrl을 생성합니다.:
[https://api.slack.com/incoming-webhooks](https://api.slack.com/incoming-webhooks)

2. 당신의 프로젝트에 SlackNotifier를 Import 합니다.

3. SlackNotifier객체를 다음 인자를 넣어 생성합니다
    - WebHookUrl (api_url)
    - channel
    - username(Default: 'SlackNotifier')
    - icon_emoji(Default: 'thumbsup')

4. 원하는 위치에서 noti를 호출합니다!

## requirements
requirements: requests, json

```bash
$ pip install requests
```
or
```bash
$ pip3 install requests
```

<div align="CENTER">
    <h3> 코드 한 줄로 당신의 업무의 생산성을 높이세요 🙌🏼🙌🏼</h3>
</div>
