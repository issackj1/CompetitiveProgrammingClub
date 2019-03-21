from sys import stdin
from collections import Counter
c = Counter()
for line in stdin:
    if(line != "***"):
        c[line] += 1
if c.most_common(2)[0][1] == c.most_common(2)[1][1]:
    print("Runoff!")
else:
    print(c.most_common(1)[0][0])

        
    


        

