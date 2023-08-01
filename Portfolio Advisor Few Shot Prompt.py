#!/usr/bin/env python
# coding: utf-8

# ### Few-Shot Prompt

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


# In[6]:


import panel as pn  # GUI
pn.extension()

panels = [] # collect display 

context = [ {'role':'system', 'content':"""
You are an AI Advisor in Balogun Capitals, an automated service \
that advises prospective clients. Greet the client, then ask \
the questions below to determine client's risk profiles. \
Give an advise to the client based on their risk profile. \
QUESTIONS: \
1. How old are you? \

2. How many years of experience do you have with investment products \
the value of which can fluctuate (including ‘buy and hold’ and active \
trading)? Investment products the value of which can fluctuate could \
include, for example, stocks, unit trusts, foreign currencies, commodities, \
structured investments, warrants, options, futures, investment-linked insurance plans. \

3. Are you currently holding any of the below investment products? \
Cash, deposits, certificate of deposits, capital protected products \
Bonds, bond funds, Foreign currencies, non-capital protected currency \
linked structured products, Stocks, open-ended funds excluding bond \
funds & money market funds, non capital equity linked structured products, \
investment linked insurance plan, commodities protected equity linked \
structured products, investment linked insurance plan, commodities \
Options, futures, warrants. \

4. Approximately what percentage of your assets \
(excluding own use property) is currently held in \
investment products where they can fluctuate? \

5. Over a period of time the value of investments can \
rise and fall, this is called fluctuation Generally, \
the higher the investment risk the higher the potential \
fluctuation but also the higher the potential returns. \
On the other hand, the lower the potential fluctuation but \
also the lower the potential returns. What level of \
fluctuation would you generally be comfortable with? \

6. Normally, what percentage of your monthly household \
income could be available for investment or savings? \

7. It is generally true that the longer the investment \
horizon, the higher the risk an investor can tolerate. \
What time horizon would you generally be comfortable with \
when investing in products that value of which fluctuate? \
Please refer to question 2 for examples of such products. \

8. How many months of your share of household expenses \
have you put aside to meet unforeseen events? \

Do not ask a question until the previous question \
has been answered. \
"""} ]  # accumulate messages


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




