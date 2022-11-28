import ssl
from elasticsearch import Elasticsearch
from elasticsearch.connection import create_ssl_context

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

indexname='liuay20_test_dfr11'

print(es.indices.get_settings(index=indexname))
print(es.indices.get_mapping(index=indexname))
