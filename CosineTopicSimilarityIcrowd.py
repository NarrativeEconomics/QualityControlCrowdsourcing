# -*- coding: utf-8 -*-
__author__ = 'Arwa Shaker'
"""this code is a replica to the cosine(topic) similarity that achieved the best performance compared to
 jaccard and cosine(TF-IDF)"""


doc1 = "Sugar is bad to consume. My sister likes to have sugar, but not my father."
doc2 = "My father spends a lot of time driving my sister around to dance practice."
doc3 = "Doctors suggest that driving may cause increased stress and blood pressure."
doc4 = "Sometimes I feel pressure to perform well at school, but my father never seems to drive my sister to do better."
doc5 = "Health experts say that Sugar is not good for your lifestyle."

# compile documents
doc_complete = [doc1, doc2, doc3, doc4, doc5]

# Cleaning and Preprocessing
# Cleaning is an important step before any text mining task, in this step,
# we will remove the punctuations, stopwords and normalize the corpus.


from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()
def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

doc_clean = [clean(doc).split() for doc in doc_complete]

# Preparing Document-Term Matrix
# All the text documents combined is known as the corpus. To run any mathematical model on text corpus,
# it is a good practice to convert it into a matrix representation. LDA model looks
# for repeating term patterns in the entire DT matrix. Python provides many great libraries
# for text mining practices, “gensim” is one such clean and beautiful library to handle text data.
# It is scalable, robust and efficient.
# Following code shows how to convert a corpus into a document-term matrix.

# Importing Gensim
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
import gensim

from gensim import corpora

# Creating the term dictionary of our courpus, where every unique term is assigned an index.
dictionary = corpora.Dictionary(doc_clean)

# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

# Running LDA Model
# Next step is to create an object for LDA model and train it on Document-Term matrix.
# The training also requires few parameters as input which are explained in the above section.
# The gensim module allows both LDA model estimation from a training corpus and inference of topic
# distribution on new, unseen documents.

# Creating the object for LDA model using gensim library
Lda = gensim.models.ldamodel.LdaModel

# Running and Trainign LDA model on the document term matrix.
ldamodel = Lda(doc_term_matrix, num_topics=3, id2word = dictionary, passes=50)

print(ldamodel.print_topics(num_topics=3, num_words=3))