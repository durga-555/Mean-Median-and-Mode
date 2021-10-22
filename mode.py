from collections import Counter
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

# finding Mode
data = Counter(new_data)
mode_data_for_range = {
    "50-60" : 0,
    "60-70" : 0,
    "70-80" : 0
}
for height, occurence in data.items():
    if 50 < float(height) < 60:
        mode_data_for_range["75-85"] += occurence
    elif 60 < float(height) < 70:
        mode_data_for_range["85-95"] += occurence
    elif 70 < float(height) < 80:
        mode_data_for_range["95-105"] += occurence
    elif 80 < float(height) < 90:
        mode_data_for_range["105-115"] += occurence
mode_range, mode_occurence = 0, 0
for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print(f"Mode is -> {mode:2f}")

        
