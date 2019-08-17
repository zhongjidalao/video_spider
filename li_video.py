import requests
import re

response = requests.get(input('请输入要下载的梨视频网址：'))
url = re.findall('srcUrl="(.*?)"', response.text, re.S)[0]
name = re.findall('<title>(.*?)</title>', response.text, re.S)[0]

print(name)

name = name.replace(':', '')

re = requests.get(url)

with open('%s.mp4' % name, mode='wb') as f:
    f.write(re.content)