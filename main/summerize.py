import gensim 
from gensim.summarization import summarize

def summerize(text):
    return summarize(text)



def summerizeByRatio(text,ratio):
    return summarize(text,ratio= ratio)


def summerizeByWordCount(text,count):
    return summarize(text,word_count= count)