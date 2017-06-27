from src.data_store.base_data_store import BaseDataStore


class ImageData(BaseDataStore):
    '''
    Data structure for storing customer data
    '''
    # Adds data to image data structure
    @staticmethod
    def add_data(event, D):
        if not event.customer_id in D.images: # noqa
            D.images[event.customer_id] = [event]
        else:
            image_value = D.images[event.customer_id]
            image_value.append(event)
            D.images[event.customer_id] = image_value

    # Gets data from image data structure
    @staticmethod
    def get_data(D):
        return D.images
