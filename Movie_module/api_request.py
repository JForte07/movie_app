# github_request.py
from pip._vendor import requests
import json
import numpy as np


class APIRequest:
    _base_url = "https://imdb-api.com"
        
    @classmethod
    def get_id(cls, movie_title):
        content = json.loads(requests.get(cls._base_url+"/en/API/SearchMovie/k_kymjglxh/"+ movie_title).content)
        
        result = content['results']
        List_id =[]
        #récupération des Id
        for i in range(len(result)):
            content_id = result[i]
            Id = content_id['id']
            List_id.append(Id)
        return List_id
    
    @classmethod
    def get_title(cls, movie_title):
        content = json.loads(requests.get(cls._base_url+"/en/API/SearchMovie/k_kymjglxh/"+ movie_title).content)
        
        result = content['results']
        List_title =[]
        #récupération des titres des films 
        for i in range(len(result)):
            content_id = result[i]
            title = content_id['title']
            List_title.append(title)
        l = len(List_title)
        return List_title,l 

    @classmethod
    def get_poster(cls,movie_title) : 
        content = json.loads(requests.get(cls._base_url+"/en/API/SearchMovie/k_kymjglxh/"+ movie_title).content)
        
        result = content['results']
        List_poster =[]
        #récupération des ima
        for i in range(len(result)):
            content_id = result[i]
            poster = content_id['image']
            if content_id['image'] == '':
                poster = 'not available'
                List_poster.append(poster)
            else : 
                List_poster.append(poster)
        return List_poster


    @classmethod
    def get_rank(cls,id) : 
        all_movie = json.loads(requests.get(cls._base_url+"/en/API/Top250Movies/k_kymjglxh").content)
        dict1 = all_movie['items']
        print('Rank :')
        for i in range(len(dict1)):
            List = dict1[i]
            if List['id'] == id : 
                return List['rank']
        
        
