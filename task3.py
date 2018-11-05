from collections import Counter
import re
f = open('war-peace.txt')
str = f.read()
f.close()
cnt = Counter(x for x in re.findall(r'[A-z\']{3,}', str))
print(cnt.most_common(10))