"""
Description: This Python code implements a Markov chain based NLP model to generate random text based on a given corpus. The model is trained on two corpora - one from the Balaji's TNS and his book recommendations and the other from Shakespeare's plays. The model generates a random sentence by combining the two corpora with weights assigned to each corpus.

Args:
path (string): the path to the Balaji TV serial transcript.
balaji_weight (float, optional): weight assigned to the Balaji corpus (default is 1).
shakespeare_weight (float, optional): weight assigned to the Shakespeare corpus (default is 1).

Returns: 
A sentence generated using markov chains.

"""

import markovify
import re
import spacy
import nltk
from nltk.corpus import gutenberg

nltk.download('gutenberg')    # Dowmload the required text corpus
nlp = spacy.load('en_core_web_sm')


"""
Description: This function returns a string containing the concatenated sentences from three Shakespearean plays: Hamlet, Macbeth, and Julius Caesar. The function reads the texts from the NLTK Gutenberg corpus, removes the chapter headings, cleans the text, and uses Spacy to tokenize the text into sentences.

Args: None.

Returns:
shakespeare_sents (string): a string containing the concatenated sentences from the three plays.

"""

def get_shakespeare_corpus():
    # Load the text of three of Shakespeare's plays
    hamlet = gutenberg.raw('shakespeare-hamlet.txt')
    macbeth = gutenberg.raw('shakespeare-macbeth.txt')
    caesar = gutenberg.raw('shakespeare-caesar.txt')
    
    # Remove the chapter headings from the texts
    hamlet = re.sub(r'Chapter \d+', '', hamlet)
    macbeth = re.sub(r'Chapter \d+', '', macbeth)
    caesar = re.sub(r'Chapter \d+', '', caesar)
    
    # Clean up the text using the text_cleaner function
    hamlet = text_cleaner(hamlet)
    caesar = text_cleaner(caesar)
    macbeth = text_cleaner(macbeth)
    
    # Use the language model to parse the cleaned text into sentences
    hamlet_doc = nlp(hamlet)
    macbeth_doc = nlp(macbeth)
    caesar_doc = nlp(caesar)
    
    # Concatenate all the sentences from the three plays into a single string
    hamlet_sents = ' '.join([sent.text for sent in hamlet_doc.sents if len(sent.text) > 1])
    macbeth_sents = ' '.join([sent.text for sent in macbeth_doc.sents if len(sent.text) > 1])
    caesar_sents = ' '.join([sent.text for sent in caesar_doc.sents if len(sent.text) > 1])
    shakespeare_sents = hamlet_sents + macbeth_sents + caesar_sents
    
    # Return the concatenated string of sentences
    return shakespeare_sents


"""
Description: This function reads the contents of a file located at the given path and returns it as a string.

Args:
path (string): the path to the file to be read.

Returns:
text (string): the contents of the file as a string.

"""

def read_file(path):
  with open(path) as f:    # open the file in read mode
    text = f.read()        # read the contents of the file
  return text              # return the read text


"""
Description: This function takes a string text and performs several cleaning operations on it, including removing double hyphens, removing square brackets and their contents, removing numbers, and removing extra whitespace.

Args:
text (string): the string to be cleaned.

Returns:
text (string): the cleaned string.

"""

def text_cleaner(text):
  # Replace double hyphens with a single space
  text = re.sub(r'--', ' ', text)
  # Remove any text between square brackets
  text = re.sub('[\[].*?[\]]', '', text)
  # Remove any digits or floating point numbers
  text = re.sub(r'(\b|\s+\-?|^\-?)(\d+|\d*\.\d+)\b','', text)
  # Remove any extra spaces
  text = ' '.join(text.split())
  # Return the cleaned text
  return text


"""
Description: This function reads a file located at the given path, cleans the contents of the file using the text_cleaner() function, and returns the cleaned text as a string.

Args:
path (string): the path to the file to be read and cleaned.

Returns:
corpus (string): the cleaned contents of the file as a string.

"""

def text_preprocess(path):
  # Read in the raw text data from the specified file path
  raw_corpus = read_file(path)
  
  # Perform any necessary cleaning or processing on the raw text data
  corpus = text_cleaner(raw_corpus)
  
  # Return the preprocessed corpus data
  return corpus


"""
Description: This class extends the markovify.Text class and adds parts-of-speech (POS) tags to the words in the input text. This is done to improve the quality of the generated text by ensuring that the generated sentences have grammatical structure.

Args: None.

Returns: None.

"""

