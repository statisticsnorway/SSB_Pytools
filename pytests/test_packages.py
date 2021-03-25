import pytest
import pandas as pd
import numpy as np

def test_pandas_numpy_installed():
    df_test = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
    assert len(df_test) > 0 & isinstance(df_test, pd.DataFrame)    
