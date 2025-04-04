import re
#teste de caixa preta simples e nada profissional com emails
regex = r"^[a-zA-Z0-9]+([._-]?[a-zA-Z0-9]+)*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

def validar_email(email):
    return bool(re.match(regex, email))

# Lista de testes
testes = {
    "teste123@gmail.com": True,
    "nome.sobrenome@ufam.br": True,
    "usuario-legal@outlook.com": True,
    "exemplo_teste@yahoo.com.br": True,
    "dev.2025@projeto.tech": True,
    "oi--oi__oi@gmail.com": False,
    "nome..email@hotmail.com": False,
    "@gmail.com": False,
    "email@.com": False,
    "user@site_com": False,
}

# Executar os testes
for email, esperado in testes.items():
    resultado = validar_email(email)
    assert resultado == esperado, f"Erro: {email} deveria ser {'válido' if esperado else 'inválido'}, mas foi {'válido' if resultado else 'inválido'}"
    
print(" Todos os testes passaram!")
