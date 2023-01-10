import spacy
nlp = spacy.load('en_core_web_md')

# Open and read in the data from the file.
file = open("movies.txt", "r")
lines = file.readlines()
file.close()

# Empty list to store the contents of the file.
descriptions = []

# Data in the file is read, new line characters striped and then split where there is a colon.
# The data is then appended to the descriptions list
for line in lines:
    temp = line.strip()
    temp = temp.split(":")
    descriptions.append(temp)

# Empty list to store the similarity data (once obtained)
similarities = []

hulk = """Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""

model_sentence = nlp(hulk)

# Will loop for the contents of the descriptions list
# Similarities are checked each iteration - the data is appended to the similarities list
for x in range(len(descriptions)):
    similarities.append(nlp(descriptions[x][1]).similarity(model_sentence))

# The object with the number closest to 1.0 is obtained and its index position found.
# This is then output to the screen using an f string.
max_similarity = max(similarities)
max_similarity_index = similarities.index(max_similarity)

print(f"With a similarity score of {max_similarity}, the most similar movie is {descriptions[max_similarity_index][0]}")


