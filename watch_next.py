#=====Class====

class MoviesSimilarity:

    def _init__(self, title, similarity):
        self.title = title
        self.similarity = similarity
        


    



movies = []

with open('movies.txt', 'r+') as f:
    for line in f:
        contents = line.strip().split(',')#
        joined_contents = " ".join(contents)
        movies.append(joined_contents)

print(movies)

#imports spacy and loads model
import spacy
nlp = spacy.load('en_core_web_md')

similarities = []

hulk_to_compare = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.""" 

hulk_nlp = nlp(hulk_to_compare)

for title in movies:
    similarity = nlp(title).similarity(hulk_nlp)
    print(title + " -", similarity)
    

#make an object to store the similarities then make comparison - need to write function 

