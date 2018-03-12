
def insert_qry_generator_v2(column_value_dict, table_nm):
    """
    From param dict, generates INSERT query
    :param column_value_dict: Dictionary extracted from JSON
    :param table_nm: Table into which records to be inserted
    :return: INSERT query
    """
    insert_qry = ''
    if isinstance(column_value_dict, dict):
        columns = str(list(column_value_dict.keys())).replace('[', '(').replace(']', ')').replace("'", "\"")
        values = str(list(column_value_dict.values())).replace('[', '(').replace(']', ')').replace('None', 'null')
        insert_qry = 'INSERT INTO '+ table_nm +   columns + ' VALUES ' + values
    elif isinstance(column_value_dict, list):
        print("Feed to ",table_nm,' is not a dictionary')
    return str(insert_qry)




