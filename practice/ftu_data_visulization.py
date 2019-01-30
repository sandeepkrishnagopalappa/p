import pandas as pd
import matplotlib.pyplot as plt

x_tick_rotation = 90
x_tick_label_size = 6.5
bar_transparency = 0.5
bar_width = 0.3
x_limit = [0, 42000]

# FTU Trend Project wise
df = pd.read_excel('C:\\AA_FTU_Data_Analysis\\Data.xlsx', sheet_name='Project_FTU')
x_projects = df['Project Name'].str[3:]
y_ftu = df['FTU']
fig = plt.figure()
ax = plt.subplot2grid((1, 1), (0, 0), colspan=1, rowspan=1)
ax.set_ylim(x_limit)
ax.set_xlabel('Projects')
ax.set_ylabel('FTU')
ax.set_title('Project FTU Trend Year-2018')
for tick in ax.get_xticklabels():
    tick.set_rotation(x_tick_rotation)
    tick.set_fontsize(x_tick_label_size)

for x, y in zip(x_projects, y_ftu):
    if y < 2500:
        ax.bar(x, y, color='red', alpha=bar_transparency)
    else:
        ax.bar(x, y, color='blue', alpha=bar_transparency)
ax.grid(alpha=bar_transparency)

# ===========================================================================================
# FTU Trend Manual Project wise
df = pd.read_excel('C:\\AA_FTU_Data_Analysis\\Data.xlsx', sheet_name='Project_Manual_FTU')
x_projects = df['Project Name'].str[3:]
y_ftu = df['Manual_FTU']
fig = plt.figure()
mx1 = plt.subplot2grid((2, 1), (0, 0), rowspan=1, colspan=1)
mx1.set_ylim(x_limit)
mx1.set_xlabel('Projects')
mx1.set_ylabel('Manual FTU')
mx1.set_title('Manual vs Automation FTU Trend Year-2018')
for tick in mx1.get_xticklabels():
    tick.set_rotation(x_tick_rotation)
    tick.set_fontsize(x_tick_label_size)
mx1.bar(x_projects, y_ftu, color='blue', alpha=bar_transparency, label='FTU')
mx1.grid(alpha=bar_transparency)
mx1.legend()


# FTU Trend Automation Project wise
df = pd.read_excel('C:\\AA_FTU_Data_Analysis\\Data.xlsx', sheet_name='Project_Automation_FTU')
x_projects = df['Project Name'].str[3:]
y_ftu = df['Automation_FTU']
mx2 = plt.subplot2grid((2, 1), (1, 0), rowspan=1, colspan=1)
mx2.set_ylim([0, 20000])
mx2.set_xlabel('Projects')
mx2.set_ylabel('Automation FTU')
for tick in mx2.get_xticklabels():
    tick.set_rotation(x_tick_rotation)
    tick.set_fontsize(x_tick_label_size)
mx2.bar(x_projects, y_ftu, color='blue', alpha=bar_transparency, label='FTU')
mx2.grid(alpha=bar_transparency)
mx2.legend()

# ===================================FTU=============================================
# FTU and Hours clocked- Approach
df = pd.read_excel('C:\\AA_FTU_Data_Analysis\\Data.xlsx', sheet_name='FTU_Approach', index_col='Approach')
a = df.loc['Automated':'Manual']

automation_mask = a.drop_duplicates('Task Type')
auto_total_ftu = automation_mask['FTU'].sum()
auto_ftu_develop = automation_mask[automation_mask['Task Type'] == 'Develop']['FTU']
auto_ftu_develop = auto_ftu_develop.iloc[0]
auto_ftu_execution = automation_mask[automation_mask['Task Type'] == 'Test Execution']['FTU']
auto_ftu_execution = auto_ftu_execution.iloc[0]
auto_ftu_misc = auto_total_ftu - (auto_ftu_develop + auto_ftu_execution)

