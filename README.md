# 3D-PCA-plot
###### Developer: Siavash Salek Ardestani (May-2022)
## 1. A short description
* The 3D-PCA-plot is a custom-made python script to plot PCA results in Linux.
## 1.2 For downloading and getting permission 3D-PCA-plot, please use:
``` git clone https://github.com/Siavash-cloud/3D-PCA-plot.git```
###### then run:
``` 
cd 3D-PCA-plot
chmod 775 3D-PCA-plot.py
```
## 1.2 Dependencies in python (>2.7)
* seaborn
* numpy
* pandas
* matplotlib
* pylab
* argparse
* If you do not have each of the above-mentioned libraries in your python, then you can install these through:
```
pip install seaborn
pip install numpy
pip install pandas
pip install matplotlib
pip install pylab
pip install argparse
```
## 2. Inputs, usage and options
#### 2.1 Inputs
The examples of inputs were deposited here (you can see: pink.eigenvalue and plink.eigenvec)
* In pink.eigenvalue:
1th column is population ID,
2th column is individual ID,
3th column is PC1,
4th column is PC2 and
5th column is PC3
* In pink.eigenvalue:
1th column includes explained variation by PC1, PC2 and PC3
#### 2.2 Usage
```
python 3D-PCA-plot.py --evec plink.eigenvec --eval plink.eigenval --s 70 --x 15 --y 10 --c brg --o sia
```
#### 2.3 Options
* --evec is the eigenvec file (required option)
* --eval is the eigenval file (required option)
* --s is the size of scatter points (optional, default=10)
* --x is the width of figure (optional, default=10)
* --y is the height of figure (optional, default=10)
* --c is colormaps: please see https://matplotlib.org/stable/tutorials/colors/colormaps.html, to choose your preferred color maps (optional, default=brg)
* --o is the output file prefix (required option)
