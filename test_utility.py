import pytest
import pandas as pd
import numpy as np
from prediction_demo import data_preparation,data_split,train_model,eval_model

@pytest.fixture
def housing_data_sample():
    return pd.DataFrame(
      data ={
      'price':[13300000,12250000],
      'area':[7420,8960],
    	'bedrooms':[4,4],	
      'bathrooms':[2,4],	
      'stories':[3,4],	
      'mainroad':["yes","yes"],	
      'guestroom':["no","no"],	
      'basement':["no","no"],	
      'hotwaterheating':["no","no"],	
      'airconditioning':["yes","yes"],	
      'parking':[2,3],
      'prefarea':["yes","no"],	
      'furnishingstatus':["furnished","unfurnished"]}
    )

def test_data_preparation(housing_data_sample):
    feature_df, target_series = data_preparation(housing_data_sample)
    # Target and datapoints has same length
    assert feature_df.shape[0]==len(target_series)

    #Feature only has numerical values
    assert feature_df.shape[1] == feature_df.select_dtypes(include=(np.number,np.bool_)).shape[1]

@pytest.fixture
def feature_target_sample(housing_data_sample):
    feature_df, target_series = data_preparation(housing_data_sample)
    return (feature_df, target_series)

def test_data_split(feature_target_sample):
    return_tuple = data_split(*feature_target_sample)
    # TODO test if the length of return_tuple is 4
    # Ensure the function returns 4 items
    assert len(return_tuple) == 4, "data_split should return 4 elements"

    # Extract the returned values
    X_train, X_test, y_train, y_test = return_tuple

    # Ensure returned data types are correct
    assert isinstance(X_train, pd.DataFrame), "X_train should be a DataFrame"
    assert isinstance(X_test, pd.DataFrame), "X_test should be a DataFrame"
    assert isinstance(y_train, pd.Series), "y_train should be a Series"
    assert isinstance(y_test, pd.Series), "y_test should be a Series"

    # Ensure train-test split ratio (80-20 split for 2 samples means 1 train, 1 test)
    assert X_train.shape[0] == 1, "X_train should have 1 sample"
    assert X_test.shape[0] == 1, "X_test should have 1 sample"
    assert y_train.shape[0] == 1, "y_train should have 1 sample"
    assert y_test.shape[0] == 1, "y_test should have 1 sample"
    # raise NotImplemented
