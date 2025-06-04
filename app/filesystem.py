from os import path, walk, popen, makedirs
from os.path import join
from pathlib import Path
from shutil import move, copy
from datetime import datetime
from zoneinfo import ZoneInfo
import sys
from .database import Database

db = Database()


def read_files(source, ext):
    """
    Function to read all files from a specified source folder, \
    filter them by extension, read the date and time of their creation, \
    and add the data to the database.

    Args:
        source (str): Path to the source folder.
        ext (str): Extension of the file.
    """
    for dirpath, dirnames, files in walk(source):
        for f_name in files:
            f_path = join(dirpath, f_name).replace(" ", "\\ ")
            if not path.islink(f_path) and not Path(f_path).suffix != ext and not f_name.startswith("."):
                command_output = popen('mdls ' + f_path + ' -name kMDItemContentCreationDate')
                command_result = command_output.read()
                command_output.close()
                key_value = command_result.rstrip().split(' = ')
                dt = datetime.strptime(key_value[1], '%Y-%m-%d %H:%M:%S %z')
                berlin = ZoneInfo('Europe/Berlin')
                f_date = datetime.strftime(dt.astimezone(berlin), "%Y/%m/%d")
                f_time = datetime.strftime(dt.astimezone(berlin), "%H%M%S")
                db.insert(dirpath, f_name, f_date, f_time)


def process_files(destination, ext, cp=True, rename=False):
    """
    The function reads datasets of file data from the database, \
    sorted by creation date, and performs copying or moving. \
    In addition, the necessary folders are created.

    Args:
        destination (int): Path to the destination folder.
        ext (int): Extension of the file.
        cp (bool): Sets whether files are to be copied or moved.
        rename (bool): Sets whether files should be renamed or keep their original names.
    """
    file_index = 0
    file_count = db.count()
    for f in db.read():
        file_index += 1
        f_path, f_name, f_date, f_time = f
        year, month, day = tuple(f_date.split('/'))

        if not path.exists(path.join(destination, year, month, day)):
            makedirs(path.join(destination, year, month, day))

        if rename is False:
            dist = path.join(destination, year, month, day, f_name)
            copy_i = 0
            while path.isfile(dist):
                copy_i += 1
                dist = path.join(destination, year, month, day, f_name.replace('.', "_copy{}.".format(copy_i)))
        else:
            new_name = 'DJI_{}{}{}{}_{:04d}{}'.format(year, month, day, f_time, file_index, ext)
            dist = path.join(destination, year, month, day, new_name)

        try:
            if cp:
                copy(path.join(f_path, f_name), dist)
            else:
                move(path.join(f_path, f_name), dist)
        except OSError:
            print(path.join(f_path, f_name))
        finally:
            sys.stdout.write('\r{}% completed'.format(round(file_index*100/file_count)))
            sys.stdout.flush()

    print()
    db.close()
