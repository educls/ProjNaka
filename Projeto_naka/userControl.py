from user_model import UserModel
from user_dao import UserDAO


class UserControl:
    user=None
    userDAO=UserDAO()

    def cadastrar(self, idUsuario, nomeUsuario, senha, tipoConta):
        self.user=UserModel(idUsuario, nomeUsuario, senha, tipoConta)
        return self.userDAO.insert(self.user)
    
    def consultar(self, nomeUsuario):
        self.user=self.userDAO.select(nomeUsuario)
        if self.user==None:
            return None
        dados=(str(self.user.getIdUsuario()),
               self.user.getNomeUsuario(),
               str(self.user.getSenha()),
               str(self.user.getTipoConta()))
        return dados
    
    def consultarLike(self, filtro):
        resultado=self.userDAO.selectLike(filtro)
        lista=[]
        for dados in resultado:
            linha=(str(dados.getIdUsuario()), dados.getNomeUsuario())
            lista.append(linha)
        return lista    

    def atualizar(self, nomeUsuario, senha, contaTipo):
        if self.user!=None and self.user.getNomeUsuario()==nomeUsuario:
            self.user.setSenha(senha)
            self.user.setTipoConta(contaTipo)
            return self.userDAO.update(self.user)

    def excluir(self, idUsuario):
        if self.user!=None and self.user.getIdUsuario()==int(idUsuario):
            self.user=None
            return self.userDAO.delete(int(idUsuario))





# pc=userutoControle()
# '''
# if pc.cadastrar('102','Pendrive 256G', '100.0', '10'):
#     print('useruto cadastrado!')
# '''
# dados=pc.consultar('101')
# if dados!=None:
#     print (dados)
# if pc.vender('101', '15'):
#     print('useruto vendido!')