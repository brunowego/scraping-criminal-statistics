# %%
import requests
from bs4 import BeautifulSoup
from re import compile
from camelot import read_pdf
import numpy as np
import pandas as pd


# %%
url = 'https://www.seguranca.go.gov.br/estatisticas'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'lxml')
link = soup.find('a', attrs={'href': compile('relatorio-2020-jan-e-set\.pdf$')})
table_areas = [
  '11,744,584,675',
  '11,669,584,560',
  '11,556,584,499',
  '11,494,584,396',
  '11,393,584,294'
]

# %%
frames = []
tables = read_pdf(link['href'], pages='1-end', flavor='stream', table_areas=table_areas)

for table in tables:
  # %%
  catidx = np.where(table.df.iloc[:1].applymap(lambda x: x != ''))[1][0]
  category = table.df.iloc[:1].values[0][catidx]
  columns = table.df.iloc[1]
  data = table.df.iloc[2:]
  data.columns = columns
  data = data.drop(columns=data.columns[-1])
  data.at[:, 'CATEGORIA'] = category
  data.at[:, 'ANO'] = 2020

  frames.append(data)

# %%
result = pd.concat(frames)
result.to_csv('statistics.csv', index=False, header=True)
