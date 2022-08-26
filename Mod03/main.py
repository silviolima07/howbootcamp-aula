#%%
# imports
import requests
import json
import backoff
import random

# %%

url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
ret = requests.get(url)

# %%
if ret:
    print(ret.text)
else:
    print("Falhou")    
# %%

dolar = json.loads(ret.text)['USDBRL']
# %%
print(f" 20 dolares hoje custam {float(dolar['bid'])*20} reais")
# %%

def cotacao(valor, moeda):
    url = f'https://economia.awesomeapi.com.br/last/{moeda}'
    #url = 'https://economia.awesomeapi.com.br/last{}'.format(moeda)
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-','')]
    print(
        f"{valor} {moeda[:3]} hoje custam {round(float(dolar['bid']) * valor,2)} {moeda[4:]}"
    )


    
# %%
cotacao(20, 'USD-BRL')

# %%
cotacao(20, 'JPY-BRL')
# %%
lst_money = [
    "USD-BRL",
    "EUR-BRL",
    "BTC-BRL",
    "RPL-BRL",
    "JPY-BRL"]



# %%
def error_check(func):
    def inner_func(*args, **kargs):
        try:
            func(*args, **kargs)
        except:
            print(f"{func.__name__} falhou")    
    return inner_func 

@error_check
def multi_moeda(valor, moeda):
    url = f'https://economia.awesomeapi.com.br/last/{moeda}'
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-','')]
    print(
        f"{valor} {moeda[:3]} hoje custam {round(float(dolar['bid']) * valor,2)} {moeda[4:]}")

# %%
# %%
multi_moeda(20, 'USD-BRL')
multi_moeda(20, 'EUR-BRL')
multi_moeda(20, 'RPL-BRL')
multi_moeda(20, 'JPY-BRL')
# %%
@backoff.on_exception(backoff.expo,(ConnectionAbortedError, ConnectionRefusedError, TimeoutError),max_tries=10)
def test_func(*args, **kargs):
        rnd = random.random()
        print(f"""
            RND: {rnd}
            args: {args if args else 'sem args'}
            kargs: {kargs if kargs else 'sem kargs'}
        """)
        print("Numero randomico: ", rnd)
        if rnd < .2:
            raise ConnectionAbortedError('Conexao finalizada')
        elif rnd < .4:
            raise ConnectionRefusedError('Conexao recusada')
        elif rnd <.0:
            raise TimeoutError('Tempo de espera excedido')    
        else:
            return "OK!"          
# %%
test_func()
# %%
test_func(42)
# %%
test_func(42, 51, nome='silvio')
# %%
import logging
# %%
log = logging.getLogger()
log.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)
# %%
@backoff.on_exception(backoff.expo,(ConnectionAbortedError, ConnectionRefusedError, TimeoutError),max_tries=10)
def test_func(*args, **kargs):
        rnd = random.random()
        log.debug(f"RND: {rnd}")
        log.info(f"args: {args if args else 'sem args'}")
        log.info(f"kargs: {kargs if kargs else 'sem kargs'}")
        if rnd < .2:
            log.error('Conexao finalizada')
            raise ConnectionAbortedError('Conexao finalizada')
        elif rnd < .4:
            log.error('Conexao recusada')
            raise ConnectionRefusedError('Conexao recusada')
        elif rnd <.0:
            log.error('Tempo de espera excedido')
            raise TimeoutError('Tempo de espera excedido')    
        else:
            return "OK!" 
# %%
test_func()
# %%
test_func(42)
# %%
test_func(42, 51, nome='silvio')
# %%
