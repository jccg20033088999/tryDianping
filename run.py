import sys
reload(sys)
sys.setdefaultencoding('utf8')
from bs4 import BeautifulSoup
import urllib2, urllib
from json import *

def foo(page,token,type): 
    f = urllib2.Request(
        url     = 'https://m.dianping.com/activity/static/list?page='+str(page)+'&cityid=2&regionParentId=0&regionId=0&type='+str(type)+'&sort=0&filter=1&token='+token,
        )

    response = urllib2.urlopen(f)
    g = response.read()
    d = JSONDecoder().decode(g)

    actList = []
    for act in d["data"]["mobileActivitys"]:
        actList.append(str(act["offlineActivityId"]))
        
    actList = list(set(actList))
    return actList

def foo2(actId,token): 
    data = {
            'phoneNo': '134****1234',
            'offlineActivityId': actId,
            'source': 'dpapp',
            'token': token
            }
    f = urllib2.Request(
        url     = 'http://m.dianping.com/mobile/event/'+actId+'/save',
        data    = urllib.urlencode(data)
        )
    response = urllib2.urlopen(f)
    soup=BeautifulSoup(response) 

    for lind in soup.find_all('span'):
        print str(lind).decode('UTF-8','ignore')
        break
        
def foo3(token): 
    f = urllib2.Request(
        url     = 'http://m.dianping.com/mobile/event/myprize?source=null',
        )
    f.add_header('Host', "m.dianping.com");
    f.add_header('Accept', "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/wxpc,*/*;q=0.8");
    f.add_header('Cookie', "_hc.v=5763a005-1d42-90a0-34c8-a01b35f2bb56.1480425421; dper="+token+"; _thirdbi.c=1a3f049c487e3207fe90542e443427b088efd655256ce2f8887183b4f7d921a10cbe0289017775a75b9459034c5668bc15ab5133e47341db411800b751b989064560c3ca7fb53c03fc6798585560dcf4; default_ab=citylist%3AA%3A1; cityid=2; __guid=87795908.4248828807560184300.1480425759969.573; share_ab=shop%3AA%3A1%7Cshopreviewlist%3AA%3A0; __mta=147749768.1480425423452.1480425761089.1480648905846.5; __mta=147749768.1480425423452.1480648905846.1481384642195.6");
    response = urllib2.urlopen(f)
    g = response.read()
    soup = BeautifulSoup(g)

    actList = []
    for lind in soup.find_all('span'):
        if "title" in str(lind):
            print str(lind).encode('GBK', 'ignore')

for token in ['yourToken']:
    for type in range(1,2):
        while True:
            actList = foo(1,token,type)
            for i in actList:
                foo2(i,token)
            if len(actList) < 5:
                break
    foo3(token)
while True:
    pass