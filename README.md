# Sequoia Scraping

This repo contains code I wrote for a blog post on Web Scraping which can be found at http://www.statworx.com/blog/.

## Motivation
In this repo I write code which scrapes all portfolio companies of Sequoia Capital which are listed on their website
at https://www.sequoiacap.com/companies/. I wrote this code to illustrate the basic principles of Web Scraping for the
blog post above. 

The blog itself goes into more theoretical background of web scraping in Python using Requests and BeautifulSoup.
The script in this repo is meant to be a minimal example of how you might scrape a page you are interested in.

As for Sequoia specifically, you might want to scrape their portfolio because you want to get a notification
anytime they announce or add a portfolio company. This could be useful because you would like to invest
in companies in Sequoia's portfolio (unlikely for Sequoia, but the principles would work the same for smaller VC firms)
or something similar.

I actually heard about a Twitter bot recently which would do exactly that: Whenever a Venture Capital firm in a certain pool
would add a new portfolio company, the Twitter bot would tweet that this firm just added a new portfolio company to their
website. The bot did this precisely by scraping the portfolios of different firms regularly and then comparing the scraped
data to the scraped data from e.g. a week ago, putting out a tweet about any companies which were in the latest scraped data
but not the one before.

## Miscellaneous
- All code was written in Python 3
- The script uses Requests to scrape the HTML and then parses this HTML using BeautifulSoup
- A requirements file for the main script can be found in this directory

If you have questions, suggestions or just feel like chatting about scraping,
please contact me here or at david.wissel@statworx.com
  
