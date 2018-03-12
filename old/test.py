from extract_v3 import extract_pkg_info
from extract_v3 import extract_pkg_classifiers
from extract_v3 import extract_pkg_releases
from extract_v3 import fetch_json
from load_v3 import insert_qry_generator_v2
from bs4 import BeautifulSoup

if __name__ == '__main__':
    import requests
    pkg_nm = 's'
    js_data = fetch_json(pkg_nm)
    print(js_data)
    print(insert_qry_generator_v2(extract_pkg_info(js_data), 'info'))



    """
        print(insert_qry_generator_v2(extract_pkg_info(js_data),'info'))
        print(insert_qry_generator_v2(extract_pkg_classifiers(js_data),'class'))
        for lines in extract_pkg_releases(js_data,js_data['info']['version'],pkg_nm):
            print(insert_qry_generator_v2(lines,'release'))
    """