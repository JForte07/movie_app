# github_request.py
from pip._vendor import requests
import json
import numpy as np


class APIRequest:
    _base_url = "https://imdb-api.com"
        
    @classmethod
    def get_id(cls, movie_title):
        content = json.loads(requests.get(cls._base_url+"/en/API/SearchMovie/k_92mqgcez/"+ movie_title).content)
        result = content['results']
        List_id =[]
        for i in range(len(result)):
            content_id = result[i]
            Id = content_id['id']
            List_id.append(Id)
        return List_id
    
    @classmethod
    def get_title(cls, movie_title):
        content = json.loads(requests.get(cls._base_url+"/en/API/SearchMovie/k_92mqgcez/"+ movie_title).content)
        result = content['results']
        List_title =[] 
        for i in range(len(result)):
            content_id = result[i]
            title = content_id['title']
            List_title.append(title)
        l = len(List_title)
        return List_title,l 

    @classmethod
    def get_poster(cls,movie_title) : 
        content = json.loads(requests.get(cls._base_url+"/en/API/SearchMovie/k_92mqgcez/"+ movie_title).content)
        result = content['results']
        List_poster =[]
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
        all_movie = json.loads(requests.get(cls._base_url+"/en/API/Top250Movies/k_92mqgcez").content)
        dict1 = all_movie['items']
        List_rank=[]
        for i in range(len(dict1)):
            List = dict1[i]            
            if List['id'] == id : 
                List_rank.append(List['rank'])
        return List_rank

    @classmethod
    def get_cast(cls,id): 
        
        cast = json.loads(requests.get(cls._base_url+"/en/API/FullCast/k_92mqgcez/"+id).content)
        All_actors = cast['actors']
        dict_actors={'name':[],'image':[]}
        for i in range(len(All_actors)):
            Actors = All_actors[i]
            dict_actors['name'].append(Actors['name'])
            dict_actors['image'].append(Actors['image'])
        return dict_actors
        
    @classmethod
    def get_trailer(cls,id):
        info = json.loads(requests.get(cls._base_url+"/en/API/Trailer/k_92mqgcez/"+id).content)
        Description = info['videoDescription']
        LinkVideo = info['link']
        return Description,LinkVideo