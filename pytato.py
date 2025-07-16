class Contact:
    def __init__(self, name, phone, email, favorite=False):
        self.name = name
        self.phone = phone
        self.email = email
        self.favorite = favorite

    def __str__(self):
        fav_mark = "⭐" if self.favorite else ""
        return f"{self.name} {fav_mark}\n  Telefone: {self.phone}\n  Email: {self.email}"


contacts = []


def add_contact():
    print("\nAdicionar Novo Contato")
    name = input("Nome: ")
    phone = input("Telefone: ")
    email = input("Email: ")
    contacts.append(Contact(name, phone, email))
    print(f"Contato '{name}' adicionado com sucesso!\n")


def view_contacts(list_to_view=None):
    print("\nLista de Contatos:")
    lista = list_to_view if list_to_view is not None else contacts
    if not lista:
        print("Nenhum contato encontrado.\n")
        return
    for idx, contact in enumerate(lista, 1):
        print(f"{idx}. {contact}")
    print()


def edit_contact():
    if not contacts:
        print("Nenhum contato para editar.\n")
        return
    view_contacts()
    try:
        idx = int(input("Digite o número do contato para editar: ")) - 1
        contact = contacts[idx]
    except (ValueError, IndexError):
        print("Seleção inválida.\n")
        return
    print("Pressione Enter para manter o valor atual.")
    new_name = input(f"Nome ({contact.name}): ") or contact.name
    new_phone = input(f"Telefone ({contact.phone}): ") or contact.phone
    new_email = input(f"Email ({contact.email}): ") or contact.email
    contact.name = new_name
    contact.phone = new_phone
    contact.email = new_email
    print(f"Contato '{contact.name}' atualizado com sucesso!\n")


def toggle_favorite():
    if not contacts:
        print("Nenhum contato para marcar/desmarcar favorito.\n")
        return
    view_contacts()
    try:
        idx = int(input("Digite o número do contato para marcar/desmarcar favorito: ")) - 1
        contact = contacts[idx]
    except (ValueError, IndexError):
        print("Seleção inválida.\n")
        return
    contact.favorite = not contact.favorite
    status = "favorito" if contact.favorite else "removido dos favoritos"
    print(f"Contato '{contact.name}' {status}.\n")


def view_favorites():
    favs = [c for c in contacts if c.favorite]
    print("\nContatos Favoritos:")
    view_contacts(list_to_view=favs)


def delete_contact():
    if not contacts:
        print("Nenhum contato para apagar.\n")
        return
    view_contacts()
    try:
        idx = int(input("Digite o número do contato para apagar: ")) - 1
        contact = contacts.pop(idx)
        print(f"Contato '{contact.name}' apagado com sucesso!\n")
    except (ValueError, IndexError):
        print("Seleção inválida.\n")


def main_menu():
    menu = {
        '1': ('Adicionar contato', add_contact),
        '2': ('Ver todos os contatos', view_contacts),
        '3': ('Editar contato', edit_contact),
        '4': ('Marcar/Desmarcar favorito', toggle_favorite),
        '5': ('Ver contatos favoritos', view_favorites),
        '6': ('Apagar contato', delete_contact),
        '0': ('Sair', None)
    }
    while True:
        print("\n=== Gerenciador de Contatos ===")
        for key, (desc, _) in menu.items():
            print(f"{key} - {desc}")
        choice = input("Escolha uma opção: ")
        action = menu.get(choice)
        if not action:
            print("Opção inválida. Tente novamente.\n")
            continue
        if choice == '0':
            print("Encerrando aplicação. Até logo!")
            break
        _, func = action
        func()


if __name__ == '__main__':
    main_menu()
