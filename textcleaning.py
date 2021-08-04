import re
from bs4 import BeautifulSoup


def decontracted(text):

    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"can\'t", "can not", text)
    text = re.sub(r"she's", "she is", text)
    text = re.sub(r"n't", "not", text)
    text = re.sub(r"what's", "what is", text)
    text = re.sub(r"it's", "it is", text)
    text = re.sub(r"'s", " own", text)
    text = re.sub("%", "percent", text)
    text = re.sub("₹", 'rupee', text)
    text = re.sub("$", "dollar", text)
    text = re.sub("€", "euro", text)
    text = re.sub("cannot", "can not", text)
    text = re.sub(r"n\'t", " not", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'s", " is", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'t", " not", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'m", " am", text)
    return text

def remove_urls(text):


  url_pattern = re.compile(r'https?://\S+|www\.\S+')
  return url_pattern.sub(r'', text)

def remove_numbers(text):

  res=''.join([i for i in text if not i.isdigit()])

  return res


def remove_nonwords(text):
  pattern = re.compile('\W')

  if type(text)==type(''):
    text = re.sub(pattern,' ',text)

  return text

def remove_htmltags(text):

  cleantext = re.compile(r'<[^>]+>').sub('',text) # https://www.geeksforgeeks.org/program-to-remove-html-tags-from-a-given-string/
  cleantext = BeautifulSoup(text, "lxml").text

  return cleantext



def remove_multiple_space(text):


  text = re.sub(' +',' ',text)

  return text

def text_clean(text):
  text=str(text).lower()
  text = decontracted(text)
  text = remove_urls(text)
  text = remove_htmltags(text)
  text = remove_numbers(text)
  text = remove_nonwords(text)
  text = remove_multiple_space(text)
  #text = remove_stopwords(text)
  return text
