## Regular Expression are used to check complex patterns

import re

pattern = "Hi"
text = '''Lorem ipsum skjigf hi Hi kergnvg iengv dkjtring rignrgir irgnrigjr rjignirjgrijfnrigjighnrnb Hi hneifn jri'''
match = re.search(pattern, text)   # search is used to find 1st occurance
print(match)

# to find a word having "yclone" & before y it can have any alphabet from A-Z
pattern = r"[A-Z]+yclone"
text = '''Cyclone iernedf eigfnedf Dyclone fehufjed eifnekk'''
matches = re.finditer(pattern, text)   # finditer is used to find all the occurences in the text
for match in matches:
    print(match)
    print(match.span())