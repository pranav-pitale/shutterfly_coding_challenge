from src.data_store.base_data_store import BaseDataStore
from datetime import datetime


class SiteVisitDataStore(BaseDataStore):
    '''
    Data structure for storing site visited data
    '''
    # Adds data to site visited data structure
    @staticmethod
    def add_data(event, D):
        # Removing micro-seconds from event-time
        if '.' in event.event_time:
            event_time = event.event_time[:event.event_time.index('.')]
        site_vist_value = dict()

        if event.customer_id not in D.site_visit: # noqa

            site_vist_value["object"] = [event]
            site_vist_value["site_visit"] = 1
            site_vist_value["min_date"] = datetime.strptime(
                event_time, '%Y-%m-%dT%H:%M:%S')
            site_vist_value["max_date"] = datetime.strptime(
                event_time, '%Y-%m-%dT%H:%M:%S')
            D.site_visit[event.customer_id] = site_vist_value
        else:
            site_vist_value = D.site_visit[event.customer_id]
            objectList = site_vist_value['object']
            objectList.append(event)
            site_vist_value['site_visit'] += 1
            event_time = datetime.strptime(event_time, '%Y-%m-%dT%H:%M:%S')

            if event_time < site_vist_value['min_date']:
                site_vist_value['min_date'] = event_time
            else:
                site_vist_value['max_date'] = event_time

            D.site_visit[event.customer_id] = site_vist_value

    # Gets data from site_visited data structure
    @staticmethod
    def get_data(D):
        return D.site_visit
