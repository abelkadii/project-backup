import sys, os, shutil

try:
    FROM = sys.argv[1]
    TO = sys.argv[2]
except:
    print("invalid input form")
    print("the correct input form is /"python script [FROM] [TO]/"")
    exit(0)

def _read(path):
    with open(path, 'rb') as f:
        return f.read()
def _write(path, data):
    with open(path, 'wb') as f:
        f.write(data)
        f.close()

def backup(src, des):
    data = _read(src)
    creation_time, modification_time = os.path.getctime(src), os.path.getmtime(src)
    _write(des, data)
    os.utime(des, (creation_time, modification_time))

def delete(path):
    if os.path.isfile(path):
        os.remove(path)
        return
    shutil.rmtree(path)

def backup_dir(path):
    name = path.split('\\')[-1]
    if name in ignore:
        return
    # print(os.path.join(TO, path))
    if not os.path.exists(os.path.join(TO, path)):
        os.mkdir(os.path.join(TO, path))
    paths = os.listdir(os.path.join(FROM, path))
    for item in paths:
        if not os.path.isfile(os.path.join(FROM, path, item)):
            backup_dir(os.path.join(path, item))
            continue
        backup_file(os.path.join(path, item))
    for item in os.listdir(os.path.join(TO, path)):
        if item not in paths:
            delete(os.path.join(TO, path, item))
    

def backup_file(path):
    name = path.split('\\')[-1]
    if name in ignore:
        return

    if os.path.exists(os.path.join(TO, path)) and os.path.getmtime(os.path.join(FROM, path)) == os.path.getmtime(os.path.join(TO, path)):
        return    
    return backup(os.path.join(FROM, path), os.path.join(TO, path))

def main():
    backup_dir("")
ignore = _read(os.path.join('\\'.join(__file__.split('\\')[:-1]), '.gitignore')).decode().split('\n')
main()
