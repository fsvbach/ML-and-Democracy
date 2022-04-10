import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from matplotlib.patches import Ellipse
import matplotlib
import numpy as np
import pandas as pd
import textwrap

def embedFlags(embedding, ax=None):
    if not ax:
        ax = plt.gca()
        
    for label, data in embedding.groupby(level=0):
        X, Y, s = data['x'], data['y'], data['sizes']
        ax.scatter(X, Y,label=label, s=s/100)
        flag = plt.imread(f'flags/{label}.png')
        plotImages(X, Y, flag, s, ax)
   
def plotImages(x, y, image, sizes, ax=None):
    ax = ax or plt.gca()

    for xi, yi, zm in zip(x,y, sizes):
        im = OffsetImage(image, zoom=zm/ax.figure.dpi)
        im.image.axes = ax

        ab = AnnotationBbox(im, (xi,yi), frameon=False, pad=0.0, )
        ax.add_artist(ab)

def code2name():
    labels = pd.read_csv('Experiments/Visualization/Images/countries.csv',
                index_col=1)
    return labels['English short name lower case'].to_dict()

def wrap_labels(ax, width, break_long_words=False):
    labels = []
    for label in ax.get_yticklabels():
        text = label.get_text()
        labels.append(textwrap.fill(text, width=width,
                      break_long_words=break_long_words))
    ax.set_yticklabels(labels, rotation=0)
