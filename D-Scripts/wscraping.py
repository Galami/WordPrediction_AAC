# -*- coding: utf-8 -*-

import os, sys
from bs4 import BeautifulSoup # Web scraping
from nltk.tokenize import RegexpTokenizer # Tokenisation

tokenizer = RegexpTokenizer(r'\w+')

link = str(input("Entrez le lien : "))

import urllib.request
with urllib.request.urlopen(link) as url:
	html = url.read().decode("utf8")

def tag_visible(element):
	if element.parent.name in ["p"]: # Si dans un paragraphe
		return True
	return False

def text_from_html(body):
	soup = BeautifulSoup(body, 'html.parser')
	soup = soup.find("div", {"class": "entry-content clearfix"})
	texts = soup.findAll(text=True)	
	visible_texts = filter(tag_visible, texts)
	return " ".join(t.strip().lower() for t in visible_texts) # Minuscule

file = open("corpus.txt", "a", encoding="utf-8")

htmlist = tokenizer.tokenize(text_from_html(html))
article = " ".join(htmlist)

file.write(article + " ")

print(len(article.split())) # Facultatif : nbre de mots
print(len(article)) # Facultatif : nbre de lettres

file.close()