import pandas as  pd
from pandas_profiling import ProfileReport

df=pd.read_csv('weather.csv')

report=ProfileReport(df,title='analysis dataset')
report.to_file('pandas analysis.html')