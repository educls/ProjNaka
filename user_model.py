class UserModel:
    def __init__(self, idUsuario, nomeUsuario, senha, contaTipo):
        self.idUsuario = idUsuario
        self.nomeUsuario = nomeUsuario
        self.senha = senha
        self.contaTipo = contaTipo
    
    def getIdUsuario(self):
        return self.idUsuario

    def getNomeUsuario(self):
        return self.nomeUsuario

    def getSenha(self):
        return self.senha

    def getTipoConta(self):
        return self.contaTipo

    def setSenha(self, senha):
        self.senha=senha

    def setTipoConta(self, contaTipo):
        self.contaTipo=contaTipo