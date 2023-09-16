class AgendaTelefonica:
    def __init__(self):
        self.contatos = {}  # Um dicionário para armazenar os contatos

    def adicionar_contato(self, nome, telefone, email, twitter, instagram):
        # Adiciona um novo contato ao dicionário de contatos
        self.contatos[nome] = {
            'telefone': telefone,
            'email': email,
            'twitter': twitter,
            'instagram': instagram
        }
        print(f"Contato '{nome}' adicionado com sucesso!")

    def consultar_contato(self, nome):
        # Consulta um contato pelo nome e retorna seus dados, se encontrado
        if nome in self.contatos:
            return self.contatos[nome]
        else:
            return None

    def remover_contato(self, nome):
        # Remove um contato da lista de contatos, se encontrado
        if nome in self.contatos:
            del self.contatos[nome]
            print(f"Contato '{nome}' removido com sucesso!")
        else:
            print(f"Contato '{nome}' não encontrado na agenda.")

    def alterar_contato(self, nome, telefone, email, twitter, instagram):
        # Altera os dados de um contato, se encontrado
        if nome in self.contatos:
            self.contatos[nome]['telefone'] = telefone
            self.contatos[nome]['email'] = email
            self.contatos[nome]['twitter'] = twitter
            self.contatos[nome]['instagram'] = instagram
            print(f"Dados do contato '{nome}' alterados com sucesso!")
        else:
            print(f"Contato '{nome}' não encontrado na agenda.")

    def adicionar_multiplos_contatos(self, quantidade):
        # Adiciona múltiplos contatos de uma vez
        for _ in range(quantidade):
            print(f"\nInclusão do {len(self.contatos) + 1}º contato:")
            nome = input("Nome do contato: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            twitter = input("Conta do Twitter: ")
            instagram = input("Conta do Instagram: ")
            self.adicionar_contato(nome, telefone, email, twitter, instagram)

    def gerar_relatorio(self):
        # Gera um relatório formatado dos contatos e seus dados
        print("Nro\tNome\t\te-mail\t\tTwitter\t\tInstagram")
        for idx, (nome, dados) in enumerate(self.contatos.items(), start=1):
            print(f"{idx}\t{nome}\t\t{dados['email']}\t{dados['twitter']}\t{dados['instagram']}")

    def menu(self):
        # Esse é menu
        while True:
            print("\nMenu:")
            print("1. Adicionar Contato")
            print("2. Consultar Contato")
            print("3. Remover Contato")
            print("4. Alterar Contato")
            print("5. Incluir Múltiplos Contatos")
            print("6. Gerar Relatório")
            print("7. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                nome = input("Nome do contato: ")
                telefone = input("Telefone: ")
                email = input("Email: ")
                twitter = input("Conta do Twitter: ")
                instagram = input("Conta do Instagram: ")
                self.adicionar_contato(nome, telefone, email, twitter, instagram)
            elif opcao == '2':
                nome = input("Nome do contato para consulta: ")
                contato = self.consultar_contato(nome)
                if contato:
                    print("Dados do Contato:")
                    print(f"Nome: {nome}")
                    print(f"Telefone: {contato['telefone']}")
                    print(f"Email: {contato['email']}")
                    print(f"Twitter: {contato['twitter']}")
                    print(f"Instagram: {contato['instagram']}")
                else:
                    print(f"Contato '{nome}' não encontrado na agenda.")
            elif opcao == '3':
                nome = input("Nome do contato para remover: ")
                self.remover_contato(nome)
            elif opcao == '4':
                nome = input("Nome do contato para alterar: ")
                if nome in self.contatos:
                    novo_nome = input("Novo nome: ")
                    telefone = input("Novo telefone: ")
                    email = input("Novo email: ")
                    twitter = input("Nova conta do Twitter: ")
                    instagram = input("Nova conta do Instagram: ")
                    self.contatos[novo_nome] = self.contatos.pop(nome)
                    self.alterar_contato(novo_nome, telefone, email, twitter, instagram)
                else:
                    print(f"Contato '{nome}' não encontrado na agenda.")
            elif opcao == '5':
                quantidade = int(input("Quantos contatos deseja adicionar? "))
                self.adicionar_multiplos_contatos(quantidade)
            elif opcao == '6':
                self.gerar_relatorio()
            elif opcao == '7':
                print("Saindo da agenda telefônica.")
                break
            else:
                print("Opção inválida. Escolha uma opção válida.")

# Criar uma instância da agenda telefônica
agenda = AgendaTelefonica()

# Executar o menu
agenda.menu()
