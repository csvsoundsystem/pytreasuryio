from json import load
from urllib2 import urlopen
from urllib import urlencode

from pandas import DataFrame

def query(sql):
    '''
    Submit an `sql` query (string) to treasury.io and return a pandas DataFrame.

    For example::

        print('Operating cash balances for May 22, 2013')
        print(treasury.io('SELECT * FROM "t1" WHERE "date" = \'2013-05-22\';'))
    '''
    url = 'https://premium.scraperwiki.com/cc7znvq/47d80ae900e04f2/sql/'
    query_string = urlencode({'q':sql})
    handle = urlopen(url + '?' + query_string)
    if handle.code == 200:
        d = load(handle)
        return DataFrame(d)
    else:
        raise ValueError(handle.read())
