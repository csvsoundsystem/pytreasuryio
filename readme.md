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
