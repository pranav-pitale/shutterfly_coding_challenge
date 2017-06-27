

class DataStore(object):
    '''
    Data Structure class for D
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.customers = dict()
        self.orders = dict()
        self.images = dict()
        self.site_visit = dict()
