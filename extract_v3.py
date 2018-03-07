import json
import requests

def fetch_json(package_name):
    """
    Fetch JSON file file of a package from pypi
    :param package_name:
    :return: json object
    """
    error_file = '/Users/deegee/PycharmProjects/navFileFolder/log_error_pkg.log'
    try:
        requests_object = requests.get('http://pypi.python.org/pypi/'+package_name+'/json')

        good_file = '/Users/deegee/PycharmProjects/navFileFolder/log_good_pkg.log'
        #with open(good_file, 'a') as good_log:   good_log.write(package_name + '\t\tis good \n')
        return requests_object.json()

    except:
        print(package_name, " needs some attention @ fetch_json")

        with open(error_file, 'a') as error_log:
            error_log.write(package_name + ' error @ fetch_json ' + '\n')
        good_file = '/Users/deegee/PycharmProjects/navFileFolder/log_good_pkg.log'




# todo Check requires_dist need to check
def extract_pkg_info(json_file,dist_key='info'):
    """
    Fetches package info from json file
    :param json_file: json file extracted in main()
    :param dist_key: default value = 'info'
    :return: Returns 10 values -
    """

    info_dtl = {}

    variables = ['name',
                     'version',
                     'summary',
                     'home_page',
                     #'requires_dist',
                     'package_url',
                     'author',
                     'author_email',
                     'docs_url',
                    ]
    try:
        #print('requires_dist',json_file[dist_key]['requires_dist'])
        for key in variables:
            if key == 'requires_dist':
                # print("if",json_file[dist_key][key])
                str_list = str(json_file[dist_key][key])
                str_list1 = str_list[1:len(str_list) - 1]
                # print("str_list1",str_list1)
                str_list2 = str_list1.replace('[', '').replace(']', '').replace('(', '').replace(')', '')
                info_dtl[key] = str_list2.replace('\'', '').replace('\"', '').replace('\\', '')
                # print("last if info_dtl",info_dtl[key])
                # print("last if info_dtl dict",info_dtl)
            else:
                # print("else",type(json_file[dist_key][key]))
                info_dtl[key] = json_file[dist_key][key]

            # print("before return",info_dtl)
            return info_dtl
    except:
        print('At ', extract_pkg_info)


def extract_pkg_releases(json_file,versn_num,package_nm,dist_key='releases'):
    """
    Extracts release details of latest version
    :param json_file: json object from pypi
    :param versn_num: extracts latest version from pkg_info_details
    :param dist_key: Default tp 'releases'
    :return:
    """
    keys = ['url',
            'packagetype',
            'size',
            ]
    release_distributions = []
    distribution = {}
    if len(json_file[dist_key][versn_num]) == 0:
        for key in keys:
            distribution.setdefault(key,'null')
        release_distributions.append(distribution)

    for values in json_file[dist_key][versn_num]:

        distribution = {}
        distribution['name'] = package_nm
        distribution['number_of_dists'] = len(json_file[dist_key][versn_num])
        for key in keys:
            distribution[key] = values[key]

        release_distributions.append(distribution)
    return(release_distributions)


def extract_pkg_classifiers(json_data, dist_key = 'info', sub_dist_key='classifiers'):
    """
    Extracts classifiers details under info (in json)
    :param package_name: Pass the package name
    :return:
    """
    json_contents = json_data[dist_key][sub_dist_key]
    classify_key = ['Name',
                    'Development Status',
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
    classifiers['Name'] = json_data['info']['name']
    for key in classify_key:
        dev_sts = []
        for values in json_contents:
            if values.startswith(key):
                dev_sts.append(values.replace(key,'').replace('::','').strip())
                classifiers[key] = ','.join(dev_sts)
    return classifiers