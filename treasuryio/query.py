from json import load
from urllib2 import urlopen
from urllib import urlencode

from pandas import DataFrame

def query(sql, format='df'):
    '''
    Submit an `sql` query (string) to treasury.io and return a pandas DataFrame.

    For example::

        print('Operating cash balances for May 22, 2013')
        print(treasuryio.query('SELECT * FROM "t1" WHERE "date" = \'2013-05-22\';'))

    Return a dict::

        treasuryio.query('SELECT * FROM "t1" WHERE "date" = \'2013-05-22\';', format='dict')

    '''
    url = 'http://api.treasury.io/cc7znvq/47d80ae900e04f2/sql/'
    query_string = urlencode({'q':sql})
    handle = urlopen(url + '?' + query_string)
    if handle.code == 200:
        d = load(handle)
        if format == 'df':
            return DataFrame(d)
        elif format == 'dict':
            return d
        else:
            raise ValueError('format must equal "df" or "dict"')
    else:
        raise ValueError(handle.read())
