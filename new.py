class News:
    """
    Class that generates new instances of news api results
    """

    news_list = [] # Empty contact list

    def __init__(self,title,description,urlToImage):
        '''
        define properties for our objects
        '''

        self.title = title
        self.description = description
        self.urlToImage = urlToImage