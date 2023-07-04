import spacy
nlp = spacy.load('en_core_web_md')

#Function that takes in the description and predicts the next possible movie to watch
def next_movie(description,f):
    similar_dict = {} #Dictionary to hold similarity values
    parsed_desc = nlp(description)
    for sentence in f:
        #checking the similarity between the input description and the one from the file
        similarity = nlp(sentence).similarity(parsed_desc)
        sentence_split = sentence.split(":") #Splitting the sentence from the file
        similar_dict[sentence_split[0]] = similarity #Assign the value against the movie name
        #Sorting the dictionary based on similarity values
        new_value = sorted(similar_dict.items(),key=lambda x:x[1], reverse=True)   
    return new_value[0][0]

#Planet Hulk description
planet_hulk = u"Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the illuminati trick Hulk into a shuffle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."

try: 
    #file open, calling the function and printing the output
    f = open("T21/movies.txt", "r")
    sim = next_movie(planet_hulk,f)
    print(sim)

except BaseException as be:
    print(be)

finally:
    f.close()

