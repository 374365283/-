import time
import datetime
import psycopg2
import json
import os

duration = 10
interval = 5
name = 'Util'
database_name = 'tutorial'
table_name = 'monitor_' + name
user_name = 'postgres'
password_name = 'postgres'
host_name = '172.16.0.190'
port_name = '5432'

#create the database
def create_table(name,database_name,table_name,user_name,password_name,host_name,port_name):

     conn = psycopg2.connect(database=database_name, user=user_name, password=password_name, host=host_name, port=port_name)
     cur = conn.cursor()
     #create the database

     var = os.popen("s-tui -j").read()
     var = json.loads(var)
     dic = var[name]

     coloum_name = []
     for coloum in dic:
         coloum_name.append(str(coloum)) 
     strCreateTable = "CREATE TABLE "+table_name+"(time TIMESTAMPTZ NOT NULL"
     for coloum in coloum_name:
         strCreateTable += "," + coloum.replace(' ','') + " DOUBLE PRECISION NULL"
     strCreateTable += ");"
     strCreateHypertable = "SELECT create_hypertable('"+table_name+"','time');"
     cur.execute(strCreateTable)
     cur.execute(strCreateHypertable)
     conn.commit()

#insert the data
def insert(duration,interval,name,database_name,table_name,user_name,password_name,host_name,port_name):
    
    conn = psycopg2.connect(database=database_name, user=user_name, password=password_name, host=host_name, port=port_name)
    cur = conn.cursor()
    
    var = os.popen("s-tui -j").read()
    var = json.loads(var)
    dic = var[name]
    coloum_name = []
    for coloum in dic:
          coloum_name.append(str(coloum))
    for i in range(duration):
          time.sleep(1)
          if i % interval == 0:
             var = os.popen("s-tui -j").read()
             var = json.loads(var)
             dic = var[name]
             info = []
             for coloum in coloum_name:
                  info.append(str(dic[coloum]))
             insert_cmd = "INSERT INTO "+table_name+"(time"
             for coloum in coloum_name:
                  insert_cmd += ','+coloum.replace(' ','')
             insert_cmd += ') VALUES (NOW()'
             for coloum in coloum_name:
                  insert_cmd += ',%s'
             insert_cmd += ');' 
             cur.execute(insert_cmd, info)

    conn.commit()

create_table(name,database_name,table_name,user_name,password_name,host_name,port_name)  
insert(duration,interval,name,database_name,table_name,user_name,password_name,host_name,port_name)
