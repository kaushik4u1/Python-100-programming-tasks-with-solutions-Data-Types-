#Get the file name from the variable 'path' and save it to the variable 'file_name'. Omit the file extension.

#Expected result:
#file

from pathlib import Path
 
path = '/home/user/dir/file.txt'
file_name = Path(path).stem
print(file_name)


#Output: 'file'
