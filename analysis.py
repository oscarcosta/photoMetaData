import pandas as pd
import sys
import glob
import os
import matplotlib.pyplot as plt

directory = sys.argv[1]  # input directory
input_files = glob.glob(os.path.join(directory, "*.csv"))

li = []
for filename in input_files:
    frame = pd.read_csv(filename, index_col=None, header=0)  # read data inferring column name from first row
    li.append(frame)
df = pd.concat(li, axis=0, ignore_index=True)

focal_length = df.groupby(['FocalLength'])['FocalLength'].count()
ax = focal_length.plot.bar()

plt.show()
