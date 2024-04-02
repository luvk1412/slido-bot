slido_base_url = 'https://app.sli.do/event/geYBLJzrAPxHagW67E3rju/live/polls'
chrome_driver_path = 'drivers/chromedriver-mac-arm64/chromedriver'
repeats = 10 # number of time bot should run

# can be 'questions' or 'wordcloud'
mode='questions'

# For wordcloud
input_text = 'generative genies'

#For questions
# google on how to find xpath of an element, here we need xpath of upvote element
vote_button_xpath = '//*[@id="live-tabpanel-questions"]/div[4]/div/div/div/div/div[1]/div[3]/div[2]/button'