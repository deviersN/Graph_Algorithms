import zipfile
import urllib.request

url = 'https://www.kaggle.com/nasa/meteorite-landings/download'
url2 = 'https://www.kaggle.com/neuromusic/avocado-prices/download'
url3 = 'https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results/downloads'
zipname = '../dataset/archive.zip'
filename = '../dataset/data.csv'

try:
    urllib.request.urlretrieve(url3, zipname)
    with zipfile.ZipFile(zipname, 'r') as zip_ref:
        zip_ref.extractall(filename)

except urllib.error.HTTPError as err:
    print(f'{err}')
