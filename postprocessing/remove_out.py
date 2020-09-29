import re
import os
with open('active-visualization/notebook/main.html','r') as f:
	data = f.read()
data = re.sub('Out\[\d+\]:','',data)
data = re.sub('<title>.*</title>','<title>Active Learning: A Visual Tour</title>',data)
with open('active-visualization/index.html','w') as f:
        f.write(data)
