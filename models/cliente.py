import json
class Cliente:
    def __init__(self, id : int, nome, email, fone, senha, adm : bool = False):
        self.id = id 
        self.nome = nome
        self.email = email
        self.fone = fone
        self.senha = senha
        self.adm = adm
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"

class Clientes:
    objetos = [] 
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for x in cls.objetos:
            if x.id > id: id = x.id

        obj.id = id + 1    

        cls.objetos.append(obj)
        cls.salvar()


    @classmethod
    def listar(cls):
        
        cls.abrir()
        return cls.objetos
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for x in cls.objetos:
            if x.id == id: return x
        return None
    
    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            #x.nome = obj.nome
            #x.email = obj.email
            #x.fone = obj.fone
            cls.salvar()        

    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.salvar()        

    @classmethod
    def salvar(cls):
        # open - cria e abre o arquivo clientes.json
        # vars - converte um objeto em um dicionário
        # dump - pega a lista de objetos e salva no arquivo
        with open("data/user.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("data/user.json", mode="r") as arquivo:
                clientes_json = json.load(arquivo)
                for obj in clientes_json:
                    c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"], obj["senha"], obj["adm"])
                    cls.objetos.append(c)    

        except FileNotFoundError:
            pass
    

