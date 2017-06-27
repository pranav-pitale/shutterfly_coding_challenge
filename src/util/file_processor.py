'''
Created on Jun 24, 2017

@author: Pranav
'''
import json
import traceback
import os


class FileProcessor(object):

    '''
    Class for File Processing viz read
    and write operations
    '''
    def __init__(self, logger=None):

        self.logger = logger
        self.data = list()

    # Read data from file
    def read_file(self, file_name):

        try:
            if(os.path.exists(file_name)):
                with open(file_name, 'r') as f:
                    for line in f:
                        if line:
                            line = line.strip()

                            if(line[len(line)-1] in [',', ']']):
                                line = line[:-1]
                            if(line[0] == '['):
                                line = line[1:]

                            self.data.append(json.loads(line))
            return self.data
        except Exception:
            if self.logger:
                self.logger.exception(Exception.message)
            else:
                print(traceback.print_exc())
            exit()

    def write_file(self, file_name, data):
        try:
            with open(file_name, 'w') as f:
                for d in data:
                    print(d)
                    f.write(d+'\n')

        except Exception:
            if self.logger:
                self.logger.exception(Exception.message)
            else:
                print(traceback.print_exc())
            exit()
