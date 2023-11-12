class Usuario:
    def __init__(self, IdUsuario, nomeUsuario, senha, contaTipo):
        self.IdUsuario=IdUsuario
        self.nomeUsuario=nomeUsuario
        self.senha=senha
        self.contaTipo=contaTipo
        
    def getIdUsuario(self):
        return self.IdUsuario

    def getNomeUsuario(self):
        return self.nomeUsuario

    def getSenha(self):
        return self.senha

    def getContaTipo(self):
        return self.contaTipo