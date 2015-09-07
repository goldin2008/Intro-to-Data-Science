import json
import requests

#if __name__ == '__main__'

def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain.
    #
    # Once you've done this, return the name of the number 1 top artist in Spain.
    
    return ... # return the top artist in Spain
    #Provide a URL we should make an API call to.
    url = ''
    
    #Make our API call using the requests library and load the results into a dict.
    data = requests.get(url).text
    data = json.loads(data)

    #Print out the name of the #1 top artist.
    print data['topartists']['artist'][0]['name']
