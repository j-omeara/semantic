# import spacy and assign nlp
import spacy
nlp = spacy.load('en_core_web_md')

# first code extract
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))