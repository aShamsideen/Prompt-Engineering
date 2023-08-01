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

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
    model=model,
    messages=messages,
    temperature=temperature)
    print(str(response.choices[0].message))
    return response.choices[0].message["content"]


# In[3]:


def collect_messages(_):
    prompt = inp.value_input
    inp.value = ''
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':f"{response}"})
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response, width=600, style={'background-color': '#F6F6F6'})))
 
    return pn.Column(*panels)


# In[4]:


import panel as pn  # GUI
pn.extension()

panels = [] # collect display 

context = [ {'role':'system', 'content':"""
You are an AI Advisor in Balogun Capitals, an automated service \
that advise prospective clients on investment options that is \
best suited to their risk assessment profile. Greet the client, \
then ask questions focused solely on risk assessment to determine \
the client's risk profile. \
Generate personalized portfolio options based on \
the risk assessment. Lastly, provide detailed explanation \
of each portfolio option and its holdings. \

The next question should be asked after the client has \
provided answer to the previous question.
"""} ]

inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
button_conversation = pn.widgets.Button(name="Chat!")

interactive_conversation = pn.bind(collect_messages, button_conversation)

dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)

dashboard


# In[ ]:




