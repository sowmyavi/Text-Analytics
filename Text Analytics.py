#!/usr/bin/env python
# coding: utf-8

# The project is centered on creating a tool for language translation and text analysis using Python, featuring a range of functions for handling and analyzing text data. Here's an overview of its primary capabilities:
# 
# - Text Processing:
#   - The project encompasses routines for reading texts from files, eliminating punctuation, segmenting texts into sentences, and generating lists of words from these sentences.
#   - A function named read_file retrieves text content from a file, returning it as a string.
#   - The remove_punc2 function strips punctuation from the text, yielding a cleaned version.
# 
# - Language Translation:
#   - The tool includes a feature for translating English words into Latin.
#   - The translate function employs a rule-based method to convert English words into Latin, relocating consonants before the first vowel to the end and appending 'ay' as a suffix.
# 
# - Text Analysis:
#   - There are several functions designed for text analysis and manipulation.
#   - The split_sentences function breaks a text string into individual sentences based on punctuation marks like '.', '?', and '!'.
#   - The starts_with_vowel function determines whether a string begins with a vowel.
# 
# - Social Network Analysis:
#   - The tool also provides functionality for analyzing social network dynamics.
#   - The list_textfiles function compiles a list of '.txt' files within a specific directory.
#   - Social relationships are parsed from a file and mapped in a dictionary (edge_dict).
#   - Using edge_dict, the following2 function identifies the users followed by a specific individual.
# 
# - Performance Evaluation:
#   - Execution times for particular functions are measured using the %timeit magic command.
#   - In summary, this project integrates language translation, text processing, and social network analysis tools, offering a comprehensive suite for processing and examining textual and social network data, alongside translating English to Latin.

# In[1]:


# Importing the data
infile = open('/Users/sowmya/Downloads/austen-emma-excerpt.txt')
print(infile)
text = infile.read()
print(text.count("e"))
print(text.count('an'))
infile.close()


# In[3]:


#The program processes a text to tally how many times the letter 'e' appears within it. 
#Afterward, it outputs the original text along with the count of 'e' instances.
nE = 0
print(text)
for x in text:
    if 'e' in x:
        nE = nE + x.count('e')

print(nE)


# In[4]:


print(text.count(' an '))


# In[5]:


#This code calculates how many times the letter 'e' appears in the text string, saves that number in the counts variable, and then displays the count.
counts = 0 
item_to_count = text
for txt in text:
    if 'e' == txt:
        counts = counts + 1

print(counts)


# In[6]:


# The `remove_punc2` function removes punctuation characters from the `text` string and returns the cleaned version.
def remove_punc2(text):
    punctuation = '!@#$%^&*()_-+={}[]:;"\'|<>>,.?/~`»¿'
    clean_text = ""
    for character in text:
        if character not in punctuation:
            clean_text += character
    return clean_text


# In[7]:


for element in enumerate("Python"):
    print(element)


# In[8]:


for index, character in enumerate("Python"):
    print(index)


# In[11]:


def end_of_sentence_marker(character):
    if character == '?':
        return True
    elif character == '!':
        return True
    elif character == '.':
        return True
    else:
        return False


# In[12]:


print(end_of_sentence_marker('?') == True)


# In[13]:


print(end_of_sentence_marker("a"))


# In[14]:


for element in enumerate('Python'):
    print(element)


# In[15]:


for index, character in enumerate("Python"):
    print(index)


# In[16]:


# The split_sentences function takes a text string as input and splits it into a list of sentences.
def split_sentences(text):
    #"Split a text string into a list of sentences."
    sentences = []
    start = 0
    for end, character in enumerate(text):
        if end_of_sentence_marker(character):
            sentence = text[start: end + 1]
            sentences.append(sentence)
            start = end + 1
    return sentences


# In[17]:


splitedSentences = split_sentences("This is a sentence. Should we seperate it from this one?")


# In[18]:


