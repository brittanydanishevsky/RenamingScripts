# RenamingScripts
Renaming Python Script

1.	Column A in “rename.xlsx” must have the old name of the file. Column B must have the new name. 
2.	Python reads column A as column 0, column B as 1, etc. Similarly, row 1 in Excel is considered row 0. 
3.	Copy a file to the desktop of the images. Name it Images. This is the SRC (source) file.
4.	New file on Desktop called Renamed. This is the DST (destination) file. 
5.	“fileexists.py” checks through each row of column 0 in the rename.xlsx workbook and see’s if it exists in the Images folder. It will spit out which files do not exist and provide a total number of unfound files. 
6.	Once you’ve gotten the un-existing files down to zero (by deleting things, renaming, consolidating, by hand), you can run the renaming.py script. It will remove the file from Images and move it to Renamed with it’s new name. It will show you each file that’s been changed – if there is a failure, you can see where the program stopped and adjust i (the row counter) accordingly to restart the program from which files haven’t been renamed yet. Alternatively, you can adjust the error by hand, and start again with a new copied folder of Images on to the desktop. 
7.	Current pathways are set to work on the Desktop. Adjust accordingly, but I would recommended creating copies of things and working in the desktop, and then moving the final products into the correct folder. 
