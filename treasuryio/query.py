from json import load
from urllib2 import urlopen
from urllib import urlencode

from pandas import DataFrame

def query(sql):
    url = 'https://box.scraperwiki.com/cc7znvq/47d80ae900e04f2/sql/'
    query_string = urlencode({'q':sql})
    handle = urlopen(url + '?' + query_string)
    if handle.code == 200:
        d = load(handle)
        return DataFrame(d)
    else:
        raise ValueError(handle.read())
