from src.mapper.base import Base
from ..util import remove_unicode


class SiteVisitMapper(Base):
    '''
    Class for mapping image upload model
    '''
    # Maps site_visit value to site_visit object
    @staticmethod
    def map_to_model(object_entry, site_visit):

        site_visit.key = remove_unicode.clean_unicodeing(
            object_entry['key'])
        site_visit.event_time = remove_unicode.clean_unicodeing(
            object_entry['event_time'])
        site_visit.customer_id = remove_unicode.clean_unicodeing(
            object_entry['customer_id'])

        # Handling null value of tag
        if 'tags' in object_entry:
            site_visit.tags = object_entry['tags']
        else:
            site_visit.tags = None

        return site_visit
