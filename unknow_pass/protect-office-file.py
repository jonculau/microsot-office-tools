import sys, zipfile, re, json, shutil
path = sys.argv[1]
recovery = json.load(open(sys.argv[2], 'r', encoding='utf-8'))
archive = zipfile.ZipFile(path, mode='r')
archive.extractall(path='tmp')
files = archive.namelist()
archive.close()
archive = zipfile.ZipFile(path, mode='w')
for file in files:
    if file in recovery:
        xmlStr = open('tmp/' + file, 'r', encoding='utf-8').read()
        xmlStr = xmlStr.replace('<sheetData/>','<sheetData/>' + recovery[file])
        xmlStr = xmlStr.replace('</sheetData>','</sheetData>' + recovery[file])
        xmlStr = xmlStr.replace("<bookViews>", recovery[file] + "<bookViews>")
        open('tmp/' + file, 'w', encoding='utf-8').write(xmlStr)
    archive.write('tmp/' + file, file)
archive.close()
shutil.rmtree('tmp', ignore_errors=True)
        
