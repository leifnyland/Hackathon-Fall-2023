import os
import subprocess
import json

def get_access_token():
    client_id = "a2c6bbc43d704d4da85406d0c9c088bc"
    client_secret = "988518dd0f6e4b779c90c0fe84723249"

    return json.loads(subprocess.getoutput('curl -X POST "https://accounts.spotify.com/api/token" -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=client_credentials&client_id=' + client_id + '&client_secret=' + client_secret + '"').strip().split("\n")[-1])['access_token']


def get_artist_data(artist_url):
    access_token = get_access_token()
    messy_dict_string = subprocess.getoutput('curl "https://api.spotify.com/v1/artists/' + artist_url + '" -H "Authorization: Bearer  ' + access_token + '"')[317:]
    messy_dict = json.loads(messy_dict_string)
    return {
        'name': messy_dict['name'],
        'popularity': messy_dict['popularity'],
        'followers': messy_dict['followers']['total'],
        'genres': messy_dict['genres'],
        'id': messy_dict['id']
    }


if __name__ == '__main__':
    print(get_artist_data('1ZwdS5xdxEREPySFridCfh?si=c-0ZDIwYSx2L-qmaqoE0Iw'))


