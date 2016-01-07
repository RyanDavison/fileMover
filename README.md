# fileMover

fileMover.py contains two functions: createDirs and copyFiles which are used to 
create a series of sub-directories based on aerial imagery tile names and copy 
those imagery files into the appropriate sub-directory.

The sub-directory names are created using the first four digits of the imagery file names.
The imagery file names are based on a convention developed by the Colorado Department of 
Local Affairs (Division of Property Taxation). The first four digits are a state code for 
an individual township. The last two digits in the image name represents the section number 
that the imagery covers.

This script should be heavily modified before use to match with your own imagery file 
naming conventions.
