# Evil Balaji

This Python code implements a Markov chain based NLP model to generate tweets in the style of Balaji Srinivasan with a Shakespearean twist. The model is trained on two corpora - one from Balaji's TNS and his book recommendations and the other from Shakespeare's plays. The model generates a random sentence by combining the two corpora with weights assigned to each corpus.

# Installation

To install Evil-Balaji, follow the steps below:

1. Ensure that you have Python 3.6 or later installed on your system.

2. Clone or download the Evil-Balaji repository from GitHub: https://github.com/hitbug-exe/Evil-Balaji

3. Open a terminal or command prompt and navigate to the root directory of the cloned or downloaded repository.

4. Install Evil-Balaji using pip by running the following command:

   `pip install .`

5. Once the installation is complete, you can import the Evil-Balaji package in your Python code and start using it.

# Improvements

To improve the quality of the generated text, you can extend the corpus used to train the model. You can add more of Balaji's writings, as well as additional works by Shakespeare. To add more Balaji writings, simply add them to the corpus file specified by the path argument when creating the BalajiShakespeareanTweetGenerator instance. To add more works by Shakespeare, you can download additional plays from the NLTK Gutenberg corpus and concatenate their contents in the get_shakespeare_corpus() function.

# References

https://github.com/jsvine/markovify#basic-usage

https://towardsdatascience.com/text-generation-with-markov-chains-an-introduction-to-using-markovify-742e6680dc33

# License

Evil Balaji is released under the MIT License. Feel free to use, modify, and distribute it as you see fit.

