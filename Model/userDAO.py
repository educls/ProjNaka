import mysql.connector


class UserDAO:
    def conectaBD(self):
        self.con = mysql.connector.connect(host="localhost",
                                           database="projnaka",
                                           user="root",
                                           password="")
        if self.con.is_connected():
            self.cursor = self.con.cursor()
            return True
        return False

    def desconectaBD(self):
        self.con.close()


    def insert(self, idUsuario, nomeUsuario, senha, contaTipo):
        sql='insert into produto values (%s, %s, %s, %s)'
        values=(idUsuario, nomeUsuario, senha, contaTipo)
        self.cursor.execute(sql, values)
        self.con.commit()
        return self.cursor.rowcount > 0

    def update(self, nomeUsuario, senha, contaTipo):
        sql = 'update usuarios set nomeUsuario=%s, senha=%s where tipoConta=%s'
        values=(nomeUsuario, senha, contaTipo)
        if self.conectaBD():
            self.cursor.execute(sql, values)
            if self.cursor.rowcount > 0:
                self.con.commit()
                self.desconectaBD()
                return True
            self.desconectaBD()
        return False

    def delete(self, idUsuario):
        sql = 'delete from usuarios where idUsuario='+str(idUsuario)
        if self.conectaBD():
            self.cursor.execute(sql)
            if self.cursor.rowcount > 0:
                self.con.commit()
                self.desconectaBD()
                return True
            self.desconectaBD()
        return False