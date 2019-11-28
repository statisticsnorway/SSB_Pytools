'''
# Functions for Data visualisation

Author: Simen Svenkerud
Updated: 2019.06.25

'''
import pandas as pd
import numpy as np
import os
import statsmodels.api as sm
import matplotlib.pyplot as plt
import datetime
import seaborn as sns
import math



def half_masked_corr_heatmap(dataframe, title=None, file=None):
    ''' 
    Required parameter: dataframe ... the reference pandas dataframe
    Optional parameters: title ... (string) chart title
                         file ... (String) path + filname if you want to save image
    '''
    plt.figure(figsize=(9,9))
    sns.set(font_scale=1)
    
    mask = np.zeros_like(dataframe.corr())
    mask[np.triu_indices_from(mask)]=True
    
    with sns.axes_style('white'):
        sns.heatmap(dataframe.corr(), mask=mask, annot=True, cmap='coolwarm')
        
    if title: plt.title(f'\n{title}\n', fontsize=18)
    plt.xlabel('') # optional in case you want an x-axis label
    plt.ylabel('') # optional in case you want a y-axis label
    if file: plt.savefig(file, bbox_inches='tight')
    plt.show()
    
    return

def corr_to_target(dataframe, target, title=None, file=None):
    '''
    Required parameters: dataframe ... the reference pandas dataframe
                        target ... (String) column name of the target variable
                        
    Optional parameters: title ... (string) chart title
                         file ... (String) path + filname if you want to save image
    '''
    plt.figure(figsize=(4,6))
    sns.set(font_scale =1)
    
    sns.heatmap(dataframe.corr()[[target]].sort_values(target,
                                                      ascending=False)[1:],
               annot=True,
               cmap='coolwarm')
    if title: plt.title(f'\n{title}\n', fontsize=18)
    plt.xlabel('') # optional in case you want an x-axis label
    plt.ylabel('') # optional in case you want a y-axis label
    if file: plt.savefig(file, bbox_inches='tight')
    plt.show();
    
    return

def gen_scatterplots(dataframe, target_column, list_of_columns, cols=1, file=None):
    '''
    Suptitle formatting adapted from Stackoverflow, Alexander McFarlane
    https://stackoverflow.com/questions/7066121/
            how-to-set-a-single-main-title-above-all-the-subplots-with-pyplot/35676071
            
    N-across scatterplots of each feature vs. target ...
    Required parameters: dataframe ... the reference pandas dataframe
                        target ... (String) column name of the target variable
                        
    Optional parameters: title ... (string) chart title
                         file ... (String) path + filname if you want to save image
    '''
    rows = math.ceil(len(list_of_columns)/cols)
    figwidth = 5 * cols
    figheight = 4 * rows
    
    fig, ax = plt.subplots(nrows=rows,
                          ncols=cols,
                          figsize =(figwidth, figheight))
    
    color_choices = ['blue', 'grey', 'goldenrod', 'r', 'black', 'darckorange','g']
    
    plt.subplots_adjust(wspace =0.3, hspace=0.3)
    ax = ax.ravel() #Ravel turns a matrix into a vector... easier to iterate
    
    for i, column in enumerate(list_of_columns):
        ax[i].scatter(dataframe[column],
                     dataframe[target_column],
                     c=color_choices[i%len(color_choices)],
                     alpha = 0.1)
        
        #Individual subplot titles, optional
        #ax[i].set_title(f'{column} vs. {target_column}', fontsize=18)
        ax[i].set_ylabel(f'{target_column}', fontsize=14)
        ax[i].set_xlabel(f'{column}',fontsize=14)
        
    fig.suptitle('\nEach Feature vs. Target Scatter Plots', size=24)
    fig.tight_layout()
    fig.subplots_adjust(bottom=0, top=0.88)
    if file: plt.savefig(file, bbox_inches='tight')
    plt.show();
    
    return

def gen_histograms(dataframe, cols=1, file=None):
    '''
    N-across Histograms of each variable in the dataframe ...
    Required parameters: dataframe ... the reference pandas dataframe
    
    Optional parameters: cols ... no. of subplot columns across fig; default = 1
                         file ... (String) path + filname if you want to save image
    '''
    rows = math.ceil(len(dataframe.columns)/cols)
    figwidth = 5 * cols
    figheight = 4 * rows
    
    fig, ax = plt.subplots(nrows=rows,
                          ncols=cols,
                          figsize =(figwidth, figheight))
    
    color_choices = ['blue', 'grey', 'goldenrod', 'r', 'black', 'darckorange','g']
    
    plt.subplots_adjust(wspace =0.3, hspace=0.3)
    ax = ax.ravel() #Ravel turns a matrix into a vector... easier to iterate
    
    for i, column in enumerate(dataframe.columns):
        ax[i].hist(dataframe[column],
                  c = color_choices[i % len(color_choices)],
                  alpha = 1)
        
        ax[i].set_title(f'{dataframe[column].name}', fontsize=18)
        ax[i].set_ylabel('Observations', fontsize=14)
        ax[i].set_xlabel('',fontsize=14)
        
    fig.suptitle('\nHistograms for All Variables in Dataframe', size=24)
    fig.tight_layout()
    fig.subplots_adjust(bottom=0, top=0.88)
    if file: plt.savefig(file, bbox_inches='tight')
    plt.show();
    
    return

