import pandas as pd

enrollments = pd.read_csv("enrollments.csv")
print(len(enrollments))
print(len(enrollments['account_key'].unique()))
print(enrollments[enrollments['account_key'] > 1000])
print()