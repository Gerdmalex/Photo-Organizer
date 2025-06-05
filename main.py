from app.filesystem import start_process

if __name__ == '__main__':

    source = '/path/to/source/folder'
    destination = '/path/to/destination/folder'
    extension = '.DNG'
    copy_files = True
    rename_files = False
    start_process(source, destination, extension, copy_files, rename_files)

