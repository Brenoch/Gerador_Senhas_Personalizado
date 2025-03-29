import random

def substituir_letras(texto):
    substuicoes = { 'a': '@', 's': '$', 'o': '0', 'e': '3', 'i': '1'}
    return ''.join(substuicoes.get(c.lower(), c) for c in texto)

def gerar_senha(nome, numero):
    nome_modificado = substituir_letras(nome)
    nome_aternado = ''.join(
        c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(nome_modificado)
    )


    simbolo = "!@#$%¨&*-_"
    senha = f"{nome_aternado}{numero}{random.choice(simbolo)}"

    return senha

nome = input("Digite uma palavra chave: ")
numero = input("Digite um número importante: ")

senha_gerada = gerar_senha(nome, numero)
print(f"Senha Gerada: {senha_gerada}")