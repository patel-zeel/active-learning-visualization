import re
import os
import sys
path = sys.argv[1]
save_path = sys.argv[2]
with open(path,'r') as f:
	data = f.read()
data = re.sub('Out\[\d+\]:','',data)
data = re.sub('<title>.*</title>','<title>Active Learning: A Visual Tour</title>',data)
with open(save_path,'w') as f:
        f.write(data)
