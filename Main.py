import mysql.connector
import openpyxl
from mysql.connector import errorcode
from python_mysql_dbconfig import read_db_config
from pathlib import Path
import table_from_dd

table_from_dd