#The code takes each sentence from the splitedSentences list, cleans it by trimming spaces, removing punctuation, and changing to lowercase.
#Then it splits the sentence into words and prints the list of words for each sentence.
for index,sent in enumerate(splitedSentences):
    wordList = []
    sent = sent.strip()
    cleanText = remove_punc2(sent)
    lowerSent = cleanText.lower()
    wordList = lowerSent.split(' ')
    print(wordList)


# In[23]:


# the code reads a file containing follower and followee names, extracts the pairs of names, 
# and stores them in a list named edges. It then prints the first 10 pairs of follower and followee names.

edges = [] # In twitterName.txt we have list of names in the format as 'follower','followee'
for line in open('/Users/sowmya/Downloads/twitterName.txt'):
    follower,followee = line.strip().split(';')
    edges.append((follower,followee))
print(edges[:10])


# In[24]:


def following(user, edges):
    "Return a list of all users USERS is following."
    followees = []
    for follower, followee in edges:
        if follower == user:
            followees.append(followee)
    return followees

print(following("@Fox", edges)) # The User Fox(follower) is following 6 People


# In[25]:


get_ipython().run_line_magic('timeit', 'following("@Fox", edges)')


# In[32]:


edge_dict = {}
for line in open("/Users/sowmya/Downloads/twitterName.txt"):
    name_a, name_b = line.strip().split(';')
    if name_a in edge_dict:
        edge_dict[name_a].append(name_b)
    else:
        edge_dict[name_a] = [name_b]


# In[33]:


edge_dict


# In[34]:


def following2(user, edges):
    return edges[user]

get_ipython().run_line_magic('timeit', 'following2("@Fox", edge_dict)')


# In[35]:


edges = []
for line in open("/Users/sowmya/Downloads/twitterName.txt"):
    name_a, name_b = line.strip().split(';')
    # repeatedly add edges to the network (1000 times)
    for i in range(1000):
        edges.append((name_a, name_b))


# In[36]:


get_ipython().run_line_magic('timeit', 'following("@Fox", edges)')


# The code imports a file with names of followers and followees, constructs a edge_dict dictionary to represent their social network connections, and calculates how long it takes to run the following2 function for the user "@Fox" using this dictionary.

# In[37]:


edge_dict = {}
for line in open("/Users/sowmya/Downloads/twitterName.txt"):
    name_a, name_b = line.strip().split(';')
    for i in range(1000):
        if name_a in edge_dict:
            edge_dict[name_a].append(name_b)
        else:
            edge_dict[name_a] = [name_b]

get_ipython().run_line_magic('timeit', 'following2("@Fox", edge_dict)')


# The code changes an English word to Latin by shifting the initial consonants to the end and appending 'ay' to it.

# In[38]:


# English to Latin
def translate(word):
    "Convert a word to latin."
    vowels = 'aeiouAEIOU'
    start = 0
    end = ''
    # loop over all characters in word
    for i, char in enumerate(word):
        # if this character is not a vowel
        if char not in vowels:
            # it is a consonant, so add it to the end.
            end += char
        # if it is a vowel
        else:
            # we set the starting position to 
            # the position of this character
            start = i
            break
    return word[start:] + end + 'ay'

translate('Practice')


# In[39]:


#Method 1
def starts_with_vowel(strings):
    vowels = 'aeiouAEIOU'
    if strings[0] in vowels:
        return True
    else:
        return False

starts_with_vowel('Amazing')
starts_with_vowel('Jack')


# In[40]:


#Method 2
def starts_with_vowel(word):
    "Return True if WORD starts with a vowel, False otherwise."
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    return word.startswith(vowels)


# In[41]:


def add_suffix(word,suffix):
    word_suffix = word + suffix
    return word_suffix

add_suffix('luck','ily')


# In[42]:


word = 'quick' 
add_suffix(word,'ly')


# The code translates a word by altering its letter order and adding a suffix, depending on if it starts with a vowel. It recursively calls the translate function, adjusting the word each time to achieve the translation.

# In[43]:


def translate(word, suffix):
    if starts_with_vowel(word):
        return add_suffix(word, suffix)
    return translate(word[1:] + word[0], suffix)

translate('JkcEEEE','Amazing')


# In[ ]:




