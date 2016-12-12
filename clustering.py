from sklearn.cluster import DBSCAN
import pandas as pd

df = [[12669, 9656, 7561, 214, 2674, 1338],[7057,9810, 9568, 1762, 3293, 1776],[6353, 8008, 7684, 2405, 3516, 7844],[13265, 1196, 4221, 6404, 507, 1788],[22615, 5410, 7198, 3915, 1777, 5185]]
data = pd.DataFrame(df, columns=['Fresh','Milk','Grocery','Frozen','Detergents','Delicassen'] )
print data
