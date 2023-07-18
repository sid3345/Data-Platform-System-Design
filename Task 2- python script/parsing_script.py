# %%
# Importing pandas library
import pandas as pd

# Load the data of Sensors.csv into a Dataframe df
df = pd.read_csv('C:/Users/i0001440/Siddharth Sinha/Personal/CMCC tasks/Sensors.csv', sep = ';', decimal=',')

# Print the Dataframe
print(df)

# %%
# extracting max temp
max_temp = df.loc[:,['Longitude', 'Latitude', 'time', 'Temperature']].astype({'Temperature':'float'}).nlargest(1, columns="Temperature")
# display
print(max_temp)

# %%
# extracting min temp

min_temp = df.loc[:,['Longitude', 'Latitude', 'time', 'Temperature']].nsmallest(1, columns="Temperature")
print(min_temp)

# %%
# the list of values included in the bounding box identified by the vertices (lat, lon): (38, 16) - (40, 18) and the average temperature for each time step 
df_lat_long =df[(df.Longitude > 16) & (df.Longitude < 18) & (df.Latitude > 38) & (df.Latitude < 40) ]
print(df_lat_long)

# %%
# the list of values detected by the sensors whose average temperature exceeds 20C
df_temp = df[df.Temperature > 20]

# storing the result in a Results.csv file
df_temp.to_csv('C:/Users/i0001440/Siddharth Sinha/Personal/CMCC tasks//Results.csv', index=False)

print(df_temp)


