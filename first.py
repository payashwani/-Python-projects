import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article
import lxml
import lxml.html.clean



def summarize():
    url= utext.get('1.0','end').strip()

    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()

        title.config(state='normal')
        author.config(state='normal')
        pdates.config(state='normal')
        summary.config(state='normal')
        sentiment.config(state='normal')

        title.delete('1.0','end')
        title.insert('1.0', article.title)
    
        author.delete('1.0','end')
        author.insert('1.0', ','.join(article.authors))
    
        pdates.delete('1.0','end')
        pdates.insert('1.0', str(article.publish_date))
    
        summary.delete('1.0','end')
        summary.insert('1.0', article.summary)

        analysis = TextBlob(article.text)
        sentiment.delete('1.0','end')
        sentiment_message = f"Polarity: {analysis.polarity}, Sentiment: {'positive' if analysis.polarity > 0 else 'negative' if analysis.polarity < 0 else 'neutral'}"
        sentiment.insert('1.0', sentiment_message)
  
        title.config(state='disabled')
        author.config(state='disabled')
        pdates.config(state='disabled')
        summary.config(state='disabled')
        sentiment.config(state='disabled')
   
  
    except Exception as e:
       summary.config(state='normal')
       summary.delete('1.0', 'end')
       summary.insert('1.0', f"Error: {str(e)}")
       summary.config(state='disabled')

 

#print(f'Title : {article.title}')
#print(f'Author : {article.authors}')
#print(f'Publication Date : {article.publish_date}')
#print(f'Summary : {article.summary}')

root = tk.Tk()
root.title("News summarizer")
root.geometry("1000x600")

tlabel = tk.Label(root,text="TITLE")
tlabel.pack()
title = tk.Text(root , height=1 , width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

alabel = tk.Label(root,text="AUTHORS")
alabel.pack()
author = tk.Text(root , height=1 , width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()

plabel = tk.Label(root,text="PUBLICATION DATES")
plabel.pack()
pdates= tk.Text(root , height=1 , width=140)
pdates.config(state='disabled', bg='#dddddd')
pdates.pack()

slabel = tk.Label(root,text="SUMMARY")
slabel.pack()
summary = tk.Text(root , height= 20 , width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

stlabel = tk.Label(root,text="SENTIMENT ANALYSIS")
stlabel.pack()
sentiment = tk.Text(root , height=1 , width=140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

ulabel = tk.Label(root,text="URL")
ulabel.pack()
utext = tk.Text(root , height=1 , width=140)
utext.pack()

btn = tk.Button(root , text="summarize" , command=summarize)
btn.pack()

root.mainloop() 