pytreasuryio
======
Access .. _treasury.io: http://treasury.io from Python.

This is a package consisting of a single, simple function for submitting ``SQL`` queries to .. _treasury.io: http://treasury.io from ``python``. While you could simply copy-and-paste the function from script-to-script, this makes it quicker and easier to get up and running!

It also has some helpers to make a Twitter bot from the treasury.io data.

Installation
--------
Install with pip.::

    pip install treasuryio

Example
---------

Basic query
~~~~~~~~~
Send an SQL query and receive a pandas data frame.::

    # Operating cash balances for May 22, 2013
    import treasuryio
    sql = 'SELECT * FROM "t1" WHERE "date" = \'2013-05-22\';'
    treasuryio.query(sql)

Twitter bot
~~~~~~~~~
Write a ``~/.twitter.yml`` file.::

    consumer_key: oeshaoduhsaousaoeuhts
    consumer_secret: b233tsao-enuhsaoehsunoesudtuhoelaouhs2uo
    access_token: 2349081293-astoehusatoehusaoeustahoeuhh2AOEUTAouhc
    access_token_secret: 9023uonshesuaHONETuoeuoeouo0eOHNEuhOuoeu
    
Define a function that produces the text of the tweet, and decorate it with the
``@treasurio.tweet`` decorator.::

    import treasuryio
    import humanize
    import math

    MIL = 1e6

    # Helpers to humanize numbers / dates
    def human_number(num):
        return humanize.intword(int(math.ceil(num))).lower()

    def human_date(date):
        return humanize.naturalday(date).title()

    @treasuryio.tweet
    def total_debt_tweet():
        df = treasuryio.query('SELECT date, close_today FROM t3c WHERE (item LIKE \'%subject to limit%\' AND year = 2013 AND month >=1) ORDER BY date DESC')

        # determine length of DataFrame
        end = len(df)-1

        # extract current amount and amount at the beginning of the year
        current_amt = df['close_today'][0]*MIL
        previous_amt = df['close_today'][end]*MIL

        # calculate change
        delta = abs(current_amt - previous_amt)

        # generate word to represnet the direction of change
        if current_amt > previous_amt:
            change = "increased"
        elif current_amt < previous_amt:
            change = "decreased"

        # humanize values
        # Notice the included ``human_date`` and ``human_number`` functions which simplify these values for you
        current_date = human_date(df['date'][0])
        amt = human_number(current_amt)
        delta = human_number(delta)
        previous_date = human_date(df['date'][end])

        # generate tweet
        vals = (current_date, amt, change, previous_date, 'http://treasury.io')
        return "As of %s, the US Gov is $%s in debt. This amount has %s since %s - %s" % vals

Then just run it.::

    total_debt_tweet()

You can get fancy by switching the functions that you use.::

    import treasuryio
    import random

    @treasurio.tweet
    def tweet_a():
        # ...

    @treasurio.tweet
    def tweet_b():
        # ...

    @treasurio.tweet
    def tweet_c():
        # ...

    random.choice([tweet_a, tweet_b, tweet_c])()
