import pandas as pd
import numpy as np

signif = pd.read_csv('signif.txt', sep = '\t')
print(signif.head())
print list(signif.columns.values)
runup = pd.read_csv('tsrunup.txt', sep='\t')
print runup.head()
print list(runup.columns.values)

eq = signif[['I_D','FLAG_TSUNAMI','YEAR','MONTH','DAY','LATITUDE','LONGITUDE','REGION_CODE']]
tsu = runup[['I_D','YEAR','MONTH','DAY','LATITUDE','LONGITUDE','REGION_CODE']]
eq['TYPE'] = 'eq'
tsu['FLAG_TSUNAMI'] = 'tsu'
tsu['TYPE'] = 'tsu'

eq.dropna(how='any', subset=['YEAR','LATITUDE','LONGITUDE'], inplace=True)
tsu.dropna(how='any', subset=['YEAR','LATITUDE','LONGITUDE'], inplace=True)

print eq
print tsu

rcodes = {77:10, 78:10, 73:120, 72:150, 70:15, 71:160, 75:150, 76:150, 74:90, 40:110, 50:130, 30:140, 60:60, 87:150, 84:30, 81:170, 80:150, 83:170, 82:170, 86:90, 85:30, 88:100, 89:100}
tsu['REGION_CODE'] = tsu['REGION_CODE'].apply(lambda x: rcodes[x])
print tsu.head()

cct = pd.concat([eq, tsu])
cct = cct.sort_values(['YEAR','MONTH','DAY'])
code = ''
anm = 0
loc = 0
codes = []
anmly = []

cct = cct.reset_index(drop=True)
for i in range(len(cct)):
    if cct.ix[i]['FLAG_TSUNAMI']=='tsu':
        codes.append(code)
        if loc != cct.ix[i]['REGION_CODE'] and anm ==0:
            anmly.append(3)
        else:
            anmly.append(anm)
    elif cct.ix[i]['FLAG_TSUNAMI']=='Tsu':
        anm = 0
        code = i
        codes.append(code)
        if cct.ix[i+1]['FLAG_TSUNAMI']!='tsu':
            anmly.append(2)
        else:
            anmly.append(0)
            loc = cct.ix[i]['REGION_CODE']
    else:
        anm = 0
        code = i
        codes.append(code)
        if cct.ix[i+1]['FLAG_TSUNAMI']=='tsu':
            anm = 1    
        anmly.append(0)
       
cct['REL_EQ'] = codes
cct['ANOMALY?'] = anmly

print cct
cct.to_csv('anomalies.csv')
