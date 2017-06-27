from src.data_store.data_store import DataStore
from src.event_mapper import EventMapper
import json


'''
Test to Check whether data related to site_visit event 
is ingested into data structure
'''
def test_ingest_site_visit():
    data_set = '{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e815502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "96f55c7d8f42", "tags": [{"some key": "some value"}]}'
    ingest = EventMapper()
    e = json.loads(data_set)
    flag = False
    D = DataStore()        
    ingest.Ingest(e, D)
    customer_id = '96f55c7d8f42'
    if customer_id in D.site_visit:
        flag = True
    assert flag == True

'''
Test to Check whether data related to site_visit event 
of multiple visits of same customer
is ingested into data structure
'''
def test_ingest_site_visit_mutiply_times_by_same_customer():
    data_set = '{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e815502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "96f55c7d8f42", "tags": [{"some key": "some value"}]}'
    ingest = EventMapper()
    customer_id = '96f55c7d8f42'
    D = DataStore()
    e = json.loads(data_set)
    ingest.Ingest(e, D)

    data_set = '{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e815502g", "event_time": "2017-01-07T12:45:52.041Z", "customer_id": "96f55c7d8f42", "tags": [{"some key": "some value"}]}'
    e = json.loads(data_set)
    ingest.Ingest(e, D)
    assert D.site_visit[customer_id]['site_visit'] == 2

'''
Test to Check whether data related to site_visit event 
of multiple visits of different customers
is ingested into data structure
'''
def test_ingest_site_visit_by_mutliple_customers():
    data_set = '{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e815502f", "event_time": "2017-01-06T12:45:52.041Z", "customer_id": "96f55c7d8f42", "tags": [{"some key": "some value"}]}'
    ingest = EventMapper()

    D = DataStore()
    e = json.loads(data_set)
    ingest.Ingest(e, D)

    data_set = '{"type": "SITE_VISIT", "verb": "NEW", "key": "ac05e815502g", "event_time": "2017-01-07T12:45:52.041Z", "customer_id": "96f55c7d8f43", "tags": [{"some key": "some value"}]}'
    e = json.loads(data_set)
    ingest.Ingest(e, D)
    assert len(D.site_visit) == 2

'''
Test to Check whether data related to customer event 
of multiple different customers
is ingested into data structure
'''
def test_ingest_for_event_customers():
    data_set = '{"type": "CUSTOMER", "verb": "NEW", "key": "96f55c7d8f42", "event_time": "2017-01-06T12:46:46.384Z", "last_name": "Smith", "adr_city": "Middletown", "adr_state": "AK"}'
    ingest = EventMapper()

    D = DataStore()
    e = json.loads(data_set)
    ingest.Ingest(e, D)

    data_set = '{"type": "CUSTOMER", "verb": "NEW", "key": "96f55c7d8f43", "event_time": "2017-01-07T12:46:46.384Z", "last_name": "Pat", "adr_city": "Middletown", "adr_state": "AK"}'
    e = json.loads(data_set)
    ingest.Ingest(e, D)
    assert len(D.customers) == 2

'''
Test to Check whether data related to image event 
of multiple different customers
is ingested into data structure
'''
def test_ingest_for_event_images():
    data_set = '{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede43b1d9g", "event_time": "2017-01-07T12:47:12.344Z", "customer_id": "96f55c7d8f45", "camera_make": "Canon", "camera_model": "EOS 80D"}'
    ingest = EventMapper()

    D = DataStore()
    e = json.loads(data_set)
    ingest.Ingest(e, D)

    data_set = '{"type": "IMAGE", "verb": "UPLOAD", "key": "d8ede43b1d9f", "event_time": "2017-01-06T12:47:12.344Z", "customer_id": "96f55c7d8f42", "camera_make": "Canon", "camera_model": "EOS 80D"}'
    e = json.loads(data_set)
    ingest.Ingest(e, D)
    assert len(D.images) == 2

'''
Test to Check whether data related to orders event 
of multiple different customers
is ingested into data structure
'''
def test_ingest_for_event_orders():
    data_set = '{"type": "ORDER", "verb": "NEW", "key": "68d84e5d1a45", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "96f55c7d8f44", "total_amount": "12.34 USD"}'
    ingest = EventMapper()

    D = DataStore()
    e = json.loads(data_set)
    ingest.Ingest(e, D)

    data_set = '{"type": "ORDER", "verb": "NEW", "key": "68d84e5d1a43", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "96f55c7d8f42", "total_amount": "10.34 USD"}'
    e = json.loads(data_set)
    ingest.Ingest(e, D)
    assert len(D.orders) == 2

'''
Test to Check whether data related to multiple 
orders event of same customers is 
ingested into data structure
'''
def test_ingest_for_event_orders_by_same_customer():
    data_set = '{"type": "ORDER", "verb": "NEW", "key": "68d84e5d1a45", "event_time": "2017-01-07T12:55:55.555Z", "customer_id": "96f55c7d8f44", "total_amount": "12.34 USD"}'
    ingest = EventMapper()
    customer_id = '96f55c7d8f44'
    D = DataStore()
    e = json.loads(data_set)
    ingest.Ingest(e, D)

    data_set = '{"type": "ORDER", "verb": "NEW", "key": "68d84e5d1a43", "event_time": "2017-01-06T12:55:55.555Z", "customer_id": "96f55c7d8f44", "total_amount": "10.34 USD"}'
    e = json.loads(data_set)
    ingest.Ingest(e, D)
    assert D.orders[customer_id]['total_amount'] == 22.68
