from passlib.context import CryptContext
from passlib.hash import django_pbkdf2_sha256 as handler # Usado para o Django

CRIPTO = CryptContext(schemes=['bcrypt'], deprecated='auto')
# CRIPTO_DJANGO = CryptContext(schemes=['sha256_crypt'], deprecated='auto', sha256_crypt__default_rounds=100000)

def verificar_senha(senha:str, hash_senha: str) -> bool:
    """
    Função para verificar se a senha está correta, comparando
    a senha em texto puro, informada pelo usuário, e o hash da
    senha que estará salvo no banco de dados durante a criação
    da conta
    """
    return handler.verify(senha, hash_senha)
    # return CRIPTO.verify(senha, hash_senha)


def gerar_hash_senha(senha: str) -> str:
    """
    Função que gera e retorna o hash da senha
    """
    return handler.hash(senha)
    # return CRIPTO.hash(senha)
