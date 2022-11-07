import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import glob

# we are assuming there is only one file with 'csv' extension in folder
# pandas library was used to load the data
file_types = "*.csv"    
file_name = glob.glob(file_types)[0]
df = pd.read_csv(file_name)

# need to assing the colour for each party
# note: 'none' stands for first column, i.e, date
# rest is self explanatory
colors = ['none', 'blue', 'red' , 'orange', 'yellow', 'purple', 'cyan', 'green', 'black']
date_labels_row = [dt.datetime.strptime(entry, '%d/%m/%Y') for entry in df.iloc[:,0]]
date_labels = [date_label.strftime("%B") + "\n" +  date_label.strftime("%Y") for date_label in date_labels_row]

# --------------------------------------- FIGURE INIT ------------------------------------------------------
fig = plt.figure()
fig.suptitle('YouGov Westminster voting intention tracker', fontsize = 20, fontweight = 'bold')
fig.patch.set_facecolor('#e0e0eb')

led = dt.datetime.strptime(df.iloc[:,0].tail(1).item(), '%d/%m/%Y')
le = f'{led.strftime("%d")} {led.strftime("%B")} {led.strftime("%Y")} '

src="Source: https://yougov.co.uk/"
plt.figtext(0.98, 0.02, src, wrap=True, horizontalalignment='right', fontsize=12)
plt.figtext(0.02, 0.02, f'Last entry: {le}', wrap =True, horizontalalignment='left', fontsize=12)

gs = fig.add_gridspec(nrows=2, ncols=2)


# --------------------------------------- TOP BAR PLOT ------------------------------------------------------
def app_col(res):
    if res < 0:
        return 'blue'
    else:
        return 'red'

size = len(date_labels) 
con = df.iloc[-size:,1].to_list()
lab = df.iloc[-size:,2].to_list()
res = [lab[i] - con[i] for i in range(size)]

ax1 = fig.add_subplot(gs[0, :])
ax1.set_facecolor('#ebe0e0')
ax1.set_title('Difference between two major parties')

for i in range(size):
    col = app_col(res[i])
    ax1.bar(i, res[i], width=0.7, color = col,)

step = 10
print(ax1.get_xticks())

# ax1.set_xticks(ax1.get_xticks()[::step])
# ax1.set_xticklabels(date_labels[::step])

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)

ax1.grid(axis='y')


# --------------------------------------- BOTTOM LEFT BOXPLOT -------------------------------------------------
box_data = [df.iloc[:,i] for i in range(1,9)]
box_names = [column for column in df.columns if column != 'X.1']
box_colors = ['blue', 'red' , 'orange', 'yellow', 'purple', 'cyan', 'green', 'black']

ax21 = fig.add_subplot(gs[1,0])
ax21.set_facecolor('#f5f5f0')
box = ax21.boxplot(x = box_data, labels=box_names, notch=True, patch_artist=True, flierprops= {'marker' : "+"} )

for patch, color in zip(box['boxes'], box_colors):
    patch.set_facecolor(color)

ax21.set_title('Boxplot comparison')
ax21.spines['top'].set_visible(False)
ax21.spines['right'].set_visible(False)
ax21.spines['left'].set_visible(False)
ax21.grid(axis='y')


# ---------------------------------------BOTTOM RIGHT PIE CHART ------------------------------------------------
pie_data = [df.iloc[:,i].to_list()[-1] for i in range(1,9)]
my_explode = [0.1, 0.1, 0, 0, 0, 0, 0 ,0]

ax22 = fig.add_subplot(gs[1,1])
ax22.pie(x = pie_data, labels=box_names, autopct='%1.0f%%', colors=box_colors, shadow=True, explode=my_explode)


# --------------------------------------- FIG DISPLAY --------------------------------------------------------
plt.show()