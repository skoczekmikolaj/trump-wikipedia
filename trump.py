import wikipedia
print("witaj w programie analizujacym artykuly dotyczace Donalda Trumpa w Wikipedii")
wikipedia.set_lang("en")
wyniki=wikipedia.search("Donald Trump")
print('\ntrwa analiza wynikow...\n\n')
streszczenia=[]
for artykul in wyniki:
    streszczenia.append(wikipedia.summary(artykul))

from textblob import TextBlob
StreszczenieSentiment={}
artykulSubiektywnosc={}
artykulPolaryzacja={}
sentymenty=[]
for s in streszczenia:
    wynik=TextBlob(s)
    sentymenty.append(wynik.sentiment)
    
for i in range (len(wyniki)):
    StreszczenieSentiment[wyniki[i]]=sentymenty[i]
    artykulSubiektywnosc[wyniki[i]]=sentymenty[i].subjectivity
    artykulPolaryzacja[wyniki[i]]=sentymenty[i].polarity

najmniejszaSub=sentymenty[0].subjectivity
najwiekszaSub=sentymenty[0].subjectivity
najmniejszaPol=sentymenty[0].polarity
najwiekszaPol=sentymenty[0].polarity
for s in sentymenty:
    if s.subjectivity<najmniejszaSub:
        najmniejszaSub=s.subjectivity
    elif s.subjectivity>najwiekszaSub:
        najwiekszaSub=s.subjectivity


for s in sentymenty:
    if s.polarity<najmniejszaPol:
        najmniejszaPol=s.polarity
    elif s.polarity>najwiekszaPol:
        najwiekszaPol=s.polarity

tMaxPol=''
tMinPol=''
tMaxSub=''
tMinSub=''


for i in range (len(wyniki)):
    print("title: "+ wyniki[i])
    print("result:"+ str(sentymenty[i])+'\n')

for k, v in artykulSubiektywnosc.items():
    if v==najmniejszaSub:
        tMinSub=k
    elif v==najwiekszaSub:
        tMaxSub=k

for k, v in artykulPolaryzacja.items():
    if v==najmniejszaPol:
        tMinPol=k
    elif v==najwiekszaPol:
        tMaxPol=k

print("the most subjective article: "+str(tMaxSub)+', rate:' +str(najwiekszaSub)+'\n')

print("the least subjective article: "+str(tMinSub)+', rate:' +str(najmniejszaSub)+'\n')

print("the most positive article: "+str(tMaxPol)+', rate:' +str(najwiekszaPol)+'\n')

print("the most negative article: "+str(tMinPol)+', rate ' +str(najmniejszaPol)+'\n')