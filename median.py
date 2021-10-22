import csv
with open('HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
# print(file_data)
# sorting data  to get the height of people.
new_data=[]
for i in range(len(file_data)):
	n_num = file_data[i][1]
	new_data.append(n_num)
 
n= len(new_data)
new_data.sort()
 # floor division-> //
if n%  2== 0:
    # first no.
  median1=float(new_data[n//2])
  # second no.
  median2=float(new_data[n//2-1])
  # finding the mean of those no.
  median = (median1+median2)/2
else:
    median= new_data[n//2]
    
print("median is "+str(median)) 
 
