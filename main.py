import pandas as pd

"""
Used to find the same location.
Same location is when latitude and longitude is same.
"""
def find_same_location():
    try:
        df = pd.read_csv(r'DataRatev2.csv')
        sameLocationDF = df[df[['Longitude', 'Latitude']].nunique(axis=1) == 1]
        return sameLocationDF
    except FileNotFoundError:
        print("File does not exist")
    except:
        print("Error in opening the file")

"""
Calculate the maximum, minimum and median value of download and Upload.
Save the result into a csv file.
"""
def calculate_save_csv_file():
    df = find_same_location()
    if df.empty:
        print("CSV doesn't consist of the same location")
        return
    else:
        col_names = ['Maximum', 'Minimum', 'Median']
        data_df = pd.DataFrame(columns=col_names)
        data_df['Maximum'] = df[['Download', 'Upload']].values.max(1)
        data_df['Minimum'] = df[['Download', 'Upload']].values.min(1)
        data_df['Median'] = df[['Download', 'Upload']].values.mean(1)
        data_df.to_csv('output.csv', index=None, header=True)
        print(data_df)


if __name__ == '__main__':
    calculate_save_csv_file()
