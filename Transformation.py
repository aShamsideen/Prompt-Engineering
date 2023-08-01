#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env key

openai.api_key = os.getenv('OPENAI_API_KEY')


# In[2]:


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
    model=model,
    messages=messages,
    temperature=0,
    )
    return response.choices[0].message["content"]


# In[3]:


prompt = f"""
Translate the following Enlgish to Hausa: \
```I would love to go on adventure.```
"""

response = get_completion(prompt)
print(response)


# In[4]:


prompt = f"""
Tell me which language this is:
```Kini oruko re?```
"""

response = get_completion(prompt)
print(response)


# In[5]:


prompt = f"""
Translate the follwoing text to Yoruba and Hausa
and Igbo: \
```I want to order a basketball```
"""

response = get_completion(prompt)
print(response)


# In[6]:


prompt = f"""
Translate the following text to Spanish in both the \
formal and infromal form:
'Do you care for a cup of coffee?'
"""

response = get_completion(prompt)
print(response)


# In[3]:


user_messages = [
    "Aga'm acho ka mu na gi hu taa ta."
]


# In[4]:


for issue in user_messages:
    prompt = f"Tell me what language this is: ```{issue}```"
    lang = get_completion(prompt)
    print(f"Original message ({lang}): {issue}")
    
    prompt = f"""
    Translate the following text to English \
    and Yoruba: ```{issue}``` 
    """
    response = get_completion(prompt)
    print(response, "\n")


# In[9]:


prompt = f"""
Translate the following from slang to a letter:
'Yup bro! What'up with our trip to the North later in the week?
"""

response = get_completion(prompt)
print(response)


# In[10]:


data_json = {"restaurant employees" :[
    {"name": "Sunbo", "email": "agbolahan85@yahoo.com"},
    {"name": "Sam", "email": "sammy1759@gamil.com"},
    {"name": "Kayode", "email": "kayelenu1809@gmail.com"}
]}

prompt = f"""
Translate the following python dictionary from JSON to an HTML
table with column headers and title: {data_json}
"""

response = get_completion(prompt)
print(response)


# In[12]:


from IPython.display import display, Markdown, Latex, HTML, JSON
display(HTML(response))


# In[14]:


text = [
    "The girl with the black and white puppies have a ball.",
    "Yolanda has her notebook.",
    "Its going to be a long day. Does the need it's oil changed."
]
for t in text:
    prompt = f"Proofread and correct: ```{t}```"
    response = get_completion(prompt)
    print(response)


# In[20]:


text = [
    "The girl with the black and white puppies have a ball.",
    "Yolanda has her notebook.",
    "Its going to be a long day. Does the need it's oil changed."
]
for t in text:
    prompt = f"""Proofread and correct the following text
    and rewrite the corrected version. If you don't find
    any errors, just say "No errors found":
    ```{t}```"""
    response = get_completion(prompt)
    print(response)


# In[16]:


text = f"""
Got this for my daughter for her birthday cuz she keeps taking \
mine from my room. Yes, adults also like pandas too. She took \
it everywhere with her, and its super soft and cute. One of the \
ears is a bit lower than the other, and I don't think that was \
designed to be assymetrical. It's a a bit small for what i paid \
though. I think there might be other options that are bigger for \
for the same price. It arrived a day earlier than expected, so I \
got to play with it myself before i gave it to my daughter. \
"""

prompt = f"Proofread and correct this review: ```{text}```"
response = get_completion(prompt)
print(response)


# In[18]:


from redlines import Redlines
diff = Redlines(text, response)
display(Markdown(diff.output_markdown))


# In[19]:


prompt = f"""
proofread and correct this review. Make it more compelling.
Ensure it follows APA style guide and targest an advanced response.
Output in markdown format.
Text: ```{text}```
"""
response = get_completion(prompt)
display(Markdown(response))

