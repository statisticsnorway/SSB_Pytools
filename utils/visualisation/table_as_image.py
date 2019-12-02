

def longitude_matrix(df, group_var, keep_vars, sort_vars, pred_var, long_length=None):
    """Create padded matrix from longitudinal data.
    Keyword arguments:
    df -- Pandas dataframe containing longitudinal data
    group_var -- Name of variable identifying the groups (e.g. subject, person, customer)
    keep_vars -- Name of columns to keep. Must all be numeric, as they end up in np.matrix
    sort_vars -- Name of variables (including group_var) that sets ordering (e.g. transaction date)
    long_length -- Length of matrix. Defaults to None and set to longest occurence at runtime.
    pred_var -- Name of variable to be predicted
    """
    dfx = df.sort_values(sort_vars)
    dfg = df.groupby(group_var)
    group_ids = list(set(dfx[group_var]))
    x = [ dfg.get_group(g)[keep_vars].values for g in group_ids ]
    y = [ max(dfg.get_group(g)[pred_var].values) for g in group_ids]
    
    print(x[4])
    long_length_calc = max([m.shape[0] for m in x])
    if long_length is None:
        long_length = long_length_calc
    else:
        if long_length<long_length_calc:
            raise ValueError('long_length can not be shorter than max length of group')
    z = np.zeros( (len(x), long_length, len(keep_vars), 1) )
    for i, e in enumerate(x):
        padding = long_length-e.shape[0] # is zero for at least 1 group, but that's OK.
        e = np.pad(e, ((0, padding),(0, 0)), mode='edge')
        z[i, 0:e.shape[0], 0:e.shape[1], 0 ] = e
    return(z, np.asarray(y))