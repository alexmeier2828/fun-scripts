try:
    from googlesearch import search
except ImportError:
    print("missing dep")
import sys
import subprocess 

#args
query = sys.argv[0]



results = search(query, tld='com', lang='en', num=10, start=0, stop=10, pause=1.0)


for r in results:
    print(r)
    p = subprocess.Popen(["w3m",str(r)]).wait()  

