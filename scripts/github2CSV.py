from github import Github
import datetime
import csv
import sys
from lxml import html
import json
import yaml
import ConfigParser 
import os
import io

FILTER_LABELS=("Accettato",)

try:
    config=ConfigParser.RawConfigParser()
    config.read('.github.cfg')

    PASS=config.get('GitHub','TOKEN')
    USER=config.get('GitHub','USER')
    REPO_NAME=config.get('GitHub','REPO_NAME')
    ORG=config.get('GitHub','ORG')
except:
    TOKEN=os.environ.get('GITHUB_TOKEN')
    PASS=os.environ.get('GITHUB_PASSWORD')
    USER=os.environ.get('GITHUB_USERNAME')
    REPO_NAME='covid19italia_segnalazioni'
    ORG='emergenzeHack'

if not TOKEN:
    if not PASS:
        print "Need a TOKEN"
        sys.exit(1)

    if not USER:
        print "Need a USER"
        sys.exit(1)

if not REPO_NAME:
    print "Need a REPO_NAME"
    sys.exit(1)

if not ORG:
    print "Need a ORG"
    sys.exit(1)

CSVFILE=sys.argv[1]

try:
    JSONFILE=sys.argv[2]
    jwr=io.open(JSONFILE,"w+",encoding="utf-8")
except:
    jwr=None

try:
    GEOJSONFILE=sys.argv[3]
    gjwr=io.open(GEOJSONFILE,"w+",encoding="utf-8")
except:
    gjwr=None

wr=file(CSVFILE,"w+")
csvwriter=csv.writer(wr,quotechar='"')

lastTime = datetime.datetime(2000,1,1)

if TOKEN:
    g = Github(TOKEN)
else:
    g = Github(USER, PASS)
org=g.get_organization(ORG)
r = org.get_repo(REPO_NAME)

filter_labels=[r.get_label(l) for l in FILTER_LABELS]

issues=r.get_issues(since=lastTime,labels=filter_labels,state='all')

csvwriter.writerow(("url","id","updated_at","created_at","title","lat","lon","labels","milestone","image","data","body","state"))

if gjwr:
    gjwr.write(unicode('{ "type": "FeatureCollection", "features": '))

csvarray=[]
jsonarray=[]
geojsonarray=[]

for issue in issues:
    labels = json.dumps([l.name for l in issue.labels])
    data={}
    lat=None
    lon=None
    image=None

    try:
        tree=html.fromstring(issue.body)

        try:
            dataRaw=tree.xpath("//data/text()")
            dataStr=dataRaw[0] if len(dataRaw) > 0 else None
            data=json.loads(dataStr)
        except:
            pass

        try:
            yamldataRaw=tree.xpath("//yamldata/text()")
            yamldataStr=yamldataRaw[0] if len(yamldataRaw) > 0 else None
            data=yaml.load(yamldataStr)
        except:
            pass
    except:
        pass

    if data.has_key("Posizione"):
        (lat,lon) = data["Posizione"].split(" ")[:2]

    if data.has_key("immagine"):
        image=data['immagine']

    title=issue.title
    if title is not None:
        title=title.encode('utf-8')

    labels=labels.encode('utf-8')

    csvarray.append((issue.html_url,issue.id,issue.updated_at,issue.created_at,title,lat,lon,labels,issue.milestone,image,json.dumps(data,sort_keys=True),issue.body.encode('utf-8'), issue.state))
    
    if jwr:
        jsonarray.append({"title":issue.title,"number":issue.number,"state":issue.state,"issue":{"url":issue.html_url,"id":issue.id,"updated_at":issue.updated_at.isoformat()+"+00:00","created_at":issue.created_at.isoformat()+"+00:00","title":title,"lat":lat,"lon":lon,"labels":labels,"milestone":issue.milestone.title if issue.milestone else None,"image":image,"data":data,"body":issue.body.encode('utf-8')}})

    if gjwr:
        geojsonarray.append({"type":"Feature","geometry":{"type":"Point","coordinates":[lon,lat]},"properties":{"title":issue.title,"number":issue.number,"state":issue.state,"url":issue.html_url,"id":issue.id,"updated_at":issue.updated_at.isoformat()+"+00:00","created_at":issue.created_at.isoformat()+"+00:00","labels":eval(labels) if labels else None,"milestone":issue.milestone.title if issue.milestone else None,"image":image,"data":data,"body":issue.body.encode('utf-8')}})

csvwriter.writerows(csvarray)

if jwr:
    jwr.write(json.dumps(jsonarray,ensure_ascii=False,encoding='utf8',sort_keys=True))

if gjwr:
    gjwr.write(json.dumps(geojsonarray,ensure_ascii=False,encoding='utf8',sort_keys=True)+"}")

