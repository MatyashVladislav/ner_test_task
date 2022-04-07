#!/usr/bin/env python
# coding: utf-8

# In[1]:


import spacy


# In[2]:


def create_list_ents(text, lg_code):
    if lg_code=='en':
        nlp = spacy.load('en_core_web_sm')
    elif lg_code=='xx':
        nlp = spacy.load('xx_ent_wiki_sm')
    else:
        nlp = spacy.load(f'{lg_code}_core_news_sm')
    ent_list = []
    doc = nlp(text)
    if doc.ents:
        for ent in doc.ents:
            ent_dict = {}
            ent_dict['text'] = ent.text
            ent_dict['type'] = spacy.explain(ent.label_)
            ent_dict['start_pos'] = ent.start_char
            ent_dict['end_pos'] = ent.end_char
            
            ent_list.append(ent_dict)
    else: 
        print('No named entities found.')
    return ent_list


# In[3]:


text = "Apple is looking at buying U.K. startup for $1 billion"
create_list_ents(text, 'en')


# In[4]:


text = "Apple фирма созданная Стивом Джобсом"
create_list_ents(text, 'ru')


# In[ ]:




