#Data Preparation
#We must prepare the data before we can use it. How? We must import it from somewhere.

#Importing Data
import pandas as pd

#pd.read_csv: read csv file using pandas
#header: 0 means the first row is the header
#sep: separator of the csv file
health_data = pd.read_csv("HealthData.csv", header=0, sep=",")
print(health_data)