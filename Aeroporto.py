class Usuario:
    def __init__(self, login, senha, nivel_acesso):
        self.login = login
        self.senha = senha
        self.nivel_acesso = nivel_acesso  # Ex: 'rh', 'voo', 'admin'

    def tem_acesso(self, area):
        permissoes = {
            'rh': ['rh', 'relatorio'],
            'voo': ['voo', 'relatorio'],
            'admin': ['rh', 'voo', 'relatorio']
        }
        return area in permissoes.get(self.nivel_acesso, [])

class Funcionario:
    def __init__(self, id_funcionario, nome, cargo, departamento):
        self.id_funcionario = id_funcionario
        self.nome = nome
        self.cargo = cargo
        self.departamento = departamento

    def __str__(self):
        return f"{self.nome} - {self.cargo} ({self.departamento})"

class RH:
    def __init__(self):
        self.funcionarios = []

    def contratar(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        if not self.funcionarios:
            print("Nenhum funcionário cadastrado.")
        for f in self.funcionarios:
            print(f"{f.id_funcionario}: {f.nome} - {f.cargo} ({f.departamento})")

    def excluir_funcionario(self, id_funcionario):
        for funcionario in self.funcionarios:
            if funcionario.id_funcionario == id_funcionario:
                self.funcionarios.remove(funcionario)
                print(f"Funcionário {funcionario.nome} removido com sucesso.")
                return True
        print("Funcionário não encontrado.")
        return False

class Companhia:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def renomear(self, novo_nome):
        self.nome = novo_nome

class Aviao:
    def __init__(self, codigo, modelo, capacidade):
        self.codigo = codigo
        self.modelo = modelo
        self.capacidade = capacidade
        self.status = "disponível"

class Voo:
    def __init__(self, codigo_voo, partida, destino, aviao, modelo_voo):
        self.codigo_voo = codigo_voo
        self.partida = partida
        self.destino = destino
        self.aviao = aviao
        self.modelo_voo = modelo_voo
        self.bagagens = []
        self.funcionarios = []

    def adicionar_bagagem(self, bagagem):
        self.bagagens.append(bagagem)

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

class Bagagem:
    def __init__(self, id_bagagem, peso, dono):
        self.id_bagagem = id_bagagem
        self.peso = peso
        self.dono = dono

class Aeroporto:
    def __init__(self, nome):
        self.nome = nome
        self.voos = []
        self.avioes = []
        self.rh = RH()
        self.companhias = []

    def adicionar_voo(self, voo):
        self.voos.append(voo)

    def adicionar_aviao(self, aviao):
        self.avioes.append(aviao)

    def gerar_relatorio(self):
        print("\n--- RELATÓRIO DO AEROPORTO ---")
        print(f"Total de aviões: {len(self.avioes)}")
        print(f"Total de voos: {len(self.voos)}")
        print(f"Total de funcionários: {len(self.rh.funcionarios)}")

    def listar_voos(self):
        if not self.voos:
            print("Nenhum voo cadastrado.")
        for voo in self.voos:
            print(f"Código: {voo.codigo_voo}, Partida: {voo.partida}, Destino: {voo.destino}, Modelo: {voo.modelo_voo}")

    def listar_avioes(self):
        if not self.avioes:
            print("Nenhum avião cadastrado.")
        for aviao in self.avioes:
            print(f"Código: {aviao.codigo}, Modelo: {aviao.modelo}, Capacidade: {aviao.capacidade}")

    def adicionar_companhia(self, companhia):
        self.companhias.append(companhia)
        print(f"Companhia {companhia.nome} cadastrada com sucesso.")

    def renomear_companhia(self, codigo, novo_nome):
        for companhia in self.companhias:
            if companhia.codigo == codigo:
                companhia.renomear(novo_nome)
                print(f"Companhia {codigo} renomeada para {novo_nome}.")
                return
        print("Companhia não encontrada.")

    def transferir_funcionario(self, id_funcionario, nova_companhia):
        for funcionario in self.rh.funcionarios:
            if funcionario.id_funcionario == id_funcionario:
                for companhia in self.companhias:
                    if companhia.codigo == nova_companhia:
                        companhia.adicionar_funcionario(funcionario)
                        print(f"Funcionário {funcionario.nome} transferido para a companhia {nova_companhia}.")
                        return
                print("Companhia de destino não encontrada.")
                return
        print("Funcionário não encontrado.")

def menu_voo(aeroporto):
    while True:
        print("\n--- Menu Voo ---")
        print("1. Adicionar Modelo do Avião")
        print("2. Adicionar Companhia do Avião")
        print("3. Adicionar Código do Avião")
        print("4. Adicionar Destino do Avião")
        print("5. Excluir Avião")
        print("6. Adicionar Partida/Ida do Avião")
        print("7. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            modelo_voo = input("Informe o Modelo do Avião: ")
            aviao_codigo = input("Código do Avião: ")
            aviao = Aviao(aviao_codigo, modelo_voo, 150)  # Exemplo de capacidade de 150
            aeroporto.adicionar_aviao(aviao)
            print(f"Avião {aviao_codigo} com modelo {modelo_voo} adicionado com sucesso.")

        elif opcao == "2":
            aviao_codigo = input("Informe o Código do Avião: ")
            companhia_nome = input("Informe o nome da Companhia: ")
            companhia = None
            for comp in aeroporto.companhias:
                if comp.nome == companhia_nome:
                    companhia = comp
                    break
            if companhia:
                for aviao in aeroporto.avioes:
                    if aviao.codigo == aviao_codigo:
                        companhia.adicionar_funcionario(Funcionario("1", "Piloto", "Piloto", "Avião"))
                        print(f"Avião {aviao_codigo} foi associado à companhia {companhia_nome}.")
                        return
            else:
                print(f"Companhia {companhia_nome} não encontrada.")

        elif opcao == "3":
            aviao_codigo = input("Informe o Código do Avião: ")
            aviao = None
            for a in aeroporto.avioes:
                if a.codigo == aviao_codigo:
                    aviao = a
                    break
            if aviao:
                novo_codigo = input("Digite o novo código para o avião: ")
                aviao.codigo = novo_codigo
                print(f"Código do avião alterado para {novo_codigo}.")
            else:
                print("Avião não encontrado.")

        elif opcao == "4":
            aviao_codigo = input("Informe o Código do Avião: ")
            aviao = None
            for a in aeroporto.avioes:
                if a.codigo == aviao_codigo:
                    aviao = a
                    break
            if aviao:
                destino = input("Informe o destino do voo: ")
                partida = input("Informe a partida do voo: ")
                print(f"Destino e partida definidos: Partida: {partida}, Destino: {destino}.")
            else:
                print("Avião não encontrado.")

        elif opcao == "5":
            aviao_codigo = input("Informe o Código do Avião para excluir: ")
            aviao = None
            for a in aeroporto.avioes:
                if a.codigo == aviao_codigo:
                    aviao = a
                    break
            if aviao:
                aeroporto.avioes.remove(aviao)
                print(f"Avião {aviao_codigo} excluído com sucesso.")
            else:
                print("Avião não encontrado.")

        elif opcao == "6":
            aviao_codigo = input("Informe o Código do Avião para adicionar partida: ")
            aviao = None
            for a in aeroporto.avioes:
                if a.codigo == aviao_codigo:
                    aviao = a
                    break
            if aviao:
                partida = input("Informe o local de partida do voo: ")
                print(f"Partida do avião {aviao_codigo} registrada com sucesso: {partida}.")
            else:
                print("Avião não encontrado.")

        elif opcao == "7":
            break

        else:
            print("Opção inválida!")

def menu_rh(aeroporto):
    while True:
        print("\n--- Menu RH ---")
        print("1. Contratar Funcionário")
        print("2. Listar Funcionários")
        print("3. Excluir Funcionário")
        print("4. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do Funcionário: ")
            id_funcionario = input("ID do Funcionário: ")
            cargo = input("Cargo do Funcionário: ")
            departamento = input("Departamento do Funcionário: ")
            funcionario = Funcionario(id_funcionario, nome, cargo, departamento)
            aeroporto.rh.contratar(funcionario)
            print(f"Funcionário {nome} contratado com sucesso.")

        elif opcao == "2":
            aeroporto.rh.listar_funcionarios()

        elif opcao == "3":
            id_funcionario = input("Informe o ID do funcionário para excluir: ")
            aeroporto.rh.excluir_funcionario(id_funcionario)

        elif opcao == "4":
            break

        else:
            print("Opção inválida!")

def menu_admin(aeroporto):
    while True:
        print("\n--- Menu Admin ---")
        print("1. Gerar Relatório")
        print("2. Listar Voos")
        print("3. Listar Aviões")
        print("4. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            aeroporto.gerar_relatorio()

        elif opcao == "2":
            aeroporto.listar_voos()

        elif opcao == "3":
            aeroporto.listar_avioes()

        elif opcao == "4":
            break

        else:
            print("Opção inválida!")

def login():
    login = input("Login: ")
    senha = input("Senha: ")
    for usuario in usuarios:
        if usuario.login == login and usuario.senha == senha:
            print(f"Login bem-sucedido! Bem-vindo, {login}.")
            return usuario
    print("Credenciais inválidas. Tente novamente.")
    return None

def cadastrar_usuario():
    login = input("Escolha um nome de usuário: ")
    senha = input("Escolha uma senha: ")
    nivel_acesso = input("Escolha um nível de acesso (rh, voo, admin): ")
    novo_usuario = Usuario(login, senha, nivel_acesso)
    usuarios.append(novo_usuario)
    print(f"Usuário {login} cadastrado com sucesso.")

def redefinir_senha():
    login = input("Informe o login do usuário: ")
    for usuario in usuarios:
        if usuario.login == login:
            nova_senha = input("Informe a nova senha: ")
            usuario.senha = nova_senha
            print(f"Senha do usuário {login} foi redefinida com sucesso.")
            return
    print("Usuário não encontrado.")

def menu_principal():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Login")
        print("2. Cadastrar Usuário")
        print("3. Redefinir Senha")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            usuario = login()
            if usuario:
                aeroporto = Aeroporto("Aeroporto Internacional")
                if usuario.nivel_acesso == "admin":
                    menu_admin(aeroporto)
                elif usuario.tem_acesso("rh"):
                    menu_rh(aeroporto)
                elif usuario.tem_acesso("voo"):
                    menu_voo(aeroporto)
                else:
                    print("Acesso não autorizado.")
        elif opcao == "2":
            cadastrar_usuario()
        elif opcao == "3":
            redefinir_senha()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

# Início do programa
usuarios = [
    Usuario("rhuser", "rh123", "rh"),
    Usuario("voouser", "voo123", "voo"),
    Usuario("admin", "admin123", "admin")
]

menu_principal()
