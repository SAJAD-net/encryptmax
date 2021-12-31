from sys import argv
import os

def run(key, path):
    for fil in os.listdir(path):
        nfile = path+"/'"+fil+"'"
        com = f"./encryptmax {key} {nfile}"
        os.system(com)
        enc = lambda x:x[:10] if len(x) >=10 else x
        print(f"{enc(fil)} ... OK")

if len(argv) > 2:
    run(int(argv[1]), argv[2])

