import random

def substituir_letras(texto):
    substuicoes = { 'a': '@', 's': '$', 'o': '0', 'e': '3', 'i': '1'}
    return ''.join(substuicoes.get(c.lower(), c) for c in texto)

def embararalhar(texto):
    lista_caracteres = list(texto)
    random.shuffle(lista_caracteres)
    return ''.join(lista_caracteres)


def gerar_senha(nome, numero):
    nome_modificado = substituir_letras(nome)
    simbolo = "!@#$%¨&*()_+-"

    senha_base = nome_modificado + str(numero) + random.choice(simbolo)

    senha_base = list(senha_base)
    tem_maiscula = any(c.isupper() for c in senha_base)

    if not tem_maiscula:
        for i, c in enumerate(senha_base):
            if c.isalpha():
                senha_base[i] = c.upper()
                break

    senha_embaralhada = embararalhar(senha_base)

    return senha_embaralhada



nome = input("Digite uma palavra chave: ")
numero = input("Digite um número importante: ")

senha_gerada = gerar_senha(nome, numero)
print(f"Senha Gerada: {senha_gerada}")

input()