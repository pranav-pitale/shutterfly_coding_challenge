'''
Created on Jun 24, 2017

@author: Pranav
'''
from src.mapper.base import Base
from ..util import remove_unicode


class ImageMapper(Base):
    '''
    Class for mapping image upload model
    '''
    # Maps image value to image object
    @staticmethod
    def map_to_model(object_entry, image):
        image.key = remove_unicode.clean_unicodeing(
            object_entry['key'])
        image.event_time = remove_unicode.clean_unicodeing(
            object_entry['event_time'])
        image.customer_id = remove_unicode.clean_unicodeing(
            object_entry['customer_id'])

        # Hanlding null value of camera make
        if 'camera_make' in object_entry:
            image.camera_make = remove_unicode.clean_unicodeing(
                object_entry['camera_make'])
        else:
            image.camera_make = None

        # Hanlding null value of camera model
        if 'camera_model' in object_entry:
            image.camera_model = remove_unicode.clean_unicodeing(
                object_entry['camera_model'])
        else:
            image.camera_model = None
        return image
