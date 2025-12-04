print('hello \n world')
print(r'hello \n world')

import re
string ="aashish@gmail.com"
pattern = '.com'
if re.search(pattern, string):
  print("Match found")

else:
    print("No match found")