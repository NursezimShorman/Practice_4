#1
import re
s=input()
print(bool(re.fullmatch(r'ab*',s)))

#2
import re
s=input()
print(bool(re.fullmatch(r'ab{2,3}',s)))

#3
import re
s=input()
print(re.findall(r'[a-z]+_[a-z]+',s))

#4
import re
s=input()
print(re.findall(r'[A-Z][a-z]+',s))

#5
import re
s=input()
print(bool(re.fullmatch(r'a.*b',s)))

#6
import re
s=input()
print(re.sub(r'[ ,.]',':',s))

#7
import re
s=input()
print(re.sub(r'_([a-z])',lambda x:x.group(1).upper(),s))

#8
import re
s=input()
print(re.split(r'(?=[A-Z])',s))

#9
import re
s=input()
print(re.sub(r'([A-Z])',r' \1',s).strip())

#10
import re
s=input()
print(re.sub(r'([A-Z])',r'_\1',s).lower())

