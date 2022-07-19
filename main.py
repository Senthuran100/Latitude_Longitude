import pandas as pd

"""
Group the location based on the Longitude and Latitude.
Find the Median, Minimum and Maximum of Download and Upload Column.
"""
def group_same_location():
    try:
        df = pd.read_csv(r'DataRatev2.csv')
        sameLocationDF =df.groupby(['Longitude','Latitude']).agg({'Download': ['median', 'min', 'max'],'Upload':['median','min','max']})
        sameLocationDF.columns = ['Download Median', 'Download Minimum', 'Download Maximum','Upload Median', 'Upload Minimum', 'Upload Maximum']
        sameLocationDF = sameLocationDF.reset_index()
        return sameLocationDF
    except FileNotFoundError:
        print("File does not exist")
    except:
        print("Exception occured.")

"""
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
