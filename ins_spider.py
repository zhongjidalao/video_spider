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
    url = re.findall('<meta property="og:video" content="(.*?)" />', response.text, re.S)[0]
    re = requests.get(url)
    with open('%s.mp4' % name, mode='wb') as f:
        f.write(re.content)
elif form == 'image':
    url_list = re.findall('"display_url":"(.*?)"', response.text, re.S)

    for url in url_list:
        print(url)
        temp = 0
        temp += 1
        name = name + str(temp)
        re = requests.get(url)
        with open('%s.jpg' % name, mode='wb') as f:
            f.write(re.content)