import pandas as pd

# Création des données complètes
data = {
    'id': ['0712930052', '0019220141', '0040020150', '0087520141', '0051020150'],
    'date': ['2014-10-13T000000', '2014-12-09T000000', '2015-02-25T000000', '2014-12-09T000000', '2015-02-18T000000'],
    'price': [221900.0, 538000.0, 180000.0, 604000.0, 510000.0],
    'bedrooms': [3, 3, 2, 4, 3],
    'bathrooms': [1.00, 2.25, 1.00, 3.00, 2.00],
    'sqft_living': [1180, 2570, 770, 1960, 1680],
    'sqft_lot': [5650, 7242, 10000, 5000, 8080],
    'floors': [1.000, 2.000, 1.000, 1.000, 1.000],
    'waterfront': [0, 0, 0, 0, 0],
    'view': [0, 0, 0, 0, 0],
    'grade': [7, 7, 6, 7, 8],
    'sqft_above': [1180, 2170, 770, 1050, 1680],
    'sqft_basement': [0, 400, 0, 910, 0],
    'yr_built': [1955, 1951, 1933, 1965, 1987],
    'yr_renovated': [0, 0, 0, 0, 0],
    'zipcode': [98178, 98125, 98028, 98136, 98074],
    'lat': [47.5112, 47.7210, 47.7379, 47.5208, 47.6168],
    'long': [-122.2571, -122.3191, -122.2332, -122.3931, -122.0451],
    'sqft_living15': [1340, 1690, 2720, 1360, 1800],
    'sqft_lot15': [5650, 7639, 8062, 5000, 7503]
}

# Création du DataFrame
df = pd.DataFrame(data)

# Sauvegarde en CSV avec tous les champs
df.to_csv('house_data_complete.csv', index=False)

# Affichage des premières lignes pour vérification
print(df.head())

# Affichage des informations sur le dataset
print("\nInformations sur le dataset:")
print(df.info())