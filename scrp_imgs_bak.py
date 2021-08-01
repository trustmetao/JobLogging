import os
import re
import ssl
import requests
from requests import HTTPError
# import urllib.request
# from urllib.request import urlretrieve

ssl._create_default_https_context = ssl._create_unverified_context

def get_req(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print('HTTP error occurred:' + str(http_err))
    except Exception as err:
        print('Other error occurred:' + str(err))
    return response

def getImag(url, savepath):
    def reporthook(a, b, c):
        print("\rdownloading: %5.1f%%" % (a * b * 100.0 / c), end="")

    if not os.path.isfile(savepath):
        print('Downloading data from %s' % url)
        print(savepath)
        response = get_req(file_url)
        img_blob = response.content
        if response.status_code == 200:
            # print('Success')
            with open(savepath, 'wb') as img_file:
                img_file.write(img_blob)
                print("File saved: " + savepath)

        print('\nDownload finished!')
    else:
        print('File already exsits!')
    filesize = os.path.getsize(savepath)
    
    print('File size = %.2f Mb' % (filesize/1024/1024))
             

if __name__ == '__main__':
    Categories = ['Akarna_Dhanurasana']
    for category in Categories:
        savepath='./Data/Images/' + category
        if not os.path.exists(savepath):
            # print('Creating folder...')
            os.mkdir(savepath)
        with open('./Data/yoga_dataset_links/' + '%s.txt' % category, 'r') as f:
            for text in f:
                print('###')
                file_name = text.split('\t')[0].split('/')[-1]
                file_url = text.split('\t')[-1].strip() # strip to remove '%0A'
                # print(file_name)
                # print(file_url)
                getImag(file_url, os.path.join(savepath, file_name))
                print('###')

