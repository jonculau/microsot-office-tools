import sys, zipfile, re, json, shutil
path = sys.argv[1]
archive = zipfile.ZipFile(path, mode='r')
archive.extractall(path='tmp')
files = archive.namelist()
archive.close()

recovery = {}
archive = zipfile.ZipFile(path, mode='w')
for file in files:
    if file.startswith('xl/worksheets/sheet') or file.startswith('xl/workbook'):
        xmlStr = open('tmp/' + file, 'r', encoding='utf-8').read()
        if file.startswith('xl/worksheets/sheet'):
            protection = "".join(re.findall(r'<sheetProtection[^>]*?/>', xmlStr))
        else:
            protection = "".join(re.findall(r'<workbookProtection[^>]*?/>', xmlStr))
        recovery[file] = protection
        open('tmp/' + file, 'w', encoding='utf-8').write(xmlStr.replace(protection, ''))
    archive.write('tmp/' + file, file)
json.dump(recovery, open('recovery.json', 'w', encoding='utf-8'), indent=4)
archive.close()
shutil.rmtree('tmp', ignore_errors=True)
        
