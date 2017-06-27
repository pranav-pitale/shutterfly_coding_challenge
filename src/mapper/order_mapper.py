from src.mapper.base import Base
from ..util import remove_unicode


class OrderMapper(Base):
    '''
    Class for mapping order model
    '''
    # Maps order value to image object
    @staticmethod
    def map_to_model(object_entry, order):
        order.key = remove_unicode.clean_unicodeing(
            object_entry['key'])
        order.event_time = remove_unicode.clean_unicodeing(
            object_entry['event_time'])
        order.customer_id = remove_unicode.clean_unicodeing(
            object_entry['customer_id'])
        order.total_amount = remove_unicode.clean_unicodeing(
            object_entry['total_amount'])
        return order
