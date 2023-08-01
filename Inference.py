#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env key

openai.api_key = os.getenv('OPENAI_API_KEY')


# In[3]:


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
    model=model,
    messages=messages,
    temperature=0,
    )
    return response.choices[0].message["content"]


# In[4]:


prod_review = """
Got this panda plush toy for my daughter's birthday, \
who loves it and takes it everywhere. It's soft and \
super cute, and it's face has a friendly look. It's a \
bit samll for what I paid though. I think there \
might be other options that are bigger for the \
same price. It arrived a day earlier than expected, \
so i got to play with it myself before i gave it \
to her.
"""


# In[5]:


prompt = f"""
Your task is to generate a short summary of a product \
review from an ecommerce site.

Summarize the review below, delimited by triple 
backticks, in at most 30 words.

Review: ```{prod_review}```
"""

response = get_completion(prompt)
print(response)


# In[6]:


prompt = f"""
Your task is to generate a short summary of a product \
review from an ecommerce site to give feedback to the \
shipping department.

Summarize the review below, delimited by triple 
backticks, in at most 30 words, and focusing on any aspects
that mention shipping and delivery of the product.

Review: ```{prod_review}```
"""

response = get_completion(prompt)
print(response)


# In[6]:


prompt = f"""
Your task is to generate a short summary of a product \
review from an ecommerce site to give feedback to the \
pricing department, responsible for determining the \
price of the product.

Summarize the review below, delimited by triple 
backticks, in at most 30 words, and focusing on any aspects
that are relevant to the price and perceived value.

Review: ```{prod_review}```
"""

response = get_completion(prompt)
print(response)


# In[7]:


prompt = f"""
Your task is to extract relevant information from \ 
a product review from an ecommerce site to give feedback to the \
shipping department.

From the review below, delimited by triple backticks
extract infromation relevant to shipping and delivery
of the product. Limit to 30 words.

Review: ```{prod_review}```
"""

response = get_completion(prompt)
print(response)


# In[10]:


prod_review_2 = """
Needed a nice lamp for my bedroom and this one \
had additional storage and not too high of a price \
point. Got it fast - arrived in 2 days. The string \
to the lamp broke during the transit and the company \
happily sent over a new one. Came within a few days \
as well. It was easy to put together. Then i had a \
missing part, so i contacted their support and they \
very quickly got me the missing piece! Seems to me \
to be a great company that cares about their customers \
and products.
"""

prod_review_3 = """
My dental hygienist recommended an electric toothbrush \
which is why i got this. The battery life seems to be \
pretty impressive so far. After initial charging and \
leaving the plugged in for the first week to \
condition the battery, i've unplugged the charger and \
been using it for twice daily brushing for the last \
3 weeks all on the same charge. but the toothbrush head \
is too small. I've seen babt toothbrush bigger than \
this one. I wish the head was bigger with different \
length bristles to get between teeth better because \
this one doesn't. Overall if you can get this one \
around the $50 mark, it's a good deal. The manufacturer's \
replacement heads are pretty expensive, but you can \
get generic ones that are more reasonably priced. This \
toothbrush makes me feel like i have been to the dentist \
every day. My teeth feel sparkly clean.
"""

prod_review_4 = """
So they still had the 17 piece system on seasonal \
sale for around $49 in the month of November, about \
half off, but for some reason (call it price gouging) \
around the second week of December, the prices all went \
up to about anywhere from between $70-$89 for the same \
system. And the 11 piece system went up around $10 or \
so in price also from the earlier sale price  of $29. \
So it looks okay, but if you look at the base, the part \
where the blade locks into place doesn't look as good \
as in previous editions from previous years ago, but i \
plan to be vry gentle with it (example, I crush \
crush very hard items like beans, rice, ice, etc. in the\
blender first then pulverize them in the serving size \
i want in the blender then switch to the whipping \
blade for a finer flour, and use the cross cutting blade \
first when making smoothies, then use the flat blade \
if i need them finer/less pulpy). Special tip when making \
smoothies, finely cut and  freeze the fruits and \
vegetables (if using spinach_lightly stew soften the \
spinach then freeze until ready for use-and if making \
sorbet, use a small to medium sized food processor) \
that you plan to use that way you can avoid adding so \
much ice if at all-when making your smoothie. \
After about a year the motor was makinf a funny noise. \
I called customer service but the warranty expired \
already, so i had to buy another one. FYI: The overall \
quality has gone down in these types of products, so \
they are kind of counting on brand recognition and \
consumer loyalty to maintain sales. Got it in about \
two days.
"""

reviews = [prod_review_2, prod_review_3, prod_review_4]


# In[11]:


for i in range(len(reviews)):
    prompt = f"""
    Your task is to generate a short summary of a prodcut \
    review from an ecommerce site.
    
    Summarize the review below, delimited by triple \
    backticks in at most 20 words. 
    
    Review: ```{reviews[i]}```
    """
    
    response = get_completion(prompt)
    print(i, response, "\n")


# In[14]:


