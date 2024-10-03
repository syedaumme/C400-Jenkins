# import requests

# data= requests.get('https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv')

# # Convert the CSV content to a list of rows
# data_content =  data.text.splitlines()

# total_rows = len(data_content)-1
# unique_boroughs = set()



# for row in data_content: 
    
#     columns = row.split(',')
#     borough = columns[1].strip()
#     unique_boroughs.add(borough) 

# count = 0
# data=list(data_content)
# for row in data:
#     if row[1] == 'Brooklyn':  
#         count += 1

     

# # Sort unique boroughs 
# unique_boroughs = sorted(unique_boroughs)

# output_file = r'/root/taxi_zone_output.txt'
# with open(output_file, 'w') as file:
#     file.write(f"Total number of rows: {total_rows}\n")
#     file.write(f"Unique boroughs (sorted): {unique_boroughs}\n")
#     file.write(f"Number of records for Brooklyn: {count}\n")

# print(f"Total number of rows: {total_rows}\n")
# print(f"Unique boroughs (sorted): {unique_boroughs}\n")
# print(f"Number of records for Brooklyn: {count}\n")

import requests
import csv

url = 'https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv'

r = requests.get(url)
csvfile = 'taxi_zone_lookup.csv'


with open(csvfile, 'wb') as file:
    file.write(r.content)


with open(csvfile, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    data = list(reader)  


total_records = len(data)
uniqueborough = sorted(set(row[1] for row in data)) 

count = 0
for row in data:
    if row[1] == 'Brooklyn':  
        count += 1


output_file = 'taxi_zone_output.txt' 
with open(output_file, 'w') as f:
    f.write(f"Total Records: {total_records}\n")
    f.write(f"Unique Boroughs: {', '.join(uniqueborough)}\n")
    f.write(f"Records for Brooklyn: {count}\n")

print(f"Data saved to {output_file}")
