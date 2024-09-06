from fishmlserv.curl import get
from fishmlserv.model.manager import run_prediction
from fishmlserv.data import add_prediction_column, add_prediction_column_api


import pandas as pd

def test_get():
    r = get(10, 10)
    assert r == "빙어"


def test_run_prediction():
    r = run_prediction(10, 10, k=1)
    assert r == "빙어"

def test_add_prediction_column():
    result_df = add_prediction_column()
    assert isinstance(result_df, pd.DataFrame)
    assert 'k1' in result_df.columns

    result_df.to_parquet('result_df.parquet')

def test_add_prediction_column_api():
    result_df = add_prediction_column_api()
    assert isinstance(result_df, pd.DataFrame)
    assert 'k1' in result_df.columns

    result_df.to_parquet('result_df_api.parquet')

