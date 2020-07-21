class Source:
    """
    Class that generates new instances of news api source results
    """

    def __init__(self,id,name,category):
        '''
        define properties for our objects
        '''

        self.id = id
        self.name = name
        self.category = category