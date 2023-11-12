from Model.userModel import Usuario

class UserControl:
    Usuario=None
    userDAO=UserDAO()

    def cadastrar(self, nomeUsuario, senha, contaTipo):

        idUsuario=''
        nomeUsuario=nomeUsuario
        senha=senha
        contaTipo=contaTipo


        values=(idUsuario, nomeUsuario, senha, contaTipo)
        self.cursor.execute(sql, values)
        if self.cursor.rowcount>0:
            self.con.commit()
            print("Usuário cadastrado")
        else:
            print("Usuário não cadastrado")