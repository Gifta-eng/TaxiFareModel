from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np

# class TimeFeaturesEncoder(BaseEstimator, TransformerMixin):
#     """Extract the day of week (dow), the hour, the month and the year from a
#     time column."""
#     def __init__(self, time_column, time_zone_name='America/New_York'):
#         self.time_column = time_column
#         self.time_zone_name = time_zone_name

#     def extract_time_features(self, X):
#         timezone_name = self.time_zone_name
#         time_column = self.time_column
#         df = X.copy()
#         df.index = pd.to_datetime(df[time_column])
#         df.index = df.index.tz_convert(timezone_name)
#         df["dow"] = df.index.weekday
#         df["hour"] = df.index.hour
#         df["month"] = df.index.month
#         df["year"] = df.index.year        
#         return df
        
#     def fit(self, X, y=None):
#         return self

#     def transform(self, X, y=None):
#         """Returns a copy of the DataFrame X with only four columns: 'dow', 'hour', 'month', 'year'"""
#         return self.extract_time_features(X)[['dow', 'hour', 'month', 'year']].reset_index(drop=True)

# def haversine_vectorized(df, 
#          start_lat="pickup_latitude",
#          start_lon="pickup_longitude",
#          end_lat="dropoff_latitude",
#          end_lon="dropoff_longitude"):

#     """ 
#         Calculate the great circle distance between two points 
#         on the earth (specified in decimal degrees).
#         Vectorized version of the haversine distance for pandas df
#         Computes distance in kms
#     """

#     lat_1_rad, lon_1_rad = np.radians(df[start_lat].astype(float)), np.radians(df[start_lon].astype(float))
#     lat_2_rad, lon_2_rad = np.radians(df[end_lat].astype(float)), np.radians(df[end_lon].astype(float))
#     dlon = lon_2_rad - lon_1_rad
#     dlat = lat_2_rad - lat_1_rad

#     a = np.sin(dlat / 2.0) ** 2 + np.cos(lat_1_rad) * np.cos(lat_2_rad) * np.sin(dlon / 2.0) ** 2
#     c = 2 * np.arcsin(np.sqrt(a))
#     return 6371 * c

# class DistanceTransformer(BaseEstimator, TransformerMixin):
#     """Compute the haversine distance between two GPS points."""
#     def __init__(self, 
#                  start_lat="pickup_latitude",
#                  start_lon="pickup_longitude", 
#                  end_lat="dropoff_latitude", 
#                  end_lon="dropoff_longitude"):
#         self.start_lat = start_lat
#         self.start_lon = start_lon
#         self.end_lat = end_lat
#         self.end_lon = end_lon

#     def fit(self, X, y=None):
#         return self
    
#     def transform(self, X, y=None):
#         """Returns a copy of the DataFrame X with only one column: 'distance'"""
#         return pd.DataFrame(haversine_vectorized(X)).rename(columns={0: "course distance [km]"}).copy()
