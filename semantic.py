import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

print("--------")

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print("--------")

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

# Cat and monkey are similar because they are both animals
# Monkey and banana seem to have similarities because it recognises monkey eat bananas (and cat's don't)
# Banana and apple are similar because they are both fruits.

# When running the example file with the ‘en_core_web_sm’ language model I noticed that the numbers returned
# tended to be less with the simpler model.  I presume this is because the more advanced 'en_core_web_md' model
# has more ability to identify similarities and therefore returns, generally, more favourable comparisons.

# The ‘en_core_web_sm’ model also has no word vectors loaded, so the results are based on the tagger, parser and NER,
# which may not give useful similarity judgements - hence the generally lower similarity scores.