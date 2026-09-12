from Aula_modularizacao.model import model_lead
import Aula_modularizacao.control as control
 
def add_lead():
    name = input("Nome: ")
    email = input("Email: ")
    status = input("Status do fluxo de vendas: ")
 
    #Validando:
    #agora preciso modelar os dados para isso, vamos usar o modulo modulo.py
    control.create_lead(model_lead(name, email, status))
    
    print(model_lead(name, email, status))
 
    #Com os dados modelados, preciso enviar para o json. Vou usar o control para enviar o dicionario do lead
 
def list_leads():
    leads = control.read_leads()
    print(leads)

def update_lead():
    email = input("Email do lead que deseja atualizar: ")
    novo_status = input("Novo status: ")
    if control.upadate_leads(email, novo_status):
        print("Lead atualizado!")
    else:
        print("Lead nao encontrado.")

def delete_lead():
    email = input("Email do lead que deseja remover: ")
    if control.delete_lead(email):
        print("Lead removido!")
    else:
        print("Lead nao encontrado.")

def main():
    while True:
        print("\nmini crm de leads")
        print("[1] Adicionar lead")
        print("[2] Listar lead")
        print("[3] Atualizar lead")
        print("[4] Remover lead")
        print("[0] Sair do programa")

        opt = input("Escolha uma opcao:")

        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "3":
            update_lead()
        elif opt == "4":
            delete_lead()
        elif opt =="0":
            print("Ate mais...")
            break
        else:
            print()


if __name__ == "__main__":
    main()
