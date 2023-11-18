import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OrdinalEncoder

def prepare_for_test(data:pd.DataFrame) -> np.ndarray:
        num_cols = [col for col in data.columns if data[col].dtype in ['int64','float64']]
        cat_cols = [col for col in data.columns if data[col].dtype=='object' ]
        
        numerical_preprocessor = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='mean')),
            ('scaler', StandardScaler())
        ])
        categorical_preprocessor = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ("ordinal", OrdinalEncoder())
        ])
        preprocessor = ColumnTransformer(transformers=[
            ("numerical", numerical_preprocessor, num_cols),
            ("categorical", categorical_preprocessor, cat_cols)
        ])
        processed_data = preprocessor.fit_transform(data)
        return processed_data