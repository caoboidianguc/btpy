import requests

def get_rhymes(word):
    baseUrl = 'https://api.datamuse.com/words'
    paramsDiction = {} #set up empty dict for query parameters
    paramsDiction['rel_rhy'] = word
    paramsDiction['max'] = '3' #get at most 3 result
    respon  = requests.get(baseUrl, params=paramsDiction)
    word_ds = respon.json()
    return [d['word'] for d in word_ds] #list comprehention

print(get_rhymes('funny'))