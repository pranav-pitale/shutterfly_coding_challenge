from src.data_store.data_store import DataStore
from src.event_mapper import EventMapper
from src.util.file_processor import  FileProcessor


'''
Test to Check whether top x 
calculated from data structure
'''
def test_topx_ltv():
    f = FileProcessor()
    data = f.read_file("../input/input.txt")
    D = DataStore()
    ingest = EventMapper()

    for e in data:
        ingest.Ingest(e, D)

    val = ingest.TopXSimpleLTVCustomers(2, D)

    assert val[0] == '96f55c7d8f50'
