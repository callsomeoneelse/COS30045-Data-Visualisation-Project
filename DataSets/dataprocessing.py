import pandas as pd
import numpy as np

# Load the CSV file
data = pd.read_csv('DataSets/TreatableDeathsOECD.csv')

# Convert 'Value' to numeric, setting errors='coerce' to handle non-numeric data
data['Value'] = pd.to_numeric(data['Value'], errors='coerce')

# Filter data for the years 2019, 2020, and 2021
filtered_data = data[data['Year'].isin([2019, 2020, 2021])]

# Calculate the average of the values for these years
mean_values = filtered_data.groupby('Country')['Value'].mean().reset_index()

# Create a new DataFrame for 2023 using existing countries listed for 2023
countries = data['Country'].unique()
new_data_2023_corrected = pd.DataFrame({
    'Country': countries,
    'Year': 2023,
    'Value': np.nan  # Initialize with NaNs
})

# Map the average values calculated earlier to the new DataFrame
new_data_2023_corrected = new_data_2023_corrected.merge(mean_values, on='Country', how='left', suffixes=('', '_mean'))
new_data_2023_corrected['Value'] = new_data_2023_corrected['Value_mean']
new_data_2023_corrected['Value'] = new_data_2023_corrected['Value'].map(lambda x: f"{x:.2f}")
new_data_2023_corrected.drop(columns='Value_mean', inplace=True)

# Save the new DataFrame to a CSV file
output_file_path = 'Output_TreatableDeathsOECD.csv'
new_data_2023_corrected.to_csv(output_file_path, index=False)

# Return the path to the saved file
output_file_path




