from lxml import html
import requests, urllib3, re, json
from urllib3.contrib import pyopenssl

#Take care about SSL redirects in Reuters
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS='ALL'
headers = {
'User-Agent': 'Mozilla/5.0',
'X-Api-Key':'adf51226795afbc4e7575ccc124face7',
}


#What we have in the beginning
url="""http://feeds.reuters.com/~r/reuters/topNews/~3/tZ0mjPE-XIc/khamenei-urges-irans-military-to-scare-off-enemy-official-website-idUSKCN1LP07Q"""

#Get some data, decode from binary to utf
page = requests.get(url,headers=headers, allow_redirects=True)
text=page.content.decode("utf-8")

#Extract JSON object
m = re.search('window\.RCOM_Data\s=\s\{.*\"\}\};', text)
dirty_data=m.group()
dirty_data=re.sub('window\.RCOM_Data\s=\s', '', dirty_data)
dirty_data=re.sub('"\}\};', '"}}', dirty_data)

#Get JSON decoded and get main key to extract body
json_data = json.loads(dirty_data)
main_key=list(filter(lambda h: 'article' in h, json_data.keys()))[0]


#Print body
print(json_data[main_key]['first_article']['body'])
