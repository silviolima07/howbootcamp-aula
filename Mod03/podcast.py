#%%
import requests
import logging
import pandas as pd

from bs4 import BeautifulSoup as bs
# %%
url = 'https://portalcafebrasil.com.br/todos/podcasts/'

#%%
ret = requests.get(url)

#%%
ret.text
#%%
soup = bs(ret.text)
print(soup)
#%%
soup.find('h5')
# %%
soup.find('h5').text
# %%
soup.find('h5').a['href']
# %%
lst_podcast = soup.find_all('h5')
lst_podcast
# %%
len(lst_podcast)
# %%
for item in lst_podcast:
    print(f"EP: {item.text} - Link:{item.a['href']}")
# %%
url = 'https://portalcafebrasil.com.br/todos/podcasts/page/{}/?ajax=true'

# %%
url.format(5)
# %%
def get_podcast(url):
    ret = requests.get(url)
    soup = bs(ret.text)
    return soup.find_all('h5')

# %%
get_podcast(url.format(1))

#%%
log = logging.getLogger()
log.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)
# %%

i = 10
i = 1000
lst_podcast = []
lst_get = get_podcast(url.format(i))
# %%
lst_get
print("Tamanho:", len(lst_get))
# %%
i = 1
lst_podcast = []
lst_get = get_podcast(url.format(i))
log.debug(f"Coletado {len(lst_get)} episodios do link:{url.format(i)}")
while len(lst_get) > 0:
    lst_podcast = lst_podcast + lst_get
    i += 1
    lst_get = get_podcast(url.format(i))
    log.debug(f"Coletado {len(lst_get)} episodios do link:{url.format(i)}")
#%%
print(len(lst_podcast))
#%%
lst_podcast
#%%
df = pd.DataFrame(columns=['nome', 'link'])
#%%
df

# %%
for item in lst_podcast:
    print("Linha: ",df.shape[0])
    df.loc[df.shape[0]] = [item.text, item.a['href']]
    print("Linha apos incluir dados: ",df.shape[0])

# %%
df.shape[0]
# %%
df.loc[df.shape[0]]
# %%
df.head()
# %%
