# To find the average temperature stored in the txt file

def get_average():
    with open('Files/data.txt', 'r') as file_local:
        data = file_local.readlines()
    values = data[1:]
    values = [float(i) for i in values]
    average_local = sum(values) / len(values)
    return average_local

average = get_average()
print(average)