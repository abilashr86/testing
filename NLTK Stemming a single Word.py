
# coding: utf-8

# NLTK Stemming a single Word

# Stemming is a rudimentary rule-based process of stripping the suffixes (“ing”, “ly”, “es”, “s” etc) from a word.

# In[3]:


from nltk.stem.porter import PorterStemmer
lem= PorterStemmer()


# In[6]:


print(lem.stem("gamers"))

