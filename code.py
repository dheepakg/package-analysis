def fetch_json(package_name):
    """
    Fetch JSON file file of a package from pypi
    :param package_name:
    :return: json object
    """
    requests_object = requests.get('http://pypi.python.org/pypi/'+package_name+'/json')
    return json.loads(requests_object.text)

def pkg_info(json_file,dist_key='info'):
    """
    Fetches package info from json file
    :param json_file: json file extracted in main()
    :param dist_key: default value = 'info'
    :return: Returns 10 values -
    """
    info_dtl = []
    variables = ['version',
                 'summary',
                 'home_page',
                 'requires_dist',
                 'package_url',
                 'author',
                 'author_email',
                 'docs_url',
                 ]
    for key in variables:
        info_dtl.append(json_file[dist_key][key])

    return info_dtl

def pkg_releases(json_file,versn_num,dist_key='releases'):
    """
    Extracts release details
    :param json_file: json object from pypi
    :param versn_num: extracts latest version from pkg_info_details
    :param dist_key: Default tp 'releases'
    :return:
    """
    keys = ['url', 'packagetype', 'size', ]

    release_distributions = []
    for values in json_file[dist_key][versn_num]:
        distribution = []
        for key in keys:

            distribution.append(values[key])
        release_distributions.append(distribution)

    return(release_distributions)

def classifier(json_data, dist_key = 'info', sub_dist_key='classifiers'):
    """
    Extracts classifiers details
    :param package_name: Pass the package name
    :return:
    """
    json_contents = json_data[dist_key][sub_dist_key]
    classify_key = ['Development Status',
               'Environment',
               'Framework',
               'Intended Audience',
               'License',
               'Natural Language',
               'Operating System',
               'Programming Language',
               'Topic',
               ]
    classifiers = dict.fromkeys(classify_key)
    classifier_values = []
    for key in classify_key:
        dev_sts = []
        for values in json_contents:

            if values.startswith(key):
                dev_sts.append(values.replace(key,'').replace('::','').strip())
                classifiers[key] = dev_sts


    print(classifiers)
    print((classifiers.values()))
    return list(classifiers.values())


if __name__ == '__main__':
    import requests
    import json
    package_nm = 'requests'
    json_data = fetch_json(package_nm)
    pkg_info = pkg_info(json_data)
    print('pkg_info',pkg_info)
    print('pkg_releases',pkg_releases(json_data,pkg_info[0]))
    print('pkg_classifiers ', classifier(json_data))


