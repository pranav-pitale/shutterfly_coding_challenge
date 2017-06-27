import abc


class BaseDataStore(abc.ABCMeta):
    '''
    Abstract base class for data structures
    '''
    @abc.abstractmethod
    def add_data(self, event, D):
        pass

    @abc.abstractmethod
    def get_data(self):
        pass