manual_mask = df.loc['Manual':]
manual_total_ftu = manual_mask['FTU'].sum()
manual_ftu_develop = manual_mask[manual_mask['Task Type'] == 'Develop']['FTU']
manual_ftu_develop = manual_ftu_develop.iloc[0]
manual_ftu_execution = manual_mask[manual_mask['Task Type'] == 'Test Execution']['FTU']
manual_ftu_execution = manual_ftu_execution.iloc[0]
manual_ftu_misc = manual_total_ftu - (manual_ftu_develop + manual_ftu_execution)

labels = ['Develop', 'Execution', 'Misc']
auto = [auto_ftu_develop, auto_ftu_execution, auto_ftu_misc]
manual = [manual_ftu_develop, manual_ftu_execution, manual_ftu_misc]
explode = (0.02, 0.02, 0)

fig = plt.figure()
ax = plt.subplot2grid((2, 2), (0, 0), rowspan=1, colspan=1)
ax.pie(auto, labels=labels, explode=explode, autopct='%1.1f%%', shadow=True, radius=1.2)
ax.set_title('FTU- Automation Approach', fontsize=8)
for text in ax.texts:
    text.set_fontsize(8)

ay = plt.subplot2grid((2, 2), (0, 1), rowspan=1, colspan=1)
ay.pie(manual, labels=labels, explode=explode, autopct='%1.1f%%', shadow=True, radius=1.2)
ay.set_title('FTU- Manual Approach', fontsize=8)
for text in ay.texts:
    text.set_fontsize(8)

# ************************* HRS ********************************************
df = pd.read_excel('C:\\AA_FTU_Data_Analysis\\Data.xlsx', sheet_name='Time_Approach', index_col='Approach')
a = df.loc['Automated':'Manual']
automation_mask = a.drop_duplicates('Task Type')
auto_total_hrs = automation_mask['Hours'].sum()
auto_hrs_develop = automation_mask[automation_mask['Task Type'] == 'Develop']['Hours']
auto_hrs_develop = auto_hrs_develop.iloc[0]
auto_hrs_execution = automation_mask[automation_mask['Task Type'] == 'Test Execution']['Hours']
auto_hrs_execution = auto_hrs_execution.iloc[0]
auto_hrs_misc = auto_total_hrs - (auto_hrs_develop + auto_hrs_execution)

manual_mask = df.loc['Manual':]
manual_total_hrs = manual_mask['Hours'].sum()
manual_hrs_develop = manual_mask[manual_mask['Task Type'] == 'Develop']['Hours']
manual_hrs_develop = manual_hrs_develop.iloc[0]
manual_hrs_execution = manual_mask[manual_mask['Task Type'] == 'Test Execution']['Hours']
manual_hrs_execution = manual_hrs_execution.iloc[0]
manual_hrs_misc = manual_total_hrs - (manual_hrs_develop + manual_hrs_execution)

labels = ['Develop', 'Execution', 'Misc']
auto = [auto_hrs_develop, auto_hrs_execution, auto_hrs_misc]
manual = [manual_hrs_develop, manual_hrs_execution, manual_hrs_misc]
explode = (0.02, 0.02, 0)

bx = plt.subplot2grid((2, 2), (1, 0), rowspan=1, colspan=1)
bx.pie(auto, labels=labels, explode=explode, autopct='%1.1f%%', shadow=True, radius=1.2)
bx.set_title('Hrs- Automation Approach', fontsize=8)
for text in bx.texts:
    text.set_fontsize(8)

by = plt.subplot2grid((2, 2), (1, 1), rowspan=1, colspan=1)
by.pie(manual, labels=labels, explode=explode, autopct='%1.1f%%', shadow=True, radius=1.2)
by.set_title('Hrs- Manual Approach', fontsize=8)
for text in by.texts:
    text.set_fontsize(8)

# ===========================SUMMARY================================================
# Total Automation vs Manual FTU
fig = plt.figure()
az = plt.subplot2grid((2, 2), (0, 0), rowspan=1, colspan=1)
az.pie([auto_total_ftu, manual_total_ftu], labels=['Automation ', 'Manual'], autopct='%1.1f%%', shadow=True , radius=1.2, startangle=90)
az.set_title('FTU- Automation vs Manual', fontsize=8)
for text in az.texts:
    text.set_fontsize(8)

