#======MODELS=====

#imports spacy and loads model
import spacy
nlp = spacy.load('en_core_web_md')

#=====Class====

class Movies:
    def __init__(self, title, description):
        self.title = title
        self.description = description


    def __str__(self):
        output = f"====={self.title}=====\n"
        output += self.description

        return(output)
    

    



#====Functions========
def read_movie_from_f():
    movie_list = []

    with open('movies.txt', 'r+') as f:
        for line in f:
            contents = line.strip().split(',') #strip characters and split each line into a list item
            joined_contents = " ".join(contents) #changed to string to split title/description by semicolon
            split_contents = joined_contents.split(":") #split string by semicolon making a two list item
            title = split_contents[0]
            description = split_contents[1]
            movie_object = Movies(title, description)
            movie_list.append(movie_object)
        
    return(movie_list)



#=======Program========


movie_to_compare = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.""" 

movie_to_compare_nlp = nlp(movie_to_compare)

#reads all movies into program
all_movies = read_movie_from_f()

similarities = []

#checks similarity of descriptions between movies using NLP


def similarity_check(list_of_movies, movie_to_compare_nlp):
    for movies in all_movies:
        movie_description = movies.description
        similarity = nlp(movie_description).similarity(movie_to_compare_nlp)
        rounded_similarity = round(similarity, 2)
        similar_title = movies.title
        similar_description = movies.description
        similarity_score = rounded_similarity
   
        return(similar_title, similar_description, similarity_score)

answer = similarity_check(all_movies, movie_to_compare_nlp)
print(answer[0])




#new object with rounded similarity 







































