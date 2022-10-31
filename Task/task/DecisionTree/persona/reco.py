import numpy as np
import pandas as pd

df_read = pd.read_csv("/home/abhinav-dev/practice/QBC.csv")
Location = df_read.Region

df_mobiles = pd.read_excel("/home/abhinav-dev/practice/Mobile_Prices.xlsx")
df_mobiles = df_mobiles.drop_duplicates(subset="Product", keep="first")
Devices = df_mobiles.Product.unique()
age = np.random.randint(20, 80, size=(2000, 1)).reshape(-1, 1)
balance = np.random.randint(4000, 12500, size=(2000, 1)).reshape(-1, 1)
Location_rand = np.random.choice(Location, 2000)
Devices_rand = np.random.choice(Devices, 2000)
df_fin = pd.DataFrame(
    zip(age, balance, Location_rand, Devices_rand),
    columns=["age", "balance", "location", "device"],
)
df_fin.to_csv("Fin.csv")
