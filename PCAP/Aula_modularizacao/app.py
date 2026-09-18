from model import model_lead
import control
 
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

def search_leads():
    query = input("Buscar por:").strip()
    if not query:
        print("Consulta vazia")
        return
    #com a query digitada (busca)... preciso enviar para o control
    # o conrol ira comparar a query com os dados do leads.json
    # e ira retornar os resultados da busca
    founds_leads = control.read_leads_serach(query)

    for i, lead in founds_leads:
        print(f"{i:02d} | {lead["name"]:<10} | {lead["email"]}")


def export_leads():
    path_csv = control.export_csv()

    if path_csv is None:
        print(f"Exportando para {path_csv}")

def main():
    while True:
        print("\nmini crm de leads")
        print("[1] Adicionar lead")
        print("[2] Listar lead")
        print("[3] Atualizar lead")
        print("[4] Remover lead")
        print("[5] Search Lead")
        print("[6] Export Lead")
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
        elif opt == "5":
            search_leads()
        elif opt == "6":
            export_leads()
        elif opt =="0":
            print("Ate mais...")
            break
        else:
            print()


if __name__ == "__main__":
    main()
