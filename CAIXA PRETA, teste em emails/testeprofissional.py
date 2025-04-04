import re
import unittest
##esse é um teste de caixa preta um pouco mais profissional, em que eu estou utilizando unittest

def validar_email(email):
    regex = r"^[a-zA-Z0-9]+([._-]?[a-zA-Z0-9]+)*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(regex, email))

class TestEmailValidator(unittest.TestCase):
    
    def test_emails_validos(self):
        emails_validos = [
            "teste123@gmail.com",
            "nome.sobrenome@ufam.br",
            "usuario-legal@outlook.com",
            "exemplo_teste@yahoo.com.br",
            "dev.2025@projeto.tech"
        ]
        for email in emails_validos:
            self.assertTrue(validar_email(email), f"Deveria ser válido: {email}")

    def test_emails_invalidos(self):
        emails_invalidos = [
            "oi--oi__oi@gmail.com",
            "nome..email@hotmail.com",
            "@gmail.com",
            "email@.com",
            "user@site_com"
        ]
        for email in emails_invalidos:
            self.assertFalse(validar_email(email), f"Deveria ser inválido: {email}")

# Isso executa o teste quando você roda o arquivo
if __name__ == "__main__":
    unittest.main()
