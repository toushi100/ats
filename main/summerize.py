import gensim 
from gensim.summarization import summarize
from rouge import Rouge
def summerize(text):
    return summarize(text)



def summerizeByRatio(text,ratio):
    return summarize(text,ratio= ratio)


def summerizeByWordCount(text,count):
    return summarize(text,word_count= count)

def word_count(text):
    text = text.split()
    textcount = len(text)
    return textcount

def precision(text, summed):
    rouge = Rouge()
    f = rouge.get_scores(summed,text)
    print(f)
    p = f[0]['rouge-2']['p']
    return p*100


