import pandas as pd

"""
Used to find the same location.
Same location is when latitude and longitude is same.
"""
def group_same_location():
    try:
        df = pd.read_csv(r'DataRatev2.csv')
        sameLocationDF =df.groupby(['Longitude','Latitude']).agg({'Download': ['mean', 'min', 'max'],'Upload':['mean','min','max']})
        sameLocationDF.columns = ['Download Mean', 'Download Min', 'Download Max','Upload Mean', 'Upload Min', 'Upload Max']
        sameLocationDF = sameLocationDF.reset_index()
        return sameLocationDF
    except FileNotFoundError:
        print("File does not exist")
    except:
        print("Exception occured.")

"""
Calculate the maximum, minimum and median value of download and Upload.
Save the result into a csv file.
"""
def save_csv_file():
    df = group_same_location()
    if df.empty:
        print("No processed Data. Try with proper data format")
        return
    else:
        df.to_csv('output.csv', index=None, header=True)
        print(df)


if __name__ == '__main__':
    save_csv_file()
