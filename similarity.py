#======MODELS=====

#imports spacy and loads model
import spacy
nlp = spacy.load('en_core_web_md')

#=====Class====

#creates movie class 
class Movies:
    def __init__(self, title, description):
        self.title = title
        self.description = description


    def __str__(self):
        output = f"====={self.title}=====\n"
        output += self.description

        return(output)
    

#====Functions========

#reads movies from txt file into program. 
def read_movie_from_f():
    movie_list = []

    with open('movies.txt', 'r+') as f:
        for line in f:
            contents = line.strip().split(',') #strip characters and split each line into a list item
            joined_contents = " ".join(contents) #changed to string to split title/description by semicolon
            split_contents = joined_contents.split(":") #split string by semicolon making a two list item
            title = split_contents[0]
            description = split_contents[1]
            movie_object = Movies(title, description)   #creates movie object to store information
            movie_list.append(movie_object) #appends movie object to movie list.
        
    return(movie_list)

#Function uses NLP t check similarity of user provided movie description against list of movies. 
def similarity_check(list_of_movies, movie_to_compare_nlp):
    for movies in all_movies:
        movie_description = movies.description
        similarity = nlp(movie_description).similarity(movie_to_compare_nlp)    #NLP on movie descriptions
        rounded_similarity = round(similarity, 2)
        similar_title = movies.title 
        similar_description = movies.description
        similarity_score = rounded_similarity
   
        return(similar_title, similar_description, similarity_score)

#=======Program========

#Welcome message
print("=====Movie Roulette=====")
print("""
Just enter the description of your favourite movie
in the section below. And we will use our state of the
art Machine Learning to give you a suggestion! 
Get your popcorn ready!\n""")

#User input of movie description
user_suggestion = str(input("Please paste your description here: "))

movie_to_compare = user_suggestion

#apply NLP module to movie descritpion given by user
movie_to_compare_nlp = nlp(movie_to_compare)

#reads all comparisson movies into program
all_movies = read_movie_from_f()

#checks similarity of descriptions between movies using NLP

most_similar_movie = similarity_check(all_movies, movie_to_compare_nlp)

suggested_title = most_similar_movie[0]
suggested_description = most_similar_movie[1]
similarity_score = most_similar_movie[2]

#Presents similar movie to user. 
print(" ")
print(f"We suggest watching: {suggested_title} which scored {similarity_score}")
print(suggested_description)







































