print('|------------------------------------------------------|')
print('| *          |                             |   *       |')
print('|      *     |         3D PCA plot         |      *    |')
print('|            |                             |  *        |')
print('|  *         |   Siavash Salek Ardestani   |       *   |')
print('|          * |            Contact:         |    *      |')
print('|   *    *   |     siasia6650@gmail.com    |*          |')
print('|      *     |                             |       *   |')
print('|------------------------------------------------------|')
import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import savefig
import argparse
P = argparse.ArgumentParser()
P.add_argument('--evec',help='eigenvec file', required=True)
P.add_argument('--eval',help='eigenval file', required=True)
P.add_argument('--s',help='Size of scatter points', type=int,required=False,default=10)
P.add_argument('--c',help='Colormaps: please see https://matplotlib.org/stable/tutorials/colors/colormaps.html, to choose your preferred color maps', type=str,required=False,default='brg')
P.add_argument('--x',help='width of figure', type=int,required=False,default=10)
P.add_argument('--y',help='height of figure', type=int,required=False,default=10)
P.add_argument('--o',help='Output files prefix', type=str, required=True)
args = P.parse_args()
####################################################################
data = pd.read_csv(args.evec,delimiter=r"\s+",header=None)
eigenval = pd.read_csv(args.eval,delimiter=r"\s+",header=None,nrows=3).round(2)
df = pd.DataFrame([('PC1'), ('PC2'), ('PC3')])
df2 = pd.DataFrame([['Breed'], ['ID']])
eigenval= (df + '('+ eigenval.astype(str)+'%)').astype(str)
keep_col1 = [0,1,2,3,4]
PCA = data[keep_col1]
header=df2.append(eigenval ,ignore_index=True)
PCA = PCA.rename(columns=header[0])
####################################################################
markers = ["d",",","o","D","v","H",0,">","1","2","3","4","8","s","p","P","*","h","^","+","x","X","D",".","|","_","<",1,2,3,4,5,6,7,8,9,10,11]
colors = np.random.rand(90)
c = plt.cm.gist_rainbow(colors)
size = args.s
cp=args.c
fig = plt.figure(figsize=(args.x, args.y))
ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)
PCA['Breed']=pd.Categorical(PCA['Breed'])
labels = np.unique(PCA['Breed'])
palette = sns.color_palette(cp, len(labels))
for label, color,label,m in zip(labels, palette,labels,markers):
    PCA1 = PCA[PCA['Breed'] == label]
    ax.scatter(PCA1.iloc[:, 2:3],  PCA1.iloc[:, 3:4], PCA1.iloc[:, 4:5],
               s=size, color=color, alpha=1, edgecolor='k',label=label, marker=m)


ax.set_xlabel(PCA.columns[2])
ax.set_ylabel(PCA.columns[3])
ax.set_zlabel(PCA.columns[4])
plt.legend()
ax.view_init(20, 65)
plt.savefig(args.o+'3dPCA.tiff', dpi=400,format="png")
plt.show()
