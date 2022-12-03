import streamlit as st
import pandas as pd
import numpy as np
from Movie_module.api_request import APIRequest
from PIL import Image
import requests
from io import BytesIO



st.title('What film are you looking for?')

title = st.text_input("Enter the title of your movie : ")
result = st.button('valid')

if result :
    #Title films 
    all_movie_title, l = APIRequest.get_title(title)
    print(l) # Problem ça sort toujours 25 
    st.text('We found:')
    st.text(l)

    #Poster films 
    all_poster = APIRequest.get_poster(title)

    #Id films 
    All_id = APIRequest.get_id(title)


    for i in range(len(all_movie_title)):
        #st.button('more information')
        st.title(all_movie_title[i])
        poster = requests.get(all_poster[i])
        #print(poster)
        #Récupéraration de l'id de chaque films
        id = all_poster[i]
        if poster.content == 'http://not available' :
            img = Image.open(BytesIO('https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.123rf.com%2Fstock-photo%2Fnot_available.html&psig=AOvVaw2GDoha3vAGubsIr-rClJAF&ust=1669717317881000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCJjf8e7T0PsCFQAAAAAdAAAAABAE'))
            st.image(img, caption='movie poster')
        else : 
            img = Image.open(BytesIO(poster.content))
            st.image(img, caption='movie poster')
        with st.expander("See more"):
            rank = APIRequest.get_rank(id)
            st.text(rank)