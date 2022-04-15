        #semaine 1:
travel_file=open('travel_plans.txt','r')
num=0
for i in travel_file:
    num = num + len(i)



num_words=0
emotion_file=open('emotion_words.txt','r')
for i in emotion_file:
    num_words = num_words + len(i.split(" "))



num_lines=0
school_file=open('school_prompt.txt','r')
for i in school_file:
    num_lines = num_lines + 1



school_file=open('school_prompt.txt','r')
beginning_chars=school_file.read(30)



school_file=open('school_prompt.txt','r')
three=[]
for i in school_file:
    three.append(i.split()[2])



emotions=[]
emotions_file=open('emotion_words.txt','r')
for i in emotions_file:
    emotions.append(i.split()[0])



travel_file=open('travel_plans.txt','r')
first_chars=travel_file.read(33)



school_file=open('school_prompt.txt','r')
words=school_file.read().split()
p_words=[word for word in words if 'p' in word]









        #semaine 2 Partie 1: 
medal_count={'United States':70,'Great Britain':38,'China':45,'Russia':30,'Germany':17}



swimmers={'Manual':4,'Lochte':12,'Adrian':7,'Ledecky':5,'Dirado':4}
swimmers['Phelps']=23



sports_periods={'baseball':9,'basketball':4,'soccer':4,'cricket':2}
sports_periods['hockey']=3



golds['Spain']=21



countries=golds



belarus=medal_count.get('Belarus')



chile_golds=total_golds.get('Chile')



fencing_value=US_medals.get('Fencing')

            









        #semaine 2 Partie 2: 
credits=0
for i in Junior.values():
    credits=credits+i



freq={}
for i in str1:
    if i in freq:
        freq[i]=freq[i]+1
    else:
        freq[i]=1



counts={}
for i in s1:
    if i in counts:
        counts[i]=counts[i]+1
    else:
        counts[i]=1



freq_words={}
words=str1.split()
for i in words:
    if i not in freq_words:
        freq_words[i]=1
    else:
        freq_words[i]=freq_words[i]+1



wrd_d={}
words=sent.split()
for i in words:
    if i not in wrd_d:
        wrd_d[i]=1
    else:
        wrd_d[i]=wrd_d[i]+1



characters={}
for i in sally:
    characters[i]=characters.get(i,0)+1
sorted(characters.items(),key=lambda x:x[1])
best_char=sorted(characters.items(),key=lambda x:x[1])[-1][0]



characters={}
for i in sally:
    characters[i]=characters.get(i,0)+1
sorted(characters.items(),key=lambda x:x[1])
worst_char=sorted(characters.items(),key=lambda x:x[1])[0][0]



letter_counts={}
for i in string1.lower():
    if i not in letter_counts:
        letter_counts[i]=1
    else:
        letter_counts[i]=letter_counts[i]+1



low_d={}
for i in p.lower():
    if i not in low_d:
        low_d[i]=1
    else:
        low_d[i]=letter_counts[i]+1
            









        #semaine 3 Partie 1:
def int_return(i):
    return i



def add(i):
    return i+2



def change(str):
    return str+"Nice to meet you!"



def accum(l):
    i=0
    for j in l:
        i=i+j
    return i



def length(l):
    if len(l)>=5:
        return "Longer than 5"
    else:
        return "Less than 5"



def divide(i):
    return i/2
def sum(i):
    return i/2 + 6
sum(divide(10))
            









        #semaine 3 Partie 2:
olympics=('Beijing','London','Rio','Tokyo')



country=[]
for i in tuples_lst:
    country.append(i[1])



olymp=('Rio','Brazil',2016)
city=olymp[0]
country=olymp[1]
year=olymp[2]



def info(name,gender,age,bday_month,hometown):
    details=(name,gender,age,bday_month,hometown)
    return details



num_medals=[]
for i in gold.items():
    num_medals.append(i[1])
            









       #semaine 4 Partie 1 : 
def sublist(i):
    s1=[]
    i=(item for item in i)
    item = next(i,5)
    while item != 5:
        s1.append(item)
        item = next(i,5)
    return s1



def check_nums(i):
    s1=[]
    i=(item for item in i)
    item = next(i,7)
    while item != 7:
        s1.append(item)
        item = next(i,7)
    return s1



def sublist(l):
    i=0
    while(i<len(l)):
        if(l[i]=="STOP"):
            return l[0:i]
        i = i + 1
    return False



def stop_at_z(l):
    i=0
    while(i<len(l)):
        if(l[i]=='z'):
            return l[0:i]
        i = i + 1
    return False



sum1=0
sum2=0
lst=[65,78,21,33]
for i in lst:
    sum1=sum1+i
