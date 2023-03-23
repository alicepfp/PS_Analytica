from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route("/album-info", methods=["GET"])

def infoartista():
    
    APIKEY = 2
    id = '111239'

    url = 'https://theaudiodb.com/api/v1/json/{}/search.php?i={}'.format(APIKEY, id)

    response = requests.get(url)

    nome = response.json()

    return id, nome

def ultimoalbum():

    APIKEY = 2    
    url = 'theaudiodb.com/api/v1/json/{}/artist.php?i={}'.format(APIKEY, id)

    response = requests.get(url)

    albums = response.json()['album']

    album_info = []

    for album in albums:
        
        idalbum = album['idAlbum']
        anoalbum = album['intYearReleased']
        nomealbum = album['strAlbum']

        info = { 'id': idalbum, 'year': anoalbum, 'name': nomealbum }

        album_info.append(info)

    album_ano = max(d['year'] for d in album_info)

    id_latest = [d['id'] for d in album_info if d['year'] == album_ano]

    album_latest = [{ 'id': d['id'], 'name': d['name'] } for d in album_info if d['year'] == album_ano]
    return album_ano, album_latest

def musicas():

    APIKEY = 2 
    ids = [a['id'] for a in album_latest]

    if len(ids) > 1:
        for id in ids:
            url = "https://theaudiodb.com/api/v1/json/{}/track.php?m={}".format(APIKEY, id)

            response = requests.get(url)

            musicas = response.json()['track']

            if len(musicas) == 1:
                full_album = None
            
            if len(musicas) > 1:
                full_album = musicas 
                album_id = id

    else:
        id = ids[0]
        
        album_id = id 

        url = "https://theaudiodb.com/api/v1/json/{}/track.php?m={}".format(APIKEY, id)

        response = requests.get(url)

        full_album = response.json()['track']
    i = 1
    album_tracks = {}
    for musicas in full_album:
        key = str(i)
        album_tracks[key] = track["strTrack"]
        i+=1
    
    return album_tracks, album_id

def info():

    data = {
            "artist": nome,
            "latest-album": album_latest,
            "album-year": album_ano,
            "album-tracks": album_tracks,
            }
    
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)

