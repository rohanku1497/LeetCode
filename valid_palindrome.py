import re
s='malayalam'
s=re.sub(r'[^a-zA-Z]','',s)
s=re.sub(r'[0-9]','',s)
s=s.lower()
rev=s[::-1]
if s==rev:
    print(True)
else:
    print(False)