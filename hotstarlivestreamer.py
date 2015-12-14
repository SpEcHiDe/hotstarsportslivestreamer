import livestreamer
import json
import urllib2

def get_id(url) :
    return url[url.rindex('/')+1:]

def get_src_stream(id) :
    HOTSTAR_CDN = "http://getcdn.hotstar.com/AVS/besc?action=GetCDN&asJson=Y&channel=TABLET&type=VOD&id=" + str(id)
    responsestring = urllib2.urlopen(HOTSTAR_CDN).read()
    jsonresponse = json.loads(responsestring)
    dl_url =  jsonresponse['resultObj']['src']
    the_real_url = "hlsvariant://" + str(dl_url)
    return the_real_url

def the_real_download(streams,quality) :
    stream = streams[quality]
    return stream.url    

if __name__ == "__main__" :
    url = raw_input('paste the link: ')
    id = get_id(url)
    the_real_thing = get_src_stream(id)
    streams = livestreamer.streams(url)
    qualities = streams.keys()
    print qualities
    the_qlty = raw_input('?')
    dbg_info = the_real_download(streams,str(the_qlty))
    print dbg_info

    
    
    

    
