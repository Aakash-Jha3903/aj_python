import csv
def write_csv():
	import csv
	# field names
	fields = ['Name', 'Branch', 'Year', 'CGPA']
	# data rows of csv file
	rows = [['Nikhil', 'COE', '2', '9.0'],
			['Sanchit', 'COE', '2', '9.1'],
			['Aditya', 'IT', '2', '9.3'],
			['Sagar', 'SE', '1', '9.5'],
			['Prateek', 'MCE', '3', '7.8'],
			['Sahil', 'EP', '2', '9.1']]
	# name of csv file
	filename = "university_records.csv"
	# writing to csv file
	with open(filename, 'w',newline="") as csvfile:
		# creating a csv writer object....................
		csvwriter = csv.writer(csvfile)
		# writing the fields
		csvwriter.writerow(fields)
		# writing the data rows
		csvwriter.writerows(rows)

def read_csv():
	filename = "university_records.csv"

	# initializing the titles and rows list
	fields = []
	rows = []

	# reading csv file
	with open(filename, 'r') as csvfile:
		# creating a csv reader object....................
		csvreader = csv.reader(csvfile)
		print("csvreader : ",type(csvreader))

		# extracting field names through first row
		print("fields : ",fields)
		fields = next(csvreader)
		print("fields : ",fields)

		# extracting each data row one by one
		for i in csvreader:
			rows.append(i)
 
    	# get total number of rows
    	# print("Total no. of rows: %d" % (csvreader.line_num))
		print("Total no. of rows : ",csvreader.line_num)

	# printing the field names
	print('Field names are:' + ', '.join(field for field in fields))

	# printing first 5 rows
	print('\nFirst 5 rows are:\n')
	for row in rows[:5]:
		# parsing each column of a row
		for col in row:
			print("%10s" % col, end=" "),
			# print(col, end=" "),+
		
		print('\n')


write_csv()
read_csv()
l = [1, 2, 3, 4, 5, 6]
iterator = iter(l)

a = next(iterator)
b = next(iterator)
print(a)
print(b)
print(type(iterator))
