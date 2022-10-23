import pandas as pd
import numpy as np

def feature_gen(df: pd.DataFrame)-> pd.DataFrame:
    df = df.copy()
    # Степень ухода за домом. Вычисляется как OverallCond * (2022 - YearRemodAdd). Например, при оценке общей оценке "8" дом 20-летней давности получит значение 160.
    df['HomeCare'] = ((df['OverallCond']) * (2022 - (df['YearRemodAdd']))).astype(np.int32)
    # Использование одного материала в отделке фасада
    df['ExteriorSingle'] = (df['Exterior1st'] == df['Exterior2nd'])
    return df