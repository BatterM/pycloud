from flask import Flask
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    res=requests.get('http://10.36.145.100:5000/v2/_catalog')
    a=res.json()
    c={}
    for j in a.values():
        for n in range(len(j)):
            re=requests.get('http://10.36.145.100:5000/v2/{}/tags/list'.format(j[n]))
            c.setdefault(j[n],re.json().get('tags'))
    html='<!DOCTYPE HTML><html><body><table border="0"><tr><th>REPOSITORY&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</th><th>TAG</th>'
    for i in c.items():
        for j in range(len(i[1])):
            html+='</tr><tr><td>{}</td><td>{}</td></tr>'.format(i[0],i[1][j])
    html+='</table></body><ml>'
    return html

if __name__ == '__main__':
    app.run()

