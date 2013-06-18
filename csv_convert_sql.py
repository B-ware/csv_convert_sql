import csv

def read_csv(infilename,outfilename):
  with open(infilename, 'rb') as csvfile:
		doc = csv.reader(csvfile, delimiter = ',', quotechar = '|')
		rownum = 0
		
		values = []
		for row in doc:
			if rownum == 0:
				contents = row
				contents = ",".join(row)
				values.insert(rownum, contents)
			else:
				value = [] 
				colnum = 0
				for col in row:
					if colnum == 0 or colnum == 7 or colnum == 8:
						value.append("'" + col + "'")
					else:
						value.append(col)
					colnum += 1
				value = ",".join(value)
				values.insert(rownum, value)
			rownum += 1
			
		write_sql(values, outfilename, rownum)
		
def write_sql(values, outfilename, rownum):
	sql_file = open(outfilename, 'wb')
	i = 1
	while i < rownum:
		insert = "INSERT INTO xyz(" + values[0] + ") VALUES(" + values[i] + ");"
		sql_file.write("%s\n" % (insert));
		i += 1;
		
	sql_file.close()
	
def main():
	str = raw_input("CSV Filename: ");
	infilename = str + '.csv'
	outfilename = str + '.sql'
	read_csv(infilename,outfilename)

main()
