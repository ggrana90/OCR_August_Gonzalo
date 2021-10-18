import os
import shutil

def TicketMove(filename):
    source_folder = 'Pending/'
    destination_folder = 'Processed/'
    for file_name in os.listdir(source_folder):
        # construct full file path
        source = source_folder + file_name
        destination = destination_folder + file_name
        # move only files
        if os.path.isfile(source):
            shutil.move(source, destination)
            print('Moved:', file_name)