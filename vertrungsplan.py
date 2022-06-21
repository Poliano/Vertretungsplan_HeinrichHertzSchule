from bs4 import BeautifulSoup
import requests
import pandas as pd
import lxml
import numpy as np

urllist = 3
url = f"https://www.heinrich-hertz-schule-hamburg.de/vertretungsplan/subst_00{urllist}.htm"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

date = doc.div.string
print(date)

dfs = pd.read_html(url, index_col=False)
df = dfs[1]

substring = input("Eingabe: ")
print(df[df.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)])