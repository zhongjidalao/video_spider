import requests
import re

response = requests.get(input('请输入要下载的ins视频网址：'))

form = re.findall(r'<meta name="medium" content="(.*?)" />', response.text, re.S)[0]

name = re.findall('<title>(.*?)</title>', response.text, re.S)[0]
name = name.replace(':', '')
name = name.replace(' ', '')
name = name.replace('\n', '')
name = name.replace('"', '')

print(name)

if form == 'video':
    url = re.findall(r'<meta property="og:video" content="(.*?)" />', response.text, re.S)[0]
    re = requests.get(url)
    with open('%s.mp4' % name, mode='wb') as f:
        f.write(re.content)
elif form == 'image':
    url = re.findall(r'<meta property="og:image" content="(.*?)" />', response.text, re.S)[0]
    re = requests.get(url)
    with open('%s.jpg' % name, mode='wb') as f:
        f.write(re.content)