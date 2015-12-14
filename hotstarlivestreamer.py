import livestreamer
import json
import urllib2

url = raw_input('paste the link: ')
id = url[url.rindex('/')+1:]
HOTSTAR_CDN = "http://getcdn.hotstar.com/AVS/besc?action=GetCDN&asJson=Y&channel=TABLET&type=VOD&id=" + str(id)
responsestring = urllib2.urlopen(HOTSTAR_CDN).read()
jsonresponse = json.loads(responsestring)
dl_url =  jsonresponse['resultObj']['src']
the_real_url = "hlsvariant://" + str(dl_url)
streams = livestreamer.streams(the_real_url)
qualities = streams.keys()
print qualities
the_qlty = raw_input('?')
stream = streams[str(the_qlty)]
print stream.url
