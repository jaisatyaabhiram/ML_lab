from statistics import mean, median, mode
import numpy as np
#central Tendency
data = [5,10,15,20,25,20,20]
mean_value = mean(data)
median_value = median(data)
mode_value = mode(data)
print(f"DataSet : {data}")
print(f"Mean value :{mean_value}")
print(f"median value :{median_value}")
print(f"Mode value :{mode_value}")

range_value = max(data)-min(data)

#Calculate quartiles
q1 = np.percentile(data,25)#first quartile
q3 = np.percentile(data,75)

#calculate quartile range(IQR)
iqr = q3 - q1
#output results
print(f"DataSet : {data}")
print(f"Range: {range_value}")
print(f"First Quartile(Q1):{q1}")
print(f"Third Quartile(Q3):{q3}")
print(f"Interquartile range(IQR):{iqr}")


