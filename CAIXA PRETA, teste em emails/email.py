import re
import logging
#não é um validador de email completo, mas sim um exemplo simples, ainda tenho que melhorar 
#pego de um arquivo de texto e coloco em um log
logging.basicConfig(filename='emailvalido.log',level=logging.INFO,format='%(asctime)s-%(levelname)s-%(message)s')

def le_email(email):
    padrao_email =  r"^[a-zA-Z0-9]+([._-]?[a-zA-Z0-9]+)*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    if re.match(padrao_email,email):
        logging.info(f'Email {email} é válido')
    else:
        logging.error(f'Email {email} é inválido')

with open('emails.txt', 'r') as arquivo:
    for linha in arquivo:
        email = linha.strip()
        
        le_email(email)

