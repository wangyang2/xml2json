# python_version = 3.5

import xmltodict
import json

def xml2json(xmlstr):
    convertedDict=xmltodict.parse(xmlstr,encoding='utf-8')
    jsonStr=json.dumps(convertedDict,indent=1,ensure_ascii=False)
    return jsonStr

if __name__=='__main__':
    xml=open("train.xml", 'r', encoding='utf-8').read()
    outputfile=open('result.json','w',encoding='utf-8')
    outputfile.write(xml2json(xml))
