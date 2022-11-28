from flask import Flask, url_for
from flask import request
from flask import render_template
import ssl
import base64
from elasticsearch import Elasticsearch
from elasticsearch.connection import create_ssl_context


app = Flask(__name__, static_url_path='/static')


@app.route('/')
def home():
    return render_template('home.html')

context = create_ssl_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

es = Elasticsearch(
    ['121.43.234.160'],
    http_auth=('liuay20', 'liuay20'),
    scheme="http",
    port=9200,
    ssl_context = context,
)

@app.route('/search', methods=['get'])
def search():
    keywords = request.args.get('keywords')
    algorithm = request.args.get('algorithm')


    if algorithm=="BM25":
        indexname="liuay20_bossjob"
    elif algorithm=="DFR":
        indexname="liuay20_test_dfr"
    elif algorithm=="IB":
        indexname="liuay20_test_ib"

    query = {
        "from": 0, "size": 3000,
        "query": {
            "multi_match": {
                "query": keywords,
                "fields": ["Name", "Address", "Salary", "Work_Frequency", "Work_Period","Company_Name", "Company_Employee_Number"]
            }
        }
    }
    res = es.search(index=indexname, body=query)
    hits = res["hits"]["total"]["value"]
    return render_template('results.html', keywords=keywords, hits=hits, docs=res["hits"]["hits"], algorithm=algorithm,res=res)