# Total Hours Automation vs Manual
ay = plt.subplot2grid((2, 2), (0, 1), rowspan=1, colspan=1)
ay.pie([auto_total_hrs, manual_total_hrs], labels=['Automation ', 'Manual'], autopct='%1.1f%%', shadow=True, radius=1.2, startangle=90)
ay.set_title('Hrs- Automation vs Manual', fontsize=8)
for text in ay.texts:
    text.set_fontsize(8)
# ========================== TOP 4 PROJECTS FTU CONTRIBUTION- MANUAL=============================
df = pd.read_excel('C:\\AA_FTU_Data_Analysis\\Data.xlsx', sheet_name='Project_Manual_FTU', index_col='Project Name')
n_largest = df['Manual_FTU'].nlargest(5)
manual_ftu = list(n_largest)
others_manual_ftu = (df['Manual_FTU'].sum()) - (n_largest.sum())
manual_ftu.append(others_manual_ftu)
manual_projects = list(n_largest.index)
manual_projects.append('OTHERS')

cx = plt.subplot2grid((2, 2), (1, 0), colspan=1, rowspan=1)
cx.pie(manual_ftu, labels=manual_projects, autopct='%1.1f%%', shadow=True, radius=1.2, startangle=90)
cx.set_title('TOP 5 PROJECTS FTU CONTRIBUTION- MANUAL', fontsize=8)
for text in cx.texts:
    text.set_fontsize(8)
# ========================== TOP 4 PROJECTS  FTU CONTRIBUTION- AUTOMATION=============================

df = pd.read_excel('C:\\AA_FTU_Data_Analysis\\Data.xlsx', sheet_name='Project_Automation_FTU', index_col='Project Name')
n_largest = df['Automation_FTU'].nlargest(5)
automation_ftu = list(n_largest)
others_automation_ftu = (df['Automation_FTU'].sum()) - (n_largest.sum())
automation_ftu.append(others_automation_ftu)
automation_projects = list(n_largest.index)
automation_projects.append('OTHERS')

dx = plt.subplot2grid((2, 2), (1, 1), colspan=1, rowspan=1)
dx.pie(automation_ftu, labels=automation_projects, autopct='%1.1f%%', shadow=True, radius=1.2, startangle=90)
dx.set_title('TOP 5 PROJECTS FTU CONTRIBUTION- AUTOMATION', fontsize=8)
for text in dx.texts:
    text.set_fontsize(8)
# =========================================================================================================
# Monthly FTU Trend
df = pd.read_excel('C:\\AA_FTU_Data_Analysis\\Data.xlsx', sheet_name='Monthly_FTU_Trend')
fig = plt.figure()
az = plt.subplot2grid((1, 1), (0, 0), rowspan=1, colspan=1)
x_month = df['Month']
y_ftu = df['FTU']
az.set_title('Monthly FTU Trend Year-2018')
az.plot(x_month, y_ftu, linewidth=2, label='Monthly Trend')
az.set_xlabel('Month')
az.set_ylabel('FTU')
# =========================================================================================================
# Monthly FTU Trend - Operations
df = pd.read_excel('C:\\AA_FTU_Data_Analysis\\Data.xlsx', sheet_name='FTU_Trend_OT')
x_month = df['Month']
y_ftu = df['FTU']
az.plot(x_month, y_ftu, linewidth=2, label='Monthly Trend- OT')
# =========================================================================================================
# Monthly FTU Trend - Customer Technology
df = pd.read_excel('C:\\AA_FTU_Data_Analysis\\Data.xlsx', sheet_name='FTU_Trend_CT')
x_month = df['Month']
y_ftu = df['FTU']
az.plot(x_month, y_ftu, linewidth=2, label='Monthly Trend- CT')
az.legend()
plt.show()
# =========================================================================================================


