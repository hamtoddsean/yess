
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
import json
import os
import time

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
#@app.route('/')
def hello_world():
#    return 'Hello from Flask!'
 fd=task_id
 clist=[]
 pathh='/home/testtomanna/fule.json'
 if not os.path.exists(pathh):
   with open(pathh,'w') as dou:
     douu=json.dump(clist,dou)


 for i in range(100):
   time.sleep(1)
   with open(pathh,'r') as d:
     g=json.load(d)
     print(g)
     g.append(2)
     with open(pathh,'w') as gc:
       json.dump(g,gc)


 if __name__ == '__main__':
   app.run(debug=True)