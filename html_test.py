import pandas as pd
#df_html = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
URL = 'https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/' #'https://en.wikipedia.org/wiki/London'
dfs = pd.read_html(URL)