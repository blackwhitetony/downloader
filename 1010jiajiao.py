import os
import time
import requests
from pyquery import PyQuery as pq

turl = "http://www.1010jiajiao.com/html5app/daan/answer/id/1247317" 
loc = "./tfqy9-b/"
os.makedirs(loc)
timmm = time.time()
nowpage = 0
resp = requests.get(turl)
resp.encoding = 'utf-8'
doc = pq(resp.text)
ml = doc('.ml')
cid = ml.children()
lis = cid.items()
for li in lis:
    nowpage = nowpage + 1
    cur_page = li('a').attr.href
    cur = requests.get(cur_page)
    cur.encoding = 'utf-8'
    curdoc = pq(cur.text)
    img = curdoc('.minifier').attr.src
    with open(loc + '/' + str(nowpage) + '.jpg', 'wb+') as f:
        f.write(requests.get(img).content)
    print('download page ' + str(nowpage) + ' succesfully')

print('download ' + str(nowpage) + ' pages succesfully')
print('use' + str(time.time() - timmm) + 'seconds')
