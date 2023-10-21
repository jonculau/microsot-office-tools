import sys, zipfile, re, json, shutil
path = sys.argv[1]
archive = zipfile.ZipFile(path, mode='r')
archive.extractall(path='tmp')
files = archive.namelist()
archive.close()

recovery = {}
archive = zipfile.ZipFile(path, mode='w')
for file in files:
    if file.startswith('xl/worksheets/sheet'):
        xmlStr = open('tmp/' + file, 'r', encoding='utf-8').read()
        protection = "".join(re.findall(r'<sheetProtection[^>]*?/>', xmlStr))
        recovery[file] = protection
        open('tmp/' + file, 'w', encoding='utf-8').write(xmlStr.replace(protection, ''))
        json.dump(recovery, open('recovery.json', 'w', encoding='utf-8'), indent=4)
    archive.write('tmp/' + file, file)
archive.close()
# shutil.rmtree('tmp', ignore_errors=True)
        
