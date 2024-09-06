import pandas as pd
from fishmlserv.model.manager import run_prediction
from tqdm import tqdm
from fishmlserv.curl import get

def add_prediction_column(csv_file_path='/home/diginori/code/fishmlserv/note/fish_test_data_100k.csv'):
    """
    CSV 파일의 데이터를 읽어와 각 행에 대한 예측 결과를 새로운 컬럼에 추가합니다.

    Args:
        csv_file_path (str): CSV 파일의 경로

    Returns:
        pandas.DataFrame: 예측 결과가 추가된 DataFrame
    """

    # CSV 파일 읽기
    df = pd.read_csv(csv_file_path)

    # 새로운 컬럼 추가 및 값 채우기
    for k in tqdm([1, 5, 15, 25, 49]):
      df[f'k{k}'] = df.apply(lambda row: run_prediction(row['Length'], row['Weight'], k=k), axis=1)

    return df

def add_prediction_column_api(csv_file_path='/home/diginori/code/fishmlserv/note/fish_test_data_100k.csv'):
    """
    CSV 파일의 데이터를 읽어와 각 행에 대한 예측 결과를 새로운 컬럼에 추가합니다.

    Args:
        csv_file_path (str): CSV 파일의 경로

    Returns:
        pandas.DataFrame: 예측 결과가 추가된 DataFrame
    """

    # CSV 파일 읽기
    df = pd.read_csv(csv_file_path)

    # 새로운 컬럼 추가 및 값 채우기
    for k in tqdm([1, 5, 15, 25, 49]):
      df[f'k{k}'] = df.apply(lambda row: get(row['Length'], row['Weight'], k=k), axis=1)

    return df