import os, random, sys


DEPTH = int(sys.argv[1])
DESTINATION = sys.argv[2]

PATH = os.path.join(os.getcwd(), DESTINATION)

extentitons = ["py", "js", "cpp", "c", "java",  "go", "php" , "html", "css", "ts", "jsx", "tsx", "sh", "png", "jpeg", "pdf", "docx", "xlsx"]


def generate_file(path):
    name=''.join([chr(97+random.randint(0, 25)) for i in range(random.randint(5, 10))])+'.'+random.choice(extentitons)
    with open(os.path.join(path, name), 'wb') as f:
        out=b""
        for i in range(random.randint(100, 8192)):
            out+=chr(random.randint(0, 127)).encode()
        f.write(out)
        f.close()
    return
def generate_dir(path, r):
    if r==DEPTH:
        return
    name=''.join([chr(97+random.randint(0, 25)) for i in range(random.randint(5, 10))])
    os.mkdir(os.path.join(path, name))
    for i in range(random.randint(1, 50)):
        if random.random()<.3:
            generate_dir(os.path.join(path, name), r+1)
            continue
        generate_file(os.path.join(path, name))
        
generate_dir(PATH, 0)