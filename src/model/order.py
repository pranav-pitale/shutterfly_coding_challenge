
class Orders(object):
    '''
    Class for model for order events
    '''

    def __init__(self):

        self.key = None
        self.event_time = None
        self.customer_id = None
        self.total_amount = None
