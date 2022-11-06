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

# ready to plot
fig, ax = plt.subplots()
fig.suptitle('YouGov Westminster voting intention tracker', fontsize = 20, fontweight = 'bold')

for count, column in enumerate(df.columns):
    if count != 0:
        ax.plot(df.iloc[:,0], df[column], color = colors[count], label = f'{column}: {df[column].iloc[-1]}%')

# number of x labels is given by 'step'
step = 10
ax.set_xticks(ax.get_xticks()[::step])
ax.set_xticklabels(date_labels[::step])

# removes frames from the plot (with one exeption: bottom)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

led = dt.datetime.strptime(df.iloc[:,0].tail(1).item(), '%d/%m/%Y')
le = f'{led.strftime("%d")} {led.strftime("%B")} {led.strftime("%Y")} '

ax.set_title(f'Source: https://yougov.co.uk/     Last entry: {le}\n')
ax.legend(loc = 'upper center', ncol = 4, shadow = True)
ax.grid(axis='y')

plt.show()
