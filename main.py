import pandas as pd
import os

data_dir = "data"
data_files = []
for file in os.listdir(data_dir):
    if file.endswith(".csv"):
        full_path = os.path.join(data_dir, file)
        data_files.append(full_path)


print("csv files found: ", data_files)

def process_files(file_path):
    df = pd.read_csv(file_path)
    df = df[df['product'] == 'Pink Morsels'].copy()
    df['price'] = df['price'].str.replace('$','',regex=False).astype(float)
    df['sales'] = df['price'] * df['quantity']
    return df[['sales','date','region']]

for file in data_files:
    pro = process_files(file)

processed_data = pd.concat([process_files(f) for f in data_files], axis=0,ignore_index=True)

os.makedirs("output", exist_ok=True)
processed_data.to_csv('output/sales.csv', index=False)
print("Processed data saved to output/sales.csv")
