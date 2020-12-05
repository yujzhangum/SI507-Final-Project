# Use API to get the jobseach results
from serpapi import GoogleSearch
import json




params = {
  "engine": "google_jobs",
  "q": "data analysis",
  "hl": "en",
  "api_key": "a463df1e2c78e577d9220ceeba3d0f6cc418db1a445ed7520d0fc6b0c62ab95a",
  "location_requested": "Austin,Texas,United States"
}
client = GoogleSearch(params)
results = client.get_dict()
results = results['jobs_results']


with open('job-results.json', 'w') as fp:
    json.dump(results, fp)




CACHE_FILE_NAME = 'job-results.json'

def load_cache():
    try:
        cache_file = open(CACHE_FILE_NAME,'r')
        cache_file_contents = cache_file.read()
        cache = json.loads(cache_file_contents)
        cache_file.close()
    except:
        cache = {}
    return cache
    
def save_cache(cache):
    cache_file = open(CACHE_FILE_NAME,'w')
    contents_to_write = json.dumps(cache)
    cache_file.write(contents_to_write)
    cache_file.close()
    
def make_url_request_using_cache(results):
    cache = load_cache()
    l = []
    for i in results:
        if i in cache:
            dic = {}
            dic['job'] = i['title']
            dic['company_name'] = i['title']
            l.append(dic)
            print('Using cache')
            print(dic)
            print('----------------------------------------------------------')
            
        else:
            save_cache(i)
            dic = {}
            dic['job'] = i['title']
            dic['company_name'] = i['title']
            l.append(dic)
            print('Fetching')

    return l

            
            
    

