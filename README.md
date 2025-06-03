# Photo Organizer App

The problem this app solves involves the need to sort photos and add a unique name to each photo to identify it accurately.
Cameras allow the user to reset the file name counter, resulting in different photos existing under the same name.
In addition, some drones reset the file name counter when formatting the card, which also causes the above problem.

Another task that this app will solve is to sort photos into folders according to the date the photo was taken, for example, in year / month / day format.
This makes it easier to find a photo in the file system. 
The uniqueness of the file name can be either with the full date, for example DJI_20250603155540_0001.DNG, or the simplified DJI_0000001.DNG.

If the camera allows you to shoot and save photos in two formats, JPEG and RAW, then there is a need to separate the data by format, for example, for further uploading and processing in Lightroom or similar software. The user will be able to choose which format files should be organized.
This solution is oriented mainly to users of Unix/Linux systems, although it can be adapted for Windows operating system.

The Python programming language version 3.13 with standard libraries will be used exclusively for implementation. The metadata stored in the photo will be used to read the date of the photo. SQLite database will be used as temporary data storage during file structure reading and analysis. To create a graphical interface tkinter will be used. 

## Definition of the input data and settings
- The root folder where the files to be processed are located.
- The folder where the files are to be copied or moved.
- The file format must be selected from the list.
- Check box selection of the need to add the full date to the file name. 
- Check box to select whether to move files or only copy.

## Database definition
For operation only one table with the following fields is needed:
- absolute path to the file
- file name
- creation date
- creation time
