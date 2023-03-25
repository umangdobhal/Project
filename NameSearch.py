import pandas as pd

# load the Excel sheet into a pandas dataframe
data = pd.read_excel('Sheet.xlsx')

# prompt the user to enter a medicine name
medicine_name = input('Enter a medicine name: ')

# search for the medicine in the dataframe and retrieve its usage and side effects
try:
    medicine_data = data.loc[data['drug_name'] == medicine_name]
    usage = medicine_data['medical_condition'].values[0]
    side_effects = medicine_data['medical_condition_description'].values[0]
    print('Usage:', usage)
    print('Side Effects:', side_effects)
except IndexError:
    print('Medicine not found.')
