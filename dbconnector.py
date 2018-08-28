# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 16:04:42 2018

@author: ASUS
"""

import os
from urllib import parse
import psycopg2 as ps

def connectToDatabase():
    url='postgres://hudqkrrzsagcyt:9a66c1df30600ba0b45377d31daeb34c9b9d35cd19ee6b5771e4d31d8f04e6b2@ec2-54-235-160-57.compute-1.amazonaws.com:5432/d6bs2drdcbe4p0'

    os.environ['DATABASE_URL'] = url
               
    parse.uses_netloc.append('postgres')
    url=parse.urlparse(os.environ['DATABASE_URL'])
    
    conn=ps.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
            )
    
    cur=conn.cursor()
    
    return cur, conn

def runquery(query):
    cur, conn=connectToDatabase()
    result=None
    try:
        cur.execute(query)
        result=list(cur)
    except:
        result=['error']
        
    cur.close()
    conn.commit()
    conn.close()
    return result

def runUpdateQuery(query):
    cur, conn=connectToDatabase()
    result=None
    try:
        cur.execute(query)
        result=cur.rowcount
    except:
        result=['error']
        
    conn.commit()
    cur.close()
    conn.close()
    return result

def getUrl():
    query="SELECT val FROM datastore WHERE item='url'"
    result=runquery(query)
    try:
        ret=result[0][0]
    except:
        ret="error"
    
    return ret

def setUrl(newurl):
    query="UPDATE datastore SET val='%s' WHERE item='url'"%(newurl)
    print(query)
    result=runUpdateQuery(query)
    if result > 0:
        ret="success"
    else:
        ret='fail'
    
    return ret

def getPassword():
    query="SELECT val FROM datastore WHERE item='password'"
    result=runquery(query)
    try:
        ret=result[0][0]
    except:
        ret="error"
    
    return ret

def setPassword(newurl):
    query="UPDATE datastore SET val='%s' WHERE item='password'"%(newurl)
    print(query)
    result=runUpdateQuery(query)
    if result > 0:
        ret="success"
    else:
        ret='fail'
    
    return ret