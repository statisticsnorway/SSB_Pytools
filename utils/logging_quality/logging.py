

def ColumnComparison (data_set1, data_set2,)
    '''
    Function to compare the columns in two data setts
    '''
    a = set(data_set1.columns)
    b = set(data_set2.columns)
    if (a & b):    
        print('These Datasets have the following common columns:')
        for elem in (a & b):
            print('* ', elem)

    if (a-b):
        print('These columns exist only in the first dataset:')
        for elem in (a-b):
            print('* ', elem)

    if (b-a):
        print('These columns exist only in the second datasett:')
        for elem in (b - a):
            print('* ', elem)