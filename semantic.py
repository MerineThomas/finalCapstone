import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

#Checking the similarity between cat, monkey and banana
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

#Checking similarity between cat,apple,monkey and banana
tokens = nlp('cat apple monkey banana')

for token1 in tokens:
    for token2 in tokens:
        print(f"{token1.text} <-> {token2.text} :", token1.similarity(token2))

#Example of my own
tokens_3 = nlp('bread sandwich car wheat human')

for token3 in tokens_3:
    for token4 in tokens_3:
        print(f"{token3.text} <-> {token4.text} :", token3.similarity(token4))
              
#Checking the similarity for the sentences
sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)