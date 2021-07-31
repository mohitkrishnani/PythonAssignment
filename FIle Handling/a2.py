import csv
rows = []
with open("sample_1.csv",'r') as inp:
	for row in csv.reader(inp):
		print(row)
		rows.append(row)
	with open("sample_1.csv",'w',newline='') as out:
		writer = csv.writer(out)
		for row in rows:
			row.append("Test")
		print(rows)
		for row in rows:
			writer.writerow(row)	
	for row in csv.reader(inp):
		print(row)
'''
Output
['1', 'one']
['2', 'two']
['3', 'three']
['4', 'four']
['5', 'five']

['1', 'one', 'Test'], 
['2', 'two', 'Test'], 
['3', 'three', 'Test'], 
['4', 'four', 'Test'], 
['5', 'five', 'Test']'''