import os

PRODUCTION = False

# The following needs to bea added to avoid issues with the mysqlclient
# Refer to https://stackoverflow.com/questions/46902357/error-loading-mysqldb-module-did-you-install-mysqlclient-or-mysql-python

# try:
#     if os.environ['PRODUCTION'] == 'True':
#         import pymysql
#         pymysql.install_as_MySQLdb()
# except Exception as e:
#     pass
