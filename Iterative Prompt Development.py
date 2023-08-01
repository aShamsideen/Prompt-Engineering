#!/usr/bin/env python
# coding: utf-8

# In[43]:


import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env key

openai.api_key = os.getenv('OPENAI_API_KEY')


# In[44]:


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
    model=model,
    messages=messages,
    temperature=0,
    )
    return response.choices[0].message["content"]


# In[49]:


fact_sheet_chair = f"""
OVERVIEW
- Part of a beautiful family of mid-century inspired office furniture 
including filling cabinets, desks, bookcases, meeting tables, file desks. 
- Several options of shell color nad base finishes.
- Available with plastic back and front upholstery (SWC-100)
or full upholstery (SWC-110) in fabric and in leather option.
- Base finish options are: stainless steel, matte black,
gloss white or chrome.
- Chair is available with or without armrests.
- Suitable for home or business setting.
- Qualified for contract use.

CONSTRUCTIONS
- 5-wheel plastic coated aluminum base
- Pneumatic chair adjust for easy raise/lower action

DIMENSIONS
- WIDTH 53 CM | 20.87"
- DEPTH 51 CM | 20.08"
- HEIGHT 80 CM | 31.5"
- SEAT HEIGHT 44 CM | 17.32"
- SEAT DEPTH 41 CM | 16.14"

OPTIONS
- Soft or hard floor catser options.
- Two choices of seat from densities:
 medium (1.8 lb/ft3) or high (2.8 lb/ft3)
- Armless or 8 position PU armrests

MATERIALS
SHELL BASE GLIDER
- CASt aluminum with modified nylon PA6/PA66 coakting.
- Shell thickness: 10mm.
SEAT
-HD36 foam

COUNTRY OF ORIGIN
- Italy
"""


# In[50]:


prompt = f"""
Your task is to help a marketing team create a 
description for a retail website of a product based 
on a technical fact sheet.

Write a product description based on the information 
provided in the technical specifications delimited by 
triple backticks.

Technincal specifications: ```{fact_sheet_chair}```
"""

response = get_completion(prompt)
print(response)


# In[51]:


prompt = f"""
Your task is to help a marketing team create a 
description for a retail website of a product based 
on a technical fact sheet.

Write a product description based on the information 
provided in the technical specifications delimited by 
triple backticks.

Use at most 50 words

Technincal specifications: ```{fact_sheet_chair}```
"""

response = get_completion(prompt)
print(response)


# In[52]:


len(response.split(" "))


# In[53]:


prompt = f"""
Your task is to help a marketing team create a 
description for a retail website of a product based 
on a technical fact sheet.

Write a product description based on the information 
provided in the technical specifications delimited by 
triple backticks.

Use at most 3 sentences

Technincal specifications: ```{fact_sheet_chair}```
"""

response = get_completion(prompt)
print(response)


# In[64]:


prompt = f"""
Your task is to help a marketing team create a 
description for a retail website of a product based 
on a technical fact sheet.

Write a product description based on the information 
provided in the technical specifications delimited by 
triple backticks.

Use at most 250 characters.

Technincal specifications: ```{fact_sheet_chair}```
"""

response = get_completion(prompt)
print(response)


# In[65]:


len(response)


# In[37]:


prompt = f"""
Your task is to help a marketing team create a 
description for a retail website of a product based 
on a technical fact sheet.

Write a product description based on the information 
provided in the technical specifications delimited by 
triple backticks.

The description is intended for furniture retailers,
so should be technical in nature and focus on the 
materials the product is constructed from.

Use at most 50 words

Technincal specifications: ```{fact_sheet_chair}```
"""

response = get_completion(prompt)
print(response)


# In[15]:


len(response.split(" "))


# In[38]:


prompt = f"""
Your task is to help a marketing team create a 
description for a retail website of a product based 
on a technical fact sheet.

Write a product description based on the information 
provided in the technical specifications delimited by 
triple backticks.

The description is intended for furniture retailers,
so should be technical in nature and focus on the 
materials the product is constructed from.

At the end of the description, include every 7-character
Product ID in the technical specification 

Technincal specifications: ```{fact_sheet_chair}```
"""

response = get_completion(prompt)
print(response)


# In[39]:


prompt = f"""
Your task is to help a marketing team create a 
description for a retail website of a product based 
on a technical fact sheet.

Write a product description based on the information 
provided in the technical specifications delimited by 
triple backticks.

The description is intended for furniture retailers,
so should be technical in nature and focus on the 
materials the product is constructed from.

At the end of the description, include every 7-character
Product ID in the technical specification

After the description, include a table that gives the 
product's dimensions. The table should have two columns.
In the first column include the name of the dimension.
In the second column include the measurements in inches only.

Give the table the title 'Product Dimensions'.

Format everything as HTML that can be used in a website.
Place the description in a <div> element.

Technincal specifications: ```{fact_sheet_chair}```
"""

response = get_completion(prompt)
print(response)


# In[40]:


from IPython.display import display, HTML


# In[42]:


display(HTML(response))

