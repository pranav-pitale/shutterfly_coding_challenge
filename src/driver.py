import argparse
from src import event_mapper
from src.util.file_processor import FileProcessor
from src.util.logger import Logger
from src.data_store.data_store import DataStore


class Driver:
    '''
    Driver class contains method and initialization of commandline arguments
    '''
    # command line argument initialization
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '--f', default="../input/input.txt",
                        help='Input file path')
    parser.add_argument("--topxltv", default=2,
                        help='Finds top x ltv valued customers')
    parser.add_argument('--loglevel', default='INFO',
                        help='Level of logging to use (default:WARNING, \
                        values: CRITICAL, ERROR, WARNING, INFO, DEBUG)')
    parser.add_argument('--output', default='../output/output.txt',
                        help='Output File path')
    args = parser.parse_args()

    if __name__ == '__main__':
        # Instatiation of logger object
        logObj = Logger()
        log = logObj.logger(args.loglevel)
        # Instatiation of FileProcessor object
        file_process = FileProcessor(log)
        log.info("File Processed")
        # Reads the data from input file
        data = file_process.read_file(args.file)
        # Instatiation of EventMapper object
        event = event_mapper.EventMapper(log)
        # Instatiation of Data D from DataStore
        D = DataStore()

        for e in data:
            # Feeding event one by one to Ingest method
            event.Ingest(e, D)
        # Call for calculating top x customer based on LTV value
        write_data = event.TopXSimpleLTVCustomers(int(args.topxltv), D)
        # Write top x customers to the output file
        file_process.write_file(args.output, write_data)
