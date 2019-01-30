import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib import style
import pandas as pd

df = pd.read_excel('C:\\AA_FTU_Data_Analysis\\aa_ftu.xlsx')
df['Accomplished By'].fillna('Unknown', inplace=True)
df['Time Spent (hrs)'] = df['Time Spent (hrs)'].astype('int')
df['Month'] = df['Month'].astype('str')


# Method to calculate the total FTU for the group
def calculate_ftu(group):
    print(type(group))
    print(group[8], group[7])
    # return group['FTU - Computed Value'].sum()


grp_Business_Group = df.groupby('Business Group')
ot = grp_Business_Group.get_group('Operations')
print(type(ot))
ot.apply(calculate_ftu, axis=1)

# style.use('ggplot')
#
# x = [1, 2, 3]
# y = [0.1, 0.2, 0.3]
#
# fig = plt.figure()
#
# ax1 = plt.subplot2grid((2, 2), (0, 0), rowspan=1, colspan=2)
# ax2 = plt.subplot2grid((2, 2), (1, 0), rowspan=1, colspan=1)
# ax2 = plt.subplot2grid((2, 2), (1, 1), rowspan=1, colspan=1)




plt.show()



