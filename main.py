import numpy as np
import pandas as pd
import json
import requests
from requests.structures import CaseInsensitiveDict

if __name__ == '__main__':
    print('web scrapper')

    #smiles_code = 'C([C@]1([H])[C@]([H])([C@@]([H])([C@]([H])([C@]([H])(OC[C@]2([H])[C@]([H])([C@@]([H])([C@]([H])([C@@]([H])(O)O2)O)O)O)O1)O)O)O)O'
    #smiles_code = ''
    #url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/{smiles_code}/cids/TXT"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    cids = []

    df = pd.read_excel("dataset.xlsx")

    for i in range(len(df)):
        url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/{str(df.iloc[i,0])}/cids/TXT"
        resp = requests.get(url, headers=headers)

        if resp.status_code == 400:
            print( str(i) + " " + "error status code 400")
            cids.append("NA")
        else:
            results = resp.json()
            print( str(i) +" "+ str(results))
            cids.append(results)

        if i % 100 == 0:
            df1 = pd.DataFrame(cids)
            df1.to_csv(f'output/{i}.csv', index=False)

    #print(cids)

    df['cids'] = pd.Series(cids)
    df.to_excel('output.xlsx')
    #print(df)

