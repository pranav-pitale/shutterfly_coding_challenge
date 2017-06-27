from src.data_store.base_data_store import BaseDataStore


class CustomerData(BaseDataStore):
    '''
    Data structure for storing customer data
    '''
    # Adds data to customer data structure
    @staticmethod
    def add_data(event, D):

        D.customers[event.key] = event

    # Gets data from customer data structure
    @staticmethod
    def get_data(D):
        return D.customers