i=0
while(i<len(lst)):
    sum2=sum2+lst[i]
    i=i+1
for x in lst:
    sum1=sum1+x



def beginning(l):
    i=0
    sublist=[]
    while(i<len(l)):
        if(l[i]=='bye'):
            break
        sublist.append(l[i])
        i=i+1
    return sublist[:10]
            









        #semaine 4 Partie 2 :
def mult(i,j=6):
    return i*j



def greeting(name,greeting="Hello ",excl="!"):
    return greeting+name+excl
print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob"), excl="!!!")



def sum(intx,intz=5):
    return intz + intx



def test(i,b=True,dict1={2:3,4:5,6:8}):
    return b and dict1.get(i,False)



def checkingIfIn(a,direction=True,d={'apple':2,'pear':1,'fruits':19,'orange':5,'banana':3,'grapes':2,'watemelon':7}):
    if direction==True:
        if a in d:
            return True
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return False



def checkingIfIn(a,direction=True,d={'apple':2,'pear':1,'fruits':19,'orange':5,'banana':3,'grapes':2,'watemelon':7}):
    if direction==True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]
c_false=checkingIfIn('guava')
c_true=checkingIfIn('apples',False,{'carrots':5,'beans':15,'califlower':8,'peas':30,'beetroot':1})
fruit_ans=checkingIfIn('fruits')
param_check=checkingIfIn('califlower',False,{'carrots':5,'beans':15,'califlower':8,'peas':30,'beetroot':1})









                    









       #semaine 5 Partie 1 : 
sorted_letters = sorted(letters,reverse=True)



animals_sorted=sorted(animals)




alphabetical=sorted(medals)



top_three=sorted(medals.keys(),key=lambda x:medals[x],reverse=True)[:3]



most_needed=sorted(groceries.keys(),key=lambda x:groceries[x],reverse=True)



def last_four(x):
    return (str(x)[-4:])

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
last_four(ids)
sorted_ids=sorted(ids,key=last_four)



sorted_id=sorted(ids,key=lambda x:str(x)[-4:])



lambda_sort=sorted(ex_lst,key=lambda x:x[1])









        #semaine 5 Partie 2 : 
punctuation_chars=["'",'"',",",".","!",":",";","#","@"]
def strip_pnuctuation(s):
    for ch in punctuation_chars:
        s=s.replace(ch,"")
    return s



punctuation_chars=["'",'"',",",".","!",":",";","#","@"]
def strip_punctuation(s):
    for ch in punctuation_chars:
        s=s.replace(ch,"")
    return s
positive_words=[]
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0]!=';' and lin[0]!='\n':
            positive_words.append(lin.strip())
def get_pos(s):
    positive=0
    l=s.lower()
    l1=strip_punctuation(l)
    list1=l1.split(" ")
    for i in positive_words:
        for j in list1:
            if(i==j):
                positive=positive+1
    return positive



punctuation_chars=["'",'"',",",".","!",":",";","#","@"]
def strip_punctuation(s):
    for ch in punctuation_chars:
        s=s.replace(ch,"")
    return s
negative_words=[]
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0]!=';' and lin[0]!='\n':
            negative_words.append(lin.strip())
def get_neg(s):
    negative=0
    l=s.lower()
    l1=strip_punctuation(l)
    list1=l1.split(" ")
    for i in negative_words:
        for j in list1:
            if(i==j):
                negative=negative+1
    return negative



punctuation_chars=["'",'"',",",".","!",":",";","#","@"]
def strip_punctuation(s):
    for ch in punctuation_chars:
        s=s.replace(ch,"")
    return s
positive_words=[]
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0]!=';' and lin[0]!='\n':
            positive_words.append(lin.strip())
def get_pos(s):
    positive=0
    l=s.lower()
    l1=strip_punctuation(l)
    list1=l1.split(" ")
    for i in positive_words:
        for j in list1:
            if(i==j):
                positive=positive+1
    return positive
negative_words=[]
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0]!=';' and lin[0]!='\n':
            negative_words.append(lin.strip())
def get_neg(s):
    negative=0
    l=s.lower()
    l1=strip_punctuation(l)
    list1=l1.split(" ")
    for i in negative_words:
        for j in list1:
            if(i==j):
                negative=negative+1
    return negative
output = open("resulting_data.csv","w")
output.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
output.write("\n")
twitter_data = open("project_twitter_data.csv","r")
twitter_data = twitter_data.readlines()
for tweet in twitter_data[1:]:
    sp = tweet.strip().split(",")
    p_score = get_pos(tweet)
    n_score = get_neg(tweet)
    net_s = p_score - n_score
    row = '{},{},{},{},{}'.format(sp[1],sp[2],p_score,n_score,net_s)
    output.write(row)
    output.write("\n")