def gen_boxplots(dataframe, cols=1, file=None):
    '''
    N-across boxplots of each variable in the dataframe ...
    Required parameters: dataframe ... the reference pandas dataframe
    
    Optional parameters: cols ... no. of subplot columns across fig; default = 1
                         file ... (String) path + filname if you want to save image
    '''
    rows = math.ceil(len(dataframe.columns)/cols)
    figwidth = 5 * cols
    figheight = 4 * rows
    
    fig, ax = plt.subplots(nrows=rows,
                          ncols=cols,
                          figsize =(figwidth, figheight))
    
    color_choices = ['blue', 'grey', 'goldenrod', 'r', 'black', 'darckorange','g']
    
    plt.subplots_adjust(wspace =0.3, hspace=0.3)
    ax = ax.ravel() #Ravel turns a matrix into a vector... easier to iterate
    
    for i, column in enumerate(dataframe.columns):
        ax[i].boxplot(dataframe[column])
        
        ax[i].set_title(f'{dataframe[column].name}', fontsize=18)
        ax[i].set_ylabel('', fontsize=14)
        ax[i].set_xlabel('',fontsize=14)
        ax[i].tick_params(labelbottom=False)
        
    fig.suptitle('\nBoxplots for All Variables in Dataframe', size=24)
    fig.tight_layout()
    fig.subplots_adjust(bottom=0, top=0.88)
    if file: plt.savefig(file, bbox_inches='tight')
    plt.show();
    
    return

def gen_linecharts(dataframe, cols=1, file=None):
    '''
    N-across Line Charts of each variable in the dataframe ...
    Required parameters: dataframe ... the reference pandas dataframe
    
    Optional parameters: cols ... no. of subplot columns across fig; default = 1
                         file ... (String) path + filname if you want to save image
    '''
    list_of_columns = list(dataframe.columns)
    rows = math.ceil(len(dataframe.columns)/cols)
    figwidth = 5 * cols
    figheight = 4 * rows
    
    fig, ax = plt.subplots(nrows=rows,
                          ncols=cols,
                          figsize =(figwidth, figheight))
    
    color_choices = ['blue', 'grey', 'goldenrod', 'r', 'black', 'darckorange','g']
    
    plt.subplots_adjust(wspace =0.3, hspace=0.3)
    ax = ax.ravel() #Ravel turns a matrix into a vector... easier to iterate
    
    for i, column in enumerate(list_of_columns):
        ax[i].plot(dataframe[column],
                  color=color_choices[i % len(color_choices)])
        
        ax[i].set_title(f'{column}', fontsize=18)
        ax[i].set_ylabel(f'{column}', fontsize=14)
        ax[i].set_xlabel('Time',fontsize=14)
    
    fig.suptitle('\nLine Graphs for All Variables in Dataframe', size=24)
    fig.tight_layout()
    fig.subplots_adjust(bottom=0, top=0.88)
    if file: plt.savefig(file, bbox_inches='tight')
    plt.show();
    
    return

def gen_linecharts_rolling(dataframe, roll_num, cols=1, file=None):
    '''
    N-across Rolling Avg Line Charts of each variable in the dataframe ...
    Required parameters: dataframe ... the reference pandas dataframe
                         roll_num ... periods over which to calc rolling avg
    
    Optional parameters: cols ... no. of subplot columns across fig; default = 1
                         file ... (String) path + filname if you want to save image
    '''
    list_of_columns = list(dataframe.columns)
    rows = math.ceil(len(dataframe.columns)/cols)
    figwidth = 5 * cols
    figheight = 4 * rows
    
    dataframe = dataframe.rolling(roll_num).mean()
    
    fig, ax = plt.subplots(nrows=rows,
                          ncols=cols,
                          figsize =(figwidth, figheight))
    
    color_choices = ['blue', 'grey', 'goldenrod', 'r', 'black', 'darckorange','g']
    
    plt.subplots_adjust(wspace =0.3, hspace=0.3)
    ax = ax.ravel() #Ravel turns a matrix into a vector... easier to iterate
    
    for i, column in enumerate(list_of_columns):
        ax[i].plot(dataframe[column],
                  color=color_choices[i % len(color_choices)])
        
        ax[i].set_title(f'{column}', fontsize=18)
        ax[i].set_ylabel(f'{column}', fontsize=14)
        ax[i].set_xlabel('Time',fontsize=14)
    
    fig.suptitle('\nRolling Avg. Line Graphs (all vars)', size=24)
    fig.tight_layout()
    fig.subplots_adjust(bottom=0, top=0.88)
    if file: plt.savefig(file, bbox_inches='tight')
    plt.show();
    
    return

def ssb_barplot_simple(plot,group):
    height = np.arange(len(group))
    plot = plot

    plt.figure(figsize=(20,10))
    plt.bar(height, plot, color='green')
    plt.xticks(height, group)
    plt.show()
    
    return

def ssb_barplot_complex(plot, group, figsize=(20,10), scale='log', ylim=(0,100000)):
    height = np.arange(len(group))
    plot = plot

    plt.figure(figsize=figsize)
    plt.bar(height, plot, color='green')
    plt.yscale(scale)
    plt.xticks(height, group)
    plt.ylim(ylim)
    plt.show()
    
    return