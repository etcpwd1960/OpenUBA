'''
Copyright 2019-Present The OpenUEBA Platform Authors
This file is part of the OpenUEBA Platform library.
The OpenUEBA Platform is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
The OpenUEBA Platform is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Lesser General Public License for more details.
You should have received a copy of the GNU Lesser General Public License
along with the OpenUEBA Platform. If not, see <http://www.gnu.org/licenses/>.
'''


'''
@name
@description Process engine is the default state of the system, whereby it will ingest
logs into the system

'''
import logging
from dataset import *

dataset_scheme = {
    "mode": "test",
    "folder": "../test_datasets/toy_1",
    "data":
        [
            {
                "log_name": "proxy",
                "type": "csv",
                "location_type": "disk",
                "folder": "proxy"
            }
        ]
}

class ProcessEngine():

    def __init__(self):
        logging.info("Process engine is initiated")


    '''
    @name execute
    @description run the process engine
    '''
    def execute(self):
        logging.info("executing process engine")
        data_folder = dataset_scheme["folder"]
        # load data from scheme above, for test
        for log_obj in dataset_scheme["data"]:
            self.process_data(data_folder, log_obj)

    '''
        @name process_data
        @description update the current data in the system for each log type.
        This means that we will load a new set of records into the system
    '''
    def process_data(self, data_folder: str, log_data_obj: dict):

        logging.warning("Data Folder: "+str(data_folder))

        log_name = log_data_obj["log_name"]
        log_type = log_data_obj["type"]
        location_type = log_data_obj["location_type"]
        folder = log_data_obj["folder"]

        dataset_session = Dataset_Session(log_type)

        if log_type == "csv":
            dataset_session.read_csv(data_folder, folder, location_type) # load

            print( "isinstance(dataset_session.dataset, Dataset): "+str(isinstance(dataset_session.dataset, Dataset)) )

            # get size
            dataset_size: int = dataset_session.get_size()
            logging.warning( "Dataset Session size: "+str(dataset_size) )