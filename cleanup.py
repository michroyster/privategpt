import sys, shutil

database = sys.argv[1]

try:
    shutil.rmtree(f"{database}/")
    print(f"echo Removed vectordb: {database}")
except OSError as e:
    print(f"Error, {e.strerror} : {database}/")