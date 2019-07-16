# -*- coding: utf-8 -*-

import re

sql_flie = ''
sql_str = ''

mysql_key_words_after_where = 'group,order,limit'

cloum_rule = 'select(.*)from.*'
condition_rule = '(?:and|where|\))*?(.*?)(?:and|group)'

property_head = 'private String '

xml_result_start = '<result colunm = "'
xml_result_mid = '" property = "'
xml_result_end = '" jdby_Type = "varchar" />'

def getCloums(sql):
    pattern = re.compile(cloum_rule,re.S)
    cloums = pattern.findall(sql)
    return cloums

def getConditions(sql):
    dict = {'single':[],'mauty':[]}
    pattern = re.compile(condition_rule,re.S)
    conditions = pattern.findall(sql)
    for condition in conditions:
        if '=' in condition :
            condition = condition.replace('where','').strip()
            arr = condition.split('=')
            dict['single'].append(arr[0].strip())

        if 'in' in condition:
            condition = condition.replace('where','').strip()
            arr = condition.split('in')
            dict['mauty'].append(arr[0].strip())

    return dict

print(getConditions('where a=4 and c=1 and d=2 and b=3 and e in ('','') group by 1)a '
                    'select * from hello where s=1 group by 1'))
# print(getCloums('where a=b and c=1 and d=2 group by 1)a select a.hello from hello where s=1 group by 1'))

def replaceByIndex(str,index,target_char):
    str_list = list(str)
    str_list[index] = target_char
    return ''.join(str_list)

# print(replaceByIndex('hello_world',6,'F'))

def buildUperCloums(cloums):
    uper_c = []
    for cloum in cloums:
        if cloum == '':
            continue
        while '_' in cloum:
            index = cloum.index('_')
            cloum = replaceByIndex(cloum,index,'')
            c = cloum[index]
            cloum = replaceByIndex(cloum,index,c.upper())
        uper_c.append(cloum)
        # print(property_head+cloum)
    return  uper_c

def buildJavaBean(cloum_arr):
    for cloum in cloum_arr:
        print(property_head+cloum)

def buildMybatitsXml(cloum_arr,uper_clounms):
    for clounm,uper_clounm in zip(cloum_arr,uper_clounms):
        print(xml_result_start+clounm+xml_result_mid+uper_clounm+xml_result_end)


def buildService():
    pass
def buildServiceImpl():
    pass

def buildDao():
    pass
def buildDaoImpl():
    pass

def buildController():
    pass



# print(buildMybatitsXml(['he_llo_wor','hello_wo'],['Hello','Bitch']))
