import sys, zipfile, re, json, shutil
import xml.etree.ElementTree as ET
path = sys.argv[1]
archive = zipfile.ZipFile(path, mode='r')
archive.extractall(path='tmp')
files = archive.namelist()
archive.close()

recovery = {}
archive = zipfile.ZipFile(path, mode='w')
for file in files:
    if file.endswith('xml'):
        xmlStr = open('tmp/' + file, 'r', encoding='utf-8').read()
        if  re.search(r'<[^<]*?Protection[^<]*?/>', xmlStr):
            protection = re.findall(r'<[^<]*?Protection[^<]*?/>', xmlStr)[0]
            next = xmlStr.split(protection)[1].split(' ')[0]
            recovery[file] = {
                'tag': protection,
                'replace': next
            }
            open('tmp/' + file, 'w', encoding='utf-8').write(xmlStr.replace(protection, ''))
    archive.write('tmp/' + file, file)
json.dump(recovery, open('recovery.json', 'w', encoding='utf-8'), indent=4)
archive.close()
shutil.rmtree('tmp', ignore_errors=True)
        
