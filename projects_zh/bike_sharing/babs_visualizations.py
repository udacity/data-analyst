import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def filter_data(data, condition):
    """
    Remove elements that do not match the condition provided.
    Takes a data list as input and returns a filtered list.
    Conditions should be a list of strings of the following format:
      '<field> <op> <value>'
    where the following operations are valid: >, <, >=, <=, ==, !=
    
    Example: ["duration < 15", "start_city == 'San Francisco'"]
    """

    # Only want to split on first two spaces separating field from operator and
    # operator from value: spaces within value should be retained.
    field, op, value = condition.split(" ", 2)
    
    # check if field is valid
    if field not in data.columns.values :
        raise Exception("'{}' is not a feature of the dataframe. Did you spell something wrong?".format(field))

    # convert value into number or strip excess quotes if string
    try:
        value = float(value)
    except:
        value = value.strip("\'\"")

    # get booleans for filtering
    if op == ">":
        matches = data[field] > value
    elif op == "<":
        matches = data[field] < value
    elif op == ">=":
        matches = data[field] >= value
    elif op == "<=":
        matches = data[field] <= value
    elif op == "==":
        matches = data[field] == value
    elif op == "!=":
        matches = data[field] != value
    else: # catch invalid operation codes
        raise Exception("Invalid comparison operator. Only >, <, >=, <=, ==, != allowed.")
    
    # filter data and outcomes
    data = data[matches].reset_index(drop = True)
    return data

def usage_stats(data, filters = [], verbose = True):
    """
    Report number of trips and average trip duration for data points that meet
    specified filtering criteria.
    """

    n_data_all = data.shape[0]

    # Apply filters to data
    for condition in filters:
        data = filter_data(data, condition)

    # Compute number of data points that met the filter criteria.
    n_data = data.shape[0]

    # Compute statistics for trip durations.
    duration_mean = data['duration'].mean()
    duration_qtiles = data['duration'].quantile([.25, .5, .75]).as_matrix()
    
    # Report computed statistics if verbosity is set to True (default).
    if verbose:
        if filters:
            print('There are {:d} data points ({:.2f}%) matching the filter criteria.'.format(n_data, 100. * n_data / n_data_all))
        else:
            print('There are {:d} data points in the dataset.'.format(n_data))

        print('The average duration of trips is {:.2f} minutes.'.format(duration_mean))
        print('The median trip duration is {:.2f} minutes.'.format(duration_qtiles[1]))
        print('25% of trips are shorter than {:.2f} minutes.'.format(duration_qtiles[0]))
        print('25% of trips are longer than {:.2f} minutes.'.format(duration_qtiles[2]))

    # Return three-number summary
    return duration_qtiles


def usage_plot(data, key = '', filters = [], **kwargs):
    """
    Plot number of trips, given a feature of interest and any number of filters
    (including no filters). Function takes a number of optional arguments for
    plotting data on continuously-valued variables:
      - n_bins: number of bars (default = 10)
      - bin_width: width of each bar (default divides the range of the data by
        number of bins). "n_bins" and "bin_width" cannot be used simultaneously.
      - boundary: specifies where one of the bar edges will be placed; other
        bar edges will be placed around that value (may result in an additional
        bar being plotted). Can be used with "n_bins" and "bin_width".
    """
    
    # Check that the key exists
    if not key:
        raise Exception("No key has been provided. Make sure you provide a variable on which to plot the data.")
    if key not in data.columns.values :
        raise Exception("'{}' is not a feature of the dataframe. Did you spell something wrong?".format(key))

    # Apply filters to data
    for condition in filters:
        data = filter_data(data, condition)

    # Create plotting figure
    plt.figure(figsize=(8,6))

    if isinstance(data[key][0] , str): # Categorical features
        # For strings, collect unique strings and then count number of
        # outcomes for survival and non-survival.
        
        # Summarize dataframe to get counts in each group
        data['count'] = 1
        data = data.groupby(key, as_index = False).count()
        
        levels = data[key].unique()
        n_levels = len(levels)
        bar_width = 0.8
        
        for i in range(n_levels):
            trips_bar = plt.bar(i - bar_width/2, data.loc[i]['count'], width = bar_width)
        
        # add labels to ticks for each group of bars.
        plt.xticks(range(n_levels), levels)
        
    else: # Numeric features
        # For numbers, divide the range of data into bins and count
        # number of outcomes for survival and non-survival in each bin.
        
        # Set up bin boundaries for plotting
        if kwargs and 'n_bins' in kwargs and 'bin_width' in kwargs:
            raise Exception("Arguments 'n_bins' and 'bin_width' cannot be used simultaneously.")

        min_value = data[key].min()
        max_value = data[key].max()
        value_range = max_value - min_value
        n_bins = 10
        bin_width = float(value_range) / n_bins

        if kwargs and 'n_bins' in kwargs:
            n_bins = int(kwargs['n_bins'])
            bin_width = float(value_range) / n_bins
        elif kwargs and 'bin_width' in kwargs:
            bin_width = kwargs['bin_width']
            n_bins = int(np.ceil(float(value_range) / bin_width))
        
        if kwargs and 'boundary' in kwargs:
            bound_factor = np.floor(( min_value - kwargs['boundary'] ) / bin_width)
            min_value = kwargs['boundary'] + bound_factor * bin_width
            if min_value + n_bins * bin_width <= max_value:
                n_bins += 1

        bins = [i*bin_width + min_value for i in range(n_bins+1)]
        
        # plot the data
        plt.hist(data[key], bins = bins)

    # Common attributes for plot formatting
    key_name = ' '.join([x.capitalize() for x in key.split('_')])
    plt.xlabel(key_name)
    plt.ylabel("Number of Trips")
    plt.title("Number of Trips by {:s}".format(key_name))
    plt.show()