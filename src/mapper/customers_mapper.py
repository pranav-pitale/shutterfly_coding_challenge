from src.mapper.base import Base
from ..util import remove_unicode


class CustomersMapper(Base):
    '''
    Class for mapping customer
    '''
    # Functions maps value to model of customer
    @staticmethod
    def map_to_model(object_entry, customer):

        customer.key = remove_unicode.clean_unicodeing(object_entry['key'])
        customer.event_time = remove_unicode.clean_unicodeing(
            object_entry['event_time'])
        # Handling null value of last name
        if 'last_name' in object_entry:
            customer.last_name = remove_unicode.clean_unicodeing(
                object_entry['last_name'])
        else:
            customer.last_name = None
        # Handling null value of address city
        if 'adr_city' in object_entry:
            customer.adr_city = remove_unicode.clean_unicodeing(
                object_entry['adr_city'])
        else:
            customer.adr_city = None

        # Handling null value of address state
        if 'adr_state' in object_entry:
            customer.adr_state = remove_unicode.clean_unicodeing(
                object_entry['adr_state'])
        else:
            customer.adr_state = None

        return customer
