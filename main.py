#!/usr/bin/python3



from extract import extract_pkg_info
from extract import extract_pkg_classifiers
from extract import extract_pkg_releases
from extract import fetch_json
from load import insert_qry_generator_v2
from bs4 import BeautifulSoup
import requests
if __name__ == '__main__':

    import sys
    #print("Running...")
    package_name = sys.argv[1]

    js_data = fetch_json(package_name)
    qry = insert_qry_generator_v2(extract_pkg_info(js_data), 'info')
    

    print(qry)
