# For each file, create new column Coord: Long + " " + Lat
# Merge all three on Coord


# http://chrisalbon.com/python/pandas_dataframe_importing_csv.html




import pandas as pd


def main():
    # sets headers, fills in all missing data as "tsrunup_missing", skip first row of file
    df1 = pd.read_csv('C:/Users/Anya/Desktop/tsrunup.txt', delimiter = '\t',
                      names=['I_D', 'TSEVENT_ID', 'YEAR', 'MONTH', 'DAY', 'DOUBTFUL', 'COUNTRY', 'STATE',
                             'LOCATION_NAME', 'LATITUDE', 'LONGITUDE', 'REGION_CODE',
                             'DISTANCE_FROM_SOURCE', 'TRAVEL_TIME_HOURS', 'TRAVEL_TIME_MINUTES',
                             'WATER_HT', 'HORIZONTAL_INUNDATION', 'TYPE_MEASUREMENT_ID', 'PERIOD',
                             'FIRST_MOTION', 'DEATHS', 'DEATHS_DESCRIPTION', 'INJURIES',
                             'INJURIES_DESCRIPTION', 'DAMAGE_MILLIONS_DOLLARS', 'DAMAGE_DESCRIPTION',
                             'HOUSES_DAMAGED', 'HOUSES_DAMAGED_DESCRIPTION', 'HOUSES_DESTROYED',
                             'HOUSES_DESTROYED_DESCRIPTION'], na_values=['tsrunup_missing'], skiprows=1)
    # Create new column to merge data on in future
    df1['COORDS']= list(zip(df1.LATITUDE, df1.LONGITUDE))
    #print df1

    # sets headers, fills in all missing data as "tsevent_missing", skip first row of file
    df2 = pd.read_csv('C:/Users/Anya/Desktop/tsevent.txt', delimiter = '\t',
                      names=['ID', 'YEAR', 'MONTH', 'DAY', 'HOUR', 'MINUTE', 'SECOND', 'VENT_VALIDITY', 'CAUSE_CODE',
                             'FOCAL_DEPTH', 'PRIMARY_MAGNITUDE', 'COUNTRY', 'STATE', 'LOCATION_NAME', 'LATITUDE',
                             'LONGITUDE', 'REGION_CODE', 'MAXIMUM_WATER_HEIGHT', 'ABE', 'IIDA', 'SOLOVIEV',
                             'WARNING_STATUS', 'DEATHS', 'DEATHS_DESCRIPTION', 'MISSING', 'MISSING_DESCRIPTION',
                             'INJURIES', 'INJURIES_DESCRIPTION', 'DAMAGE_MILLIONS_DOLLARS', 'DAMAGE_DESCRIPTION',
                             'HOUSES_DESTROYED', 'HOUSES_DESTROYED_DESCRIPTION', 'HOUSES_DAMAGED',
                             'HOUSES_DAMAGED_DESCRIPTION', 'TOTAL_DEATHS', 'TOTAL_DEATHS_DESCRIPTION', 'TOTAL_MISSING',
                             'TOTAL_MISSING_DESCRIPTION', 'TOTAL_INJURIES', 'TOTAL_INJURIES_DESCRIPTION',
                             'TOTAL_DAMAGE_MILLIONS_DOLLARS', 'TOTAL_DAMAGE_DESCRIPTION', 'TOTAL_HOUSES_DESTROYED',
                             'TOTAL_HOUSES_DESTROYED_DESCRIPTION', 'TOTAL_HOUSES_DAMAGED',
                             'TOTAL_HOUSES_DAMAGED_DESCRIPTION'], na_values=['tsevent_missing'], skiprows=1)
    # Create new column to merge data on in future
    df2['COORDS'] = list(zip(df2.LATITUDE, df2.LONGITUDE))
    #print df2


    # sets headers, fills in all missing data as "signif_missing", skip first row of file
    df3 = pd.read_csv('C:/Users/Anya/Desktop/signif.txt', delimiter = '\t',
                      names=['I_D', 'FLAG_TSUNAMI', 'YEAR', 'MONTH', 'DAY', 'HOUR', 'MINUTE', 'SECOND', 'FOCAL_DEPTH',
                             'EQ_PRIMARY', 'EQ_MAG_MW', 'EQ_MAG_MS', 'EQ_MAG_MB', 'EQ_MAG_ML', 'EQ_MAG_MFA',
                             'EQ_MAG_UNK', 'INTENSITY', 'COUNTRY', 'STATE', 'LOCATION_NAME', 'LATITUDE', 'LONGITUDE',
                             'REGION_CODE', 'DEATHS', 'DEATHS_DESCRIPTION', 'MISSING', 'MISSING_DESCRIPTION',
                             'INJURIES', 'INJURIES_DESCRIPTION', 'DAMAGE_MILLIONS_DOLLARS', 'DAMAGE_DESCRIPTION',
                             'HOUSES_DESTROYED', 'HOUSES_DESTROYED_DESCRIPTION', 'HOUSES_DAMAGED',
                             'HOUSES_DAMAGED_DESCRIPTION', 'TOTAL_DEATHS', 'TOTAL_DEATHS_DESCRIPTION', 'TOTAL_MISSING',
                             'TOTAL_MISSING_DESCRIPTION', 'TOTAL_INJURIES', 'TOTAL_INJURIES_DESCRIPTION',
                             'TOTAL_DAMAGE_MILLIONS_DOLLARS', 'TOTAL_DAMAGE_DESCRIPTION', 'TOTAL_HOUSES_DESTROYED',
                             'TOTAL_HOUSES_DESTROYED_DESCRIPTION', 'TOTAL_HOUSES_DAMAGED',
                             'TOTAL_HOUSES_DAMAGED_DESCRIPTION'], na_values=['signif_missing'], skiprows=1)
    # Create new column to merge data on in future
    df3['COORDS'] = list(zip(df3.LATITUDE, df3.LONGITUDE))
    #df3['COORDS'] = df3['COORDS'].astype(str)
   # " ".join(df3['COORDS'].str.split())
    #for index, row in df3.iterrows():
        #df3['COORDS'] = df3.apply(" ".join(df3['COORDS'].str.split()), axis =1)
    #    print df3['COORDS']
    #df3['COORDS'] = df3['COORDS'].str.strip()
    print df3

    # Merge all three dataframes on COORDS
    #df_final = df1.merge(df2, on='COORDS').merge(df3, on='COORDS')
    df_final = df1.merge(df2, on='COORDS')
    #print df_final.columns
    #print df_final


main()
