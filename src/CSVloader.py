import zipfile
import urllib.request

url = 'https://www.kaggle.com/nasa/meteorite-landings/download'
zipname = '../dataset/archive.zip'
filename = '../dataset/data.csv'

try:
    urllib.request.urlretrieve(url, zipname)
    with zipfile.ZipFile(zipname, 'r') as zip_ref:
        zip_ref.extractall(filename)

except urllib.error.HTTPError as err:
    print(f'{err}')
