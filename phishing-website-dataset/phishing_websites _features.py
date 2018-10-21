
# coding: utf-8

# In[79]:


import re
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
# -1 represent  phishing url while 1 represent not phishing url, returning zero means not sure
#length of urls

#if url contains ip addresses instead of name http://125.98.3.123/fake.html
def ip_address(url):
    match=re.search('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',url)
    if match:
        return -1  
    else:
        return 1
print(ip_address('http://125.98.3.123/fake.html'))

def url_length(url):
    if len(url)<54:
        return 1
    elif len(url)>=54|len(url)<=75:
        return 0
    else:
        return -1

    
#if url contains shortening services something like bit.ly/19DXSk4
def url_shortener(url):
    match=re.search('bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
                    'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
                    'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
                    'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'
                    'db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'
                    'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'
                    'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|tr\.im|link\.zip\.net',url)

    if match:
        return -1
    else:
        return 1
# Using “@” symbol in the URL leads the browser to ignore everything preceding the “@” symbol and the real address often follows the “@” symbol. 
def url_symbol(url):
    match=re.search("@", url)
    if match:
        return -1
    else:
        return 1
def url_redirect(url):
    list = [x.start(0) for x in re.finditer('\\.',url)]
    if list[len(list)-1]>6:
        return -1
    else:
        return 1
print(url_redirect('https://www.legitimate.com//http://www.phishing.com'))
   
# Adding Prefix or Suffix Separated by (-) to the Domain
def pref_suf(url):
    match = re.search("-", url)
    if match:
        return -1
    else:
        return 1
# Sub Domain and Multi Sub Domains
def sub_domain(url):
     if(ip_address(url)==-1):
        match = re.search('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
                    '(?:^|(?<=\s))(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))(?=\s|$)'
                    '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}',url).end(0)
        pos = match.end(0)
        url = url[pos:]
        list = [x.start(0) for x in re.finditer('\.',url)]
        if len(list)<=3:
            return 1
        elif len(list) == 4:
            return 0
        else:
            return -1

#def submitting_to_mail(url):
    #web = urlopen(url)
    #soup = bs(web, 'html.parser')
    #for form in soup.findAll('form', action= True):
      #  if "mailto:" in form['action'] :
     #       return -1
    #     else:
 #           return 1
#print(submitting_to_mail("https://whogohost.com"))
# Website Traffic 

def web_traffic(url):
    content = urlopen("http://data.alexa.com/data?cli=10&dat=s&url=" + url)
    try:
        rank = bs(content, "xml").find("REACH")['RANK']
        rank= int(rank)
    except Exception as e:
        return -1
    if (rank<100000):
        return 1
    else:
        return 0
   
#print(web_traffic("facebook.com"))

    

