"""
Desafio: Analisador de E-mails da FIAP
Disciplina: Pensamento Computacional e Automação com Python
Conteúdo: Dicionários e Tuplas

Objetivo:
    Ler uma lista de e-mails digitada pelo usuário, separar cada e-mail
    em (usuário, domínio), contar quantos e-mails existem por domínio
    usando um dicionário, montar uma tupla com os nomes de usuário e
    trocar a posição do primeiro e do último usuário sem usar variável
    temporária.
"""


def separar_emails(entrada: str) -> list[str]:
    """Recebe a string digitada pelo usuário e devolve uma lista de e-mails,
    já sem espaços em branco extras."""
    return [email.strip() for email in entrada.split(',')]


def montar_relatorio(emails: list[str]) -> tuple[dict, tuple]:
    """Percorre a lista de e-mails, separa usuário e domínio (split('@')),
    conta quantos e-mails existem por domínio em um dicionário e
    monta uma tupla com todos os usuários."""
    usuarios = []
    dominios = {}  # dicionário: chave = domínio, valor = quantidade de e-mails

    for email in emails:
        usuario, dominio = email.split('@')
        usuarios.append(usuario)

        if dominio not in dominios:
            dominios[dominio] = 1
        else:
            dominios[dominio] += 1

    usuarios_tupla = tuple(usuarios)  # lista -> tupla (imutável)
    return dominios, usuarios_tupla


def trocar_primeiro_ultimo(usuarios_tupla: tuple) -> tuple:
    """Troca a posição do primeiro e do último usuário SEM usar
    variável temporária, aproveitando a atribuição múltipla do Python
    (a, b = b, a) e devolve uma nova tupla."""
    lista_usuarios = list(usuarios_tupla)
    lista_usuarios[0], lista_usuarios[-1] = lista_usuarios[-1], lista_usuarios[0]
    return tuple(lista_usuarios)


def exibir_relatorio(dominios: dict, usuarios_tupla: tuple, usuarios_trocados: tuple) -> None:
    """Imprime o relatório final formatado."""
    print("\nRelatório:")
    print("Quantidade de e-mails por domínio:")
    for dominio, quantidade in dominios.items():
        print(f"  {dominio}: {quantidade}")

    print(f"\nLista de usuários: {usuarios_tupla}")
    print(f"Primeiro usuário: {usuarios_tupla[0]}")
    print(f"Último usuário: {usuarios_tupla[-1]}")
    print(f"Após troca de posições: {usuarios_trocados}")


def main() -> None:
    entrada = input("Digite os e-mails separados por vírgula: ")

    emails = separar_emails(entrada)
    dominios, usuarios_tupla = montar_relatorio(emails)
    usuarios_trocados = trocar_primeiro_ultimo(usuarios_tupla)

    exibir_relatorio(dominios, usuarios_tupla, usuarios_trocados)


if __name__ == "__main__":
    main()


# ---------------------------------------------------------------------------
# Exemplo de execução (entrada manual para teste rápido, sem usar input()):
#
# emails_teste = "joao.silva@fiap.com.br, maria.souza@fiap.com.br, ana.paula@fiap.com.br"
# doms, tup = montar_relatorio(separar_emails(emails_teste))
# tup_trocada = trocar_primeiro_ultimo(tup)
# exibir_relatorio(doms, tup, tup_trocada)
#
# Saída esperada:
# Relatório:
# Quantidade de e-mails por domínio:
#   fiap.com.br: 3
# Lista de usuários: ('joao.silva', 'maria.souza', 'ana.paula')
# Primeiro usuário: joao.silva
# Último usuário: ana.paula
# Após troca de posições: ('ana.paula', 'maria.souza', 'joao.silva')
# ---------------------------------------------------------------------------