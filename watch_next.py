# This is the function crated ----->>>>>>>>
'''
import spacy

nlp = spacy.load('en_core_web_md')

def find_similar_movie(description):
    # Load movie descriptions from the file
    file_path = "movies.txt"
    with open(file_path, "r") as file:
        movie_descriptions = file.readlines()

    # Initialize variables for tracking the most similar movie
    max_similarity = -1
    most_similar_movie = ""

    # Iterate over each movie description and calculate similarity
    for movie_description in movie_descriptions:
        # Remove leading/trailing whitespace and newline characters
        movie_description = movie_description.strip()

        # Calculate similarity between the input description and the movie description
        similarity = nlp(description).similarity(nlp(movie_description))
        
        # Check if the current movie has higher similarity
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_movie = movie_description

    return most_similar_movie

# Read in the movie descriptions from the file
file_path = "movies.txt"
with open(file_path, "r") as file:
    movie_descriptions = file.readlines()

# Test the function
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
similar_movie = find_similar_movie(description)
print("The most similar movie is:", similar_movie)

'''

# --> The function should take in the description as a parameter and return the
#     title of the most similar movie:

import spacy

nlp = spacy.load('en_core_web_md')

def find_similar_movie(description):
    # Load movie descriptions from the file
    file_path = "movies.txt"
    with open(file_path, "r") as file:
        movie_data = file.readlines()

    # Calculate similarity between the input description and each movie description
    similarity_scores = []
    for desc in movie_data:
        similarity = nlp(description).similarity(nlp(desc))
        similarity_scores.append((desc, similarity))

    # Sort the similarity scores in descending order
    similarity_scores.sort(key=lambda x: x[1], reverse=True)

    # Return the description of the most similar movie
    most_similar_movie = similarity_scores[0][0]
    return most_similar_movie

# Test the function
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
similar_movie = find_similar_movie(description)
print("The most similar movie description is:", similar_movie)