lamp_review = """
Needed a nice lamp for my bedroom and this one \
had additional storage and not too high of a price \
point. Got it fast - arrived in 2 days. The string \
to the lamp broke during the transit and the company \
happily sent over a new one. Came within a few days \
as well. It was easy to put together. Then i had a \
missing part, so i contacted their support and they \
very quickly got me the missing piece! Seems to me \
to be a great company that cares about their customers \
and products.
"""

prompt = f"""
What is the sentiment of the following product review,
which is delimited by triple backticks?

Review text: ```{lamp_review}```
"""
response = get_completion(prompt)
print(response)


# In[15]:


lamp_review = """
Needed a nice lamp for my bedroom and this one \
had additional storage and not too high of a price \
point. Got it fast - arrived in 2 days. The string \
to the lamp broke during the transit and the company \
happily sent over a new one. Came within a few days \
as well. It was easy to put together. Then i had a \
missing part, so i contacted their support and they \
very quickly got me the missing piece! Seems to me \
to be a great company that cares about their customers \
and products.
"""

prompt = f"""
What is the sentiment of the following product review,
which is delimited by triple backticks?

Give your answer as a single word, either "positive" \
or "negative".

Review text: ```{lamp_review}```
"""
response = get_completion(prompt)
print(response)


# In[16]:


prompt = f"""
Identify a list of emotions that the writer of the \
following review is expressing. Include no more than \
five items in the list. Format your answer as a list of \
lower-case words separated by commas.

Review text: '''{lamp_review}'''
"""

response = get_completion(prompt)
print(response)


# In[19]:


prompt = f"""
Is the writer of the following review expressing anger? \
The review is delimited by triple backticks. \
Give your answer as either yes or no.

Review text: '''{lamp_review}'''
"""

response = get_completion(prompt)
print(response)


# In[20]:


prompt = f"""
Identify the following items from the  review text:
- Item purchased by reviewer
- Company that made the item

The review is delimited with triple backticks. \
Format your response as a JSON object with \
"Item" and "Brand" as the keys.
If the information is not present, use "unknown" \
as the value.
Make your response as short as possible.

Review text: '''{lamp_review}'''
"""

response = get_completion(prompt)
print(response)


# In[22]:


prompt = f"""
Identify the following items from the  review text:
- Sentiment (negative or positive)
- Is the reviewer expressing anger?
- Item purchased by reviewer
- Company that made the item

The review is delimited with triple backticks. \
Format your response as a JSON object with \
"Sentiment", "Anger", "Item" and "Brand" as the keys.
If the information is not present, use "unknown" \
as the value.
Make your response as short as possible.

Format the Anger value as a boolean.

Review text: '''{lamp_review}'''
"""

response = get_completion(prompt)
print(response)


# In[31]:


story = """
Sometimes people come into your life and you know right away that they were meant to be there, 
to serve some sort of purpose, teach you a lesson, or to help you figure out who you are or who you want to become. 
You never know who these people may be (possibly your roommate, neighbor, coworker, longlost friend, lover, 
or even a complete stranger) but when you lock eyes with them, you know at that very moment that they will
affect your life in some profound way.

And sometimes things happen to you that may seem horrible, painful, and unfair at first, 
but in reflection you find that without overcoming those obstacles you would have never realized your potential, 
strength, willpower, or heart.

Everything happens for a reason. Nothing happens by chance or by means of luck. Illness, 
injury, love, lost moments of true greatness, and sheer stupidity all occur to test the limits of your soul. 
Without these small tests, whatever they may be, life would be like a smoothly paved, straight, flat road to nowhere. 
It would be safe and comfortable, but dull and utterly pointless.

The people you meet who affect your life, and the success and downfalls you experience help to create who you become. 
Even the bad experiences can be learned from. In fact, they are probably the most poignant and important ones. 
If someone hurts you, betrays you, or breaks your heart, forgive them, for they have helped you learn about trust 
and the importance of being cautious when you open your heart. If someone loves you, love them back unconditionally, 
not only because they love you, but because in a way, they are teaching you to love and how to open your heart and eyes to things.

Make every day count!!! Appreciate every moment and take from those moments everything that you possibly 
can for you may never be able to experience it again. Talk to people that you have never talked to before, 
and actually listen. Let yourself fall in love, break free, and set your sights high. Hold your head up 
because you have every right to. Tell yourself you are a great individual and believe in yourself, 
for if you don’t believe in yourself, it will be hard for others to believe in you. You can make of your 
life anything you wish. Create your own life then go out and live it with absolutely no regrets.
"""


# In[32]:


prompt = f"""
Determine five topics that are being discussed in the \
following text, which is delimited by triple backticks.

Make each item one or two words long

Format your response as a list of words separated by commas.

Text sample: '''{story}'''
"""

response = get_completion(prompt)
print(response)


# In[33]:


response.split(sep=',')


# In[40]:


topic_list = [
    "Life lessons", "Purpose", "Wickedness", 
    "Relationships", "Self-belief"
]


# In[41]:


prompt = f"""
Determine whether each item in the following list of \
topics is a topic in the text below, which 
is delimited by triple backticks.

Give your answer as list with 0 or 1 for each topic.\

List of topics: {", ".join(topic_list)}

Format your response as a list of words separated by commas.

Text sample: '''{story}'''
"""

response = get_completion(prompt)
print(response)

