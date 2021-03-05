#Create the function 'is_string', Which checks if provided to it object is a string. The function should return 'True' or 'False'.

from typing import Any

def is_string(obj: Any) -> bool:
    return isinstance(obj,str)


arr = ['python', 22, ['elem'], '', {'elem'}, '323']

for obj in arr:
    if is_string(obj):
        print(f'"{obj}" is a string')
    else:
        print(f'"{obj}" is not a string')
        
# Output: "python" is a string
#         "22" is not a string
#         "['elem']" is not a string
#         "" is a string
#         "{'elem'}" is not a string
#         "323" is a string
