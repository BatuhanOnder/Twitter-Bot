import twint


class tweetscraper:

    def __init__(self,Config, ScrollCount):
        self.Config = Config
        self.scrape_all_tweets(ScrollCount)



    def tweet_scraper(self):
        ''' Bu metot kullanici twitlerini çekmek için kullanilir'''
        # Configuration
        c = self.Config

        # Run
        twint.run.Search(c)

    def scrape_all_tweets(self, ScrollCount):
        ''' Diger parametreler eklenecek'''
        for i in range(ScrollCount):
            self.tweet_scraper()




