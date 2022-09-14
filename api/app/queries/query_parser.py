def query_parse(path):
    # Open and read the file as a single buffer
    fd = open(path, 'r')
    sql_file = fd.read()
    fd.close()
    return sql_file

