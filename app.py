import streamlit as st
import pandas as pd
import numpy as np
from Movie_module.api_request import APIRequest
from PIL import Image
import requests
from io import BytesIO


def home_page(st):
    # Display the title and the query bar
    st.title('What film are you looking for?')
    title = st.text_input("Enter the title of your movie : ")
    result = st.button('valid')

    if result :
        #Title films 
        all_movie_title, l = APIRequest.get_title(title) # Get the titles of the movie returned by the query
        st.text(str(l)+'movies find') # Display how many answer were found to the query

        #Poster films 
        all_poster = APIRequest.get_poster(title) # Get the posters of the movie returned by the query

        #Id films 
        All_id = APIRequest.get_id(title) # Get the ids of the movie returned by the query

        
        # Loop for each movie returned by the query
        for i in range(len(all_movie_title)):

            st.title(all_movie_title[i]) # Display the movie title
            poster = requests.get(all_poster[i])
            if poster.content == 'http://not available' : # If no poster available, show a "not available image"
                img = Image.open(BytesIO('https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.123rf.com%2Fstock-photo%2Fnot_available.html&psig=AOvVaw2GDoha3vAGubsIr-rClJAF&ust=1669717317881000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCJjf8e7T0PsCFQAAAAAdAAAAABAE'))
                st.image(img, caption='movie poster')
            else : 
                img = Image.open(BytesIO(poster.content)) # If available, show the movie poster
                st.image(img, caption='movie poster')

            with st.expander("See more"): # Only if the user is interested in the movie : display further informations
                st.text('synopsis:')
                Descr,link = APIRequest.get_trailer(All_id[i])
                st.text(Descr) # Display the movie synopsis
                st.text('Trailer:')
                st.write('Click in the link to view the trailer [link](%s)'% link) # Display a link of the trailer
                st.text('Rank according to the IMDb database :')
                st.text(APIRequest.get_rank(All_id[i])) # Show the ranking of the movie (only if it is in the Top 250)

                st.text('Casting :')
                Cast = APIRequest.get_cast(All_id[i]) # Get the list of actors in the movie
                
                for j in range(len(Cast)) :
                    # For each of the actors, display the name and a picture
                    st.text(Cast['name'][j])
                    image = requests.get(Cast['image'][j])
                    img = Image.open(BytesIO(image.content))
                    st.image(img, caption='actors')
    return st 
