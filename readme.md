pytreasuryio
======
Access [treasury.io](http://treasury.io) from Python.

This is a package consisting of a single, simple function for submitting `SQL` queries to [treasury.io](http://treasury.io) from `R`. While you could simply copy-and-paste the function from script-to-script, this makes it quicker and easier to get up and running!

It also has some helpers to make a Twitter bot from the treasury.io data.

## Installation

    pip install treasuryio

## Example

### Basic query

    # Operating cash balances for May 22, 2013
    import treasuryio
    sql = 'SELECT * FROM "t1" WHERE "date" = \'2013-05-22\';'
    treasuryio.query(sql)

### Twitter bot
Write a `~/.twitter.yml` file.

    

Define a function that produces the text of the tweet, and decorate it with the
`@treasurio.tweet` decorator.

    import treasuryio

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
        # Notice the included `human_date` and `human_number` functions which simplify these values for you
        current_date = human_date(df['date'][0])
        amt = human_number(current_amt)
        delta = human_number(delta)
        previous_date = human_date(df['date'][end])

        # generate tweet
        vals = (current_date, amt, change, previous_date, URL)
        return "As of %s, the US Gov is $%s in debt. This amount has %s since %s - %s" % vals

Then just run it.

    total_debt_tweet()

You can get fancy by switching the functions that you use.

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
