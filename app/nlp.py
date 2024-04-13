import spacy

# Load the English language model
nlp = spacy.load('en_core_web_sm')

# Process the text document
doc = nlp('The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France.')

# Display the named entities found in the document
for ent in doc.ents:
    print(ent.text, ent.label_)
