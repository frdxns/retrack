import requests, os, json
from dotenv import load_dotenv

load_dotenv()

URL = "http://ws.audioscrobbler.com/2.0/"
API_KEY = os.getenv("LASTFM_API_KEY")


def pegar_top_artistas(usuario):
    params = {
        "method": "user.gettopartists",
        "period": "7day",
        "user": usuario,
        "api_key": API_KEY,
        "format": "json",
        "limit" : 3
    }

    response = requests.get(URL, params= params)
    
    dados = response.json()


    artistas = dados["topartists"]["artist"]

    dadosformatados = [{
        "titulo": artista["name"],
        "plays": artista["playcount"]
    }for artista in artistas]

    artistasdados  = dadosformatados
    return artistasdados


def pegar_top_musicas(usuario):
    params = {
        "method": "user.gettoptracks",
        "period": "7day",
        "user": usuario,
        "api_key": API_KEY,
        "format": "json",
        "limit" : 3
    }

    response = requests.get(URL, params= params)

    dados = response.json()
    
    musicas = dados["toptracks"]["track"]
    
    imagens = dados["toptracks"]["track"][0]["image"]
    
    dadosformatados = [{
        "id" : musica["mbid"],
        "titulo": musica["name"],
        "plays":musica["playcount"],
        "imagem": next((img['#text'] for img in imagens if img['size'] == 'extralarge'), 'fallback-image.png')
    }for musica in musicas]

    musicas_dados = dadosformatados
    return musicas_dados


def pegar_top_albuns(usuario):
    params = {
        "method": "user.gettopalbums",
        "user": usuario,
        "period": "7day",
        "api_key": API_KEY,
        "format": "json",
        "limit" : 3
    }

    response = requests.get(URL, params= params)

    dados = response.json()
    
    albuns = dados["topalbums"]["album"]

    dadosformatados = [{
        "titulo": album["name"],
        "plays": album["playcount"]
    }for album in albuns]

    albuns_dados = dadosformatados
    return albuns_dados


def pegar_tops_lastfm(usuario):

    artistas = pegar_top_artistas(usuario)
    musicas = pegar_top_musicas(usuario)
    albuns = pegar_top_albuns(usuario)

    dadoscru = [{"artistas": artistas}, {"musicas": musicas}, {"albuns": albuns}]

    dados = json.dumps(dadoscru)
    return dados

def recente(usuario):
    params = {
            "method": "user.getrecenttracks",
            "period": "7day",
            "user": usuario,
            "api_key": API_KEY,
            "format": "json",
            "limit" : 1
        }
    
    response = requests.get(URL, params= params)
        
    dados = response.json()

    return dados



def imagens():
    params = {
        "method": "track.getinfo",
        "mbid": '455aacf0-d22a-4c9f-bbc2-27d431613b20',
        "api_key": API_KEY,
        "format": "json"
    }

    response = requests.get(URL, params=params)
    dados = response.json()

    return dados