#!/usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import print_function

import matplotlib.pyplot as plt
import numpy as np

def get_data(hist_dict):
    """Convert a histogram dictionary {'x': y} to a sorted list of tuples"""
    sorted_list=hist_dict.items()
    sorted_list.sort()
    return sorted_list

def round_up_ymax(value):
    if value < 1:
        return 1.0
    else:
        temp_max_index = len(str(value))
        temp_max_str = "1e%i" % temp_max_index
        temp_max = float(temp_max_str) 
        half_temp = temp_max /2
        if value <= half_temp * 0.9:
            return half_temp
        else:
            return temp_max

def plot_hist(hist_dict, x_item_label, frequency_label):
    """Plot a histogram"""
    fig = plt.figure()
    ax = fig.add_subplot(111)

    sorted_data_list = get_data(hist_dict)
    # the x locations for the groups
    bar_width = 0.8

    x_labels = []
    y_data = []

    for x,y in sorted_data_list:
        x_labels.append(x)
        
        N = len(x_labels)      
        ind = np.arange(N)      # x locations for the groups  


        y_data.append(y)

    y_array = np.array(y_data)

    rects = ax.bar(ind,y_array, bar_width, align = 'center')

    ax.set_xlabel(x_item_label)
    ax.set_ylabel(frequency_label)
    ax.set_xticks(ind)
    if len(str(x_labels[-1])) < 3:
        ax.set_xticklabels(x_labels)
    else:
        ax.set_xticklabels(x_labels, rotation = 17)


    y_max = max(y_array)/0.95 

    plt.axis([0,N+1,0,y_max])
    plt.show()









