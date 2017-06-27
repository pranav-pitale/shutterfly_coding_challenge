import abc


class Base(abc.ABCMeta):
    '''
    Abstract Base class for mapping models
    '''
    @abc.abstractmethod
    def map_to_model(self, object_entry, site_visit):
        pass