class POSifiedText(markovify.Text):
    
    # This method splits the input sentence into words and appends a part-of-speech tag to each word.
    # It uses spaCy's language model to tag the words.
    def word_split(self, sentence):
        return ['::'.join((word.orth_, word.pos_)) for word in nlp(sentence)]
    
    # This method joins the words by removing the part-of-speech tag.
    # It extracts the original word from the tagged word and concatenates them with a space.
    def word_join(self, words):
        sentence = ' '.join(word.split('::')[0] for word in words)
        return sentence



"""
    This class represents a text model that is used to generate random sentences based on a given input text corpus. 

    Args:
    - corpus (str): A string representing the input text corpus.

    Attributes:
    - corpus (str): A string representing the input text corpus.
    - model (markovify.Text): A Markov chain-based model used to generate random sentences.

    Methods:
    - ramble(): A method used to generate a single random sentence based on the input text corpus and the Markov chain-based model.

    Usage:
    The `TextModel` class is used to create a Markov chain-based model using an input text corpus. The class takes the corpus as an argument and initializes a `markovify.Text` object based on it. The `ramble` method can then be used to generate a single random sentence based on the model.

    Example:
    ```
    corpus = "This is a sample corpus for testing."
    model = TextModel(corpus)
    print(model.ramble())
    ```

    Output:
    ```
    "This is a sample corpus for testing."
    ```

"""

class TextModel:



  """

  Description: This method initializes an instance of the TextModel class. It takes a string corpus as input and creates a Markov chain model based on the POS-tagged words in the corpus using the POSifiedText class.

  Args:
  corpus (string): the corpus of text to be used to train the model.

  Returns: None.

  """

  def __init__(self, corpus):
    self.corpus = corpus  # store the corpus in the instance variable
    self.model = POSifiedText(corpus, state_size=3)

  """
  Description: This method generates a random sentence using the Markov chain model created in the __init__() method.

  Args: None.

  Returns:  sentence (string): a randomly generated sentence.

  """

  def ramble(self):

    return self.model.make_sentence()


"""
Returns a combined Markov chain model using two text corpora, where the first corpus is a preprocessed text corpus
at the given `path`, and the second corpus is a concatenation of three Shakespeare plays (Hamlet, Macbeth, and Julius Caesar).
The function returns a `model` object that is an instance of the `markovify.Text` class, which is a subclass of the `markovify.Chain` class.

Args:
- path: A string representing the path to a text file containing the first corpus.
- balaji_weight: A float representing the weight to be given to the first corpus in the combined model. This weight determines
                 the likelihood of the output sentences being generated from the first corpus.
- shakespeare_weight: A float representing the weight to be given to the second corpus in the combined model. This weight determines
                      the likelihood of the output sentences being generated from the second corpus.
Returns:
- model: A `markovify.Text` object that represents the combined Markov chain model.
"""

def get_model(path, balaji_weight, shakespeare_weight):
    # Read and preprocess the Balaji corpus using the text_preprocess function.
    balaji_corpus = text_preprocess(path)
    
    # Create an instance of TextModel class for the preprocessed Balaji corpus.
    miniBalaji = TextModel(balaji_corpus)
    
    # Retrieve the Shakespeare corpus using the get_shakespeare_corpus function.
    shakespeare_sents = get_shakespeare_corpus()
    
    # Create an instance of TextModel class for the Shakespeare corpus.
    classicShakespeare = TextModel(shakespeare_sents)
    
    # Combine the two text models to create a new model using the specified weights.
    model = markovify.combine([miniBalaji, classicShakespeare], [balaji_weight, shakespeare_weight])
    
    # Return the resulting Markov chain-based NLP model.
    return model


"""
A function that runs the Markov Chain-based Natural Language Processing model to generate a sentence.

Args:
- path (str): The path of the text file to use as the primary corpus.
- balaji_weight (float, optional): The weight given to the Balaji corpus. Defaults to 1.
- shakespeare_weight (float, optional): The weight given to the Shakespeare corpus. Defaults to 1.

Returns:
- None

This function first calls the `get_model` function to create a Markov chain model using the Balaji corpus and the
Shakespeare corpus. The `balaji_weight` and `shakespeare_weight` parameters determine the relative contribution of each
corpus to the model. The default weights are equal for both corpora.
After creating the model, this function generates a sentence using the `ramble` method of the model. If an error occurs
during sentence generation, the `make_sentence` method of the model is used as a fallback.
The generated sentence is then printed to the console.
"""

def run(path, balaji_weight = 1, shakespeare_weight = 1):

    model = get_model(path, balaji_weight, shakespeare_weight)

    try:
        # Try to generate a rambling sentence using the trained Markov chain model
        print(model.ramble())
    except:
        # If that fails, generate a single sentence using the trained Markov chain model
        print(model.make_sentence())


if __name__ == "__main__":
    # Call the run function with the specified path
    path = "tns.txt"     # Change to the path of Balaji corpus.
    run(path)
