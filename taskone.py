import pandas as pd 

#store file path in var
excel_file_1='Inputfile1.xlsx'
excel_file_2='Inputfile2.xlsx'

#read the excel file using pandas and store file in df1 and 2 repectivly 
#Here df is data frame 

df1 = pd.read_excel(excel_file_1)
df2 = pd.read_excel(excel_file_2)

"""#next is to know columns in data frame one and data frame two 
print(df1.columns)
print(df2.columns)
"""
sp_name = [
    'General Electric',
    'Infosys / GE Vernova',
    'GE Healthcare (sean holloway)',
    'General Electric Aviation',
    'GE Healthcare - Parallel Design SAS'
]
dps_status = [
    'Cancellation Request',
    'Cancelled'
]

"""filter_spname = df1.filter(items=['SP Name'], axis=1)"""
filtered_spname_df1 = df1[df1['SP Name'].isin(sp_name)]
#print(filtered_spname_df1)

latest_fweek1 = filtered_spname_df1['Fweek'].max()
filtered_fweek_df1 = filtered_spname_df1[filtered_spname_df1['Fweek'] == latest_fweek1]
print(f"------------------------------DATA FARME ONE = df1 AFTER APPLYING ALL FILTERS : ----------------------")
print(filtered_fweek_df1)


filtered_dps_status1 = filtered_fweek_df1[filtered_fweek_df1['DPS Status'].isin(dps_status)]
print(filtered_dps_status1)

#now filtering data frame 2 = df2

filtered_spname_df2 = df2[df2['SP Name'].isin(sp_name)]
latest_fweek2 = filtered_spname_df2['Fweek'].max()
filtered_fweek_df2 = filtered_spname_df2[filtered_spname_df2['Fweek'] == latest_fweek1]
print(f"------------------------------DATA FARME TWO = df2; AFTER APPLYING ALL FILTERS : ----------------------")
print(filtered_fweek_df2)



"""filtered_dps_status2 = filtered_spname_df2[filtered_spname_df2['DPS Status'].isin(dps_status)]
print(filtered_dps_status2)"""

"""# File path for master output
master_output = 'Master file.xlsx'

# Use ExcelWriter in append mode with openpyxl engine
with pd.ExcelWriter(master_output, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    filtered_fweek_df1.to_excel(writer, sheet_name='Filtered_df1', index=False)
    filtered_fweek_df2.to_excel(writer, sheet_name='Filtered_df2', index=False)
"""
# Merge filtered_fweek_df1 and filtered_fweek_df2 vertically
merged_df = pd.concat([filtered_fweek_df1, filtered_fweek_df2], ignore_index=True)

print(f"------------------------------MERGED DATAFRAME : ----------------------")
print(merged_df)

master_output = 'Master file.xlsx'
with pd.ExcelWriter(master_output, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
    merged_df.to_excel(writer, sheet_name='Merged_Data', index=False)