from Movie_module.api_request import APIRequest
from Movie_module.input_text import InputText

movie_title = InputText.input_text()
#print(movie_title)
Id = APIRequest.get_id(movie_title)
casting = APIRequest.get_cast(Id)
rank = APIRequest.get_rank(Id)

print(Id,casting,rank)
