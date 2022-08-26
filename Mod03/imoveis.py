#%%
import requests
import logging
import pandas as pd

from bs4 import BeautifulSoup as bs
#%%
url = 'https://www.vivareal.com.br/venda/parana/curitiba/apartamento_residencial/?pagina={}'
# %%
i  = 1
ret = requests.get(url.format(i))
print("ret.text:", ret.text)
#%%
soup = bs(ret.text)
soup
# %%
print(soup)
# %%
houses = soup.find_all('a',{'class': 'property-card__content-link js-card-title'})
# %%
houses
# %%
print(houses)
# %%
