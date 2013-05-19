#!/usr/bin/python
# coding: utf8

import MySQLdb
import config
import sys
from xml.etree import ElementTree
import codecs

def fast_iter(context, func, args=[], kwargs={}):
    for event, elem in context:
        func(elem, *args, **kwargs)
        elem.clear()
    del context

def recording(cursor, data, value):
    pub={}
    #data = data.encode('utf-8')
    #value = value.encode('utf-8')
    print data
    print value
    sql='''INSERT INTO dict (id, data, value)
           VALUES (%s, %s, %s)
        '''
    args = ['', data, value]
    #try:
    cursor.execute(sql,args)
    #except:
    #    print "Execute error"
    return



def main():
    connection=MySQLdb.connect(charset='utf8',
        host=config.HOST,user=config.USER,
        passwd=config.PASS,db=config.MYDB)
    cursor=connection.cursor()

    with open('dict.xdxf', 'rt') as f:
        tree = ElementTree.parse(f)
    
    for node in tree.iter('k'):
        recording(cursor, node.text , node.tail)


    cursor.close()
    connection.commit()
    connection.close()

if __name__ == '__main__':
    main()

