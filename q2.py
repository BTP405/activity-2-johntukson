import matplotlib.pyplot as plt

file_path = '/workspaces/activity-2-johntukson/snowfall.txt'

def graphSnowfall(t):
   snowfall_data = []
   snowfall_ranges = [0, 10, 20, 30, 40, 50]
   range_labels = [f"{snowfall_ranges[i]}-{snowfall_ranges[i+1]} cm" for i in range(len(snowfall_ranges)-1)]
   occurances = [0] * (len(snowfall_ranges) - 1)
   
   with open(t, 'r') as file:
    for line in file:
      if line.strip():
         snowfall_data.append(int(line.strip()))
         
   for i in snowfall_data:
      for j in range(len(snowfall_ranges) - 1):
         if snowfall_ranges[j] <= i <= snowfall_ranges[j + 1]:
            occurances[j] += 1
            break
         
   plt.bar(range_labels, occurances, color='blue')
   plt.xlabel('Snowfall Range (cm)')
   plt.ylabel('Number of Occurances')
   plt.title('Snowfall Accumlation Based on Occurance')
   plt.show()
   
graphSnowfall(file_path)
