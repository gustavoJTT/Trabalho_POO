import json
class Categoria:
    def __init__(self, id, descricao):
        self.id = id 
        self.descricao = descricao
    def __str__(self):
        return f"{self.id} - {self.descricao}"

class Categorias:
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
        with open("data/categorias.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("data/categorias.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo)
                for obj in objetos_json:
                    c = Categoria(obj["id"], obj["descricao"])
                    cls.objetos.append(c)    
        except FileNotFoundError:
            pass
    

