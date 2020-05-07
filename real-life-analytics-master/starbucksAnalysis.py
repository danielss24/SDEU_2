import numpy as np
import pandas as pd

taxiData = pd.read_csv("data/trip_data_2013-01-14.csv")
starbucksData = pd.read_csv("data/All_Starbucks_Locations_in_the_US_2013.csv")

      #Latitud   #Longitud
nw = [40.916178, -74.25909]
se = [40.477399, -73.700181]

lat = 0
lon = 1

margen = 0.02

# a = starbucksData[starbucksData['Longitude'] > -74.25909]
# a = a[a['Longitude'] < -73.700181]
# a = a[a['Latitude'] > 40.477399]
# a = a[a['Latitude'] < 40.916178]

taxiDataFiltered = taxiData[taxiData['pickup_longitude'] > nw[lon]]
taxiDataFiltered = taxiDataFiltered[taxiDataFiltered['pickup_longitude'] < se[lon]]
taxiDataFiltered = taxiDataFiltered[taxiDataFiltered['pickup_latitude'] > se[lat]]
taxiDataFiltered = taxiDataFiltered[taxiDataFiltered['pickup_latitude'] < nw[lat]]

taxiDataFiltered = taxiDataFiltered[taxiDataFiltered['dropoff_longitude'] > nw[lon]]
taxiDataFiltered = taxiDataFiltered[taxiDataFiltered['dropoff_longitude'] < se[lon]]
taxiDataFiltered = taxiDataFiltered[taxiDataFiltered['dropoff_latitude'] > se[lat]]
taxiDataFiltered = taxiDataFiltered[taxiDataFiltered['dropoff_latitude'] < nw[lat]]

starbucksDataFiltered = starbucksData[starbucksData['Longitude'] > nw[lon]]
starbucksDataFiltered = starbucksDataFiltered[starbucksDataFiltered['Longitude'] < se[lon]]
starbucksDataFiltered = starbucksDataFiltered[starbucksDataFiltered['Latitude'] > se[lat]]
starbucksDataFiltered = starbucksDataFiltered[starbucksDataFiltered['Latitude'] < nw[lat]]

dictStoreNum_SB = {}

starbucksDataFiltered = starbucksDataFiltered.reset_index()
taxiDataFiltered = taxiDataFiltered.reset_index()
# storeNumberSB = starbucksData['Store Number'].to_numpy()
for i in np.unique(starbucksDataFiltered['Store Number'].to_numpy()):
    dictStoreNum_SB[i] = 0

for contTax in range(len(taxiDataFiltered)):
    for contStarbucks in range(len(starbucksDataFiltered)):
        margenInf_lon = starbucksDataFiltered['Longitude'][contStarbucks] * (1-0.02)
        margenSup_lon = starbucksDataFiltered['Longitude'][contStarbucks] * (1+0.02)
        margenInf_lat = starbucksDataFiltered['Latitude'][contStarbucks] * (1-0.02)
        margenSup_lat = starbucksDataFiltered['Latitude'][contStarbucks] * (1+0.02)

        if (margenSup_lon > taxiDataFiltered['pickup_longitude'][contTax] > margenInf_lon):
            if (margenSup_lat > taxiDataFiltered['pickup_latitude'][contTax] > margenInf_lat):
                if (margenSup_lon > taxiDataFiltered['dropoff_longitude'][contTax] > margenInf_lon):
                    if (margenSup_lat > taxiDataFiltered['dropoff_latitude'][contTax] > margenInf_lat):
                        dictStoreNum_SB[starbucksData['Store Number'][contStarbucks]] += 1

print("FIN")


