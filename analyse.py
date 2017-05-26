import pandas as pd
from datetime import datetime

# Read the psv file into pandas dataframe
dataframe = pd.read_csv('test.psv', sep='|', header=1)

# Extract data from frame and load separate columns
data = dataframe.values

dates = data[:,0]
y = data[:,1]
yhat = data[:,2]

# Convert dates to datetime object and return integer day of week
daysofweek = []

for date in dates:
	day = datetime.strptime(date, '%Y-%m-%d').weekday()
	daysofweek.append(day)

# Calculate true and false positive and negatives
tp = 0
fp = 0
tn = 0
fn = 0

for i in range(0,len(daysofweek)):
	if daysofweek[i] == 3:
		# import pdb; pdb.set_trace()
		if y[i] == 1:
			if yhat[i] == 1:
				tp += 1
			else:
				fn += 1
		if y[i] == 0:
			if yhat[i] == 1:
				fp += 1
			else:
				tn += 1


# Calculate precision, recall and F1
precision = tp / (tp+fp)
recall = tp / (tp+fn)
F1 = 2*(precision*recall)/(precision+recall)

print(F1)