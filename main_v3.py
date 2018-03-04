from extract_v3 import extract_pkg_info
from extract_v3 import extract_pkg_classifiers
from extract_v3 import extract_pkg_releases
from extract_v3 import fetch_json
from load_v3 import insert_qry_generator_v2
from bs4 import BeautifulSoup

if __name__ == '__main__':
    import requests
    print("Running...")
    pkg_nm = 'requests'
    url = 'https://pypi.python.org/simple/'
    r = requests.get(url)
    html_doc = r.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    for link in soup.find_all('a'):
        pkg_nm = link.get('href')
        js_data = fetch_json(pkg_nm)

        #print(insert_qry_generator_v2(extract_pkg_info(js_data), 'info'))

    print("Completed!")

    """
        print(insert_qry_generator_v2(extract_pkg_info(js_data),'info'))
        print(insert_qry_generator_v2(extract_pkg_classifiers(js_data),'class'))
        for lines in extract_pkg_releases(js_data,js_data['info']['version'],pkg_nm):
            print(insert_qry_generator_v2(lines,'release'))
    """