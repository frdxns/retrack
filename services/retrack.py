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

    imagens = pegar_imagens(usuario)
    
    
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

    dadoscru = [{"artistas": artistas}, {"musicas": musicas}, {"albuns": albuns}, {"recente": recente(usuario)}]

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
        
    dado = response.json()

    if "@attr" in dado["recenttracks"]["track"][0]:
        musica_recente = {"tocando": True, "titulo": dado["recenttracks"]["track"][0]["name"], "artista": dado["recenttracks"]["track"][0]["artist"]["#text"]}
    else:
        musica_recente = {"tocando": False, "titulo": dado["recenttracks"]["track"][0]["name"], "artista": dado["recenttracks"]["track"][0]["artist"]["#text"]}

    return musica_recente

def pegar_id(usuario):
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
    
    musica = dados["toptracks"]["track"]
    
    id = musica[0]["mbid"],

    return id

def pegar_imagens(usuario):
    id = pegar_id(usuario)

    params = {
        "method": "track.getinfo",
        "mbid": id,
        "api_key": API_KEY,
        "format": "json"
    }

    response = requests.get(URL, params=params)
    dados = response.json()
    imagem = dados["track"]["album"]["image"]

    return imagem