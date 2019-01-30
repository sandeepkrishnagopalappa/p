import pandas as pd


# Method to calculate the total FTU for the group
def calculate_ftu(group):
    return group['FTU - Computed Value'].sum()


# Method to calculate the FTU Utilization
def calculate_ftu_utlization(group):
    total = group['FTU - Computed Value'].sum()
    return round((total * 100) / 280)


# Method to calculate the FTU Utilization
def calculate_hrs_utlization(group):
    total = group['Time Spent (hrs)'].sum()
    return round((total * 100) / 152)


# Load excel to Pandas Library
df = pd.read_excel('C:\\AA_FTU_Data_Analysis\\aa_ftu.xlsx')
# Clean up the data
df['Accomplished By'].fillna('Unknown', inplace=True)
df['Time Spent (hrs)'] = df['Time Spent (hrs)'].astype('int')
df['Month'] = df['Month'].astype('str')


# Create Writer Object
writer = pd.ExcelWriter('C:\\AA_FTU_Data_Analysis\\Data.xlsx')

# FTU Trend Project wise for the Year-2018
grp_project = df.groupby('Project Name')
grp_project.apply(calculate_ftu).to_excel(writer, sheet_name='Project_FTU', header=['FTU'])

# FTU Trend Resource wise for the Year-2018
grp_resource = df.groupby('Accomplished By')
grp_resource.apply(calculate_ftu).to_excel(writer, sheet_name='FTU_Resource', header=['FTU'])

# FTU Trend /Project/Month for the Year-210
grp_month_project = df.groupby(['Month', 'Project Name'])
grp_month_project.apply(calculate_ftu).to_excel(writer, sheet_name='Project_Month', header=['FTU'])

# FTU Trend /Project/Month/Resource for the Year-2108
grp_month_project = df.groupby(['Month', 'Project Name', 'Accomplished By'])
grp_month_project.apply(calculate_ftu).to_excel(writer, sheet_name='Project_Month_Resource', header=['FTU'])

# FTU Trend Approach wise for the Year-2018
grp_approach_ftu = df.groupby(['Approach', 'Task Type'])
grp_approach_ftu.apply(calculate_ftu).to_excel(writer, sheet_name='FTU_Approach', header=['FTU'])

# Hours Spent (Approach) for the Year-2018
grp_approach_time = df.groupby(['Approach', 'Task Type'])
grp_approach_time['Time Spent (hrs)'].sum().to_excel(writer, sheet_name='Time_Approach', header=['Hours'])

# FTU Trend Project wise Manual
grp_approach = df.groupby('Approach')
manual = grp_approach.get_group('Manual')
manual = manual.groupby('Project Name')
manual.apply(calculate_ftu).to_excel(writer, sheet_name='Project_Manual_FTU', header=['Manual_FTU'])

# FTU Trend Project wise Automation
automation = grp_approach.get_group('Automated')
automation = automation.groupby('Project Name')
automation.apply(calculate_ftu).to_excel(writer, sheet_name='Project_Automation_FTU', header=['Automation_FTU'])

# Monthly FTU Trend for the Year-2108
grp_month = df.groupby('Month')
grp_month.apply(calculate_ftu).to_excel(writer, sheet_name='Monthly_FTU_Trend', header=['FTU'])

# Monthly FTU Trend (Operations) for the Year-2108
grp_Business_Group = df.groupby('Business Group')
grp_ot = grp_Business_Group.get_group('Operations')
grp_m = grp_ot.groupby('Month')
grp_m.apply(calculate_ftu).to_excel(writer, sheet_name='FTU_Trend_OT', header=['FTU'])

# Monthly FTU Trend (Customer Technology) for the Year-2108
grp_Business_Group = df.groupby('Business Group')
grp_ct = grp_Business_Group.get_group('Customer Technology')
grp_m = grp_ct.groupby('Month')
grp_m.apply(calculate_ftu).to_excel(writer, sheet_name='FTU_Trend_CT', header=['FTU'])

# Monthly FTU Utilization per Resource
grp_ftu = df.groupby(['Month', 'Accomplished By'])
s = grp_ftu.apply(calculate_ftu_utlization)
sd = s.to_frame()
sd['Deveation'] = sd - 100
sd.to_excel(writer, sheet_name='FTU_Utlization', header=['% FTU_Utlization', '% Deveation'])

# Monthly Hours Utilization per Resource
grp_hrs = df.groupby(['Month', 'Accomplished By'])
s = grp_hrs.apply(calculate_hrs_utlization)
sd = s.to_frame()
sd['Deveation'] = sd - 100
sd.to_excel(writer, sheet_name='Hrs_Utlization', header=['% Hrs_Utlization', '% Deveation'])

writer.save()
