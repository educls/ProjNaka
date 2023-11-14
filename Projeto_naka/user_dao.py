from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

from user_model import UserModel

class UserDAO:
    def conectar(self):
        self.con = mysql.connector.connect(host="localhost",
                                           database="projnaka",
                                           user="root",
                                           password="")
        if self.con.is_connected():
            self.cursor = self.con.cursor()
            return True
        return False

    def disconnect(self):
        try:
            if self.con.is_connected():
                self.con.close()
                print("Conexão fechada com sucesso.")
        except Exception as e:
            print(f"Erro ao fechar a conexão: {e}")

    def insert(self, user):
        sql = 'insert into usuarios values (%s, %s, %s, %s)'
        values = (user.getIdUsuario(), user.getNomeUsuario(),
                  user.getSenha(), user.getTipoConta())
        if self.conectar():
            self.cursor.execute(sql, values)
            if self.cursor.rowcount > 0:
                self.con.commit()
                self.disconnect()
                return True
            self.disconnect()
        return False

    def update(self, user):
        sql = 'update usuarios set senha=%s, contaTipo=%s where idUsuario=%s'
        values = (user.getSenha(), user.getTipoConta(), user.getIdUsuario())
        if self.conectar():
            self.cursor.execute(sql, values)
            if self.cursor.rowcount > 0:
                self.con.commit()
                self.disconnect()
                return True
            self.disconnect()
        return False

    def delete(self, idUsuario):
        sql = 'delete from usuarios where idUsuario= %s'
        if self.conectar():
            self.cursor.execute(sql, (idUsuario, ))
            if self.cursor.rowcount > 0:
                self.con.commit()
                self.disconnect()
                return True
            self.disconnect()
        return False

    def select(self, nomeUsuario):
        sql = 'select * from usuarios where nomeUsuario= %s'
        if self.conectar():
            self.cursor.execute(sql, (nomeUsuario, ))
            dados = self.cursor.fetchone()
            self.disconnect()
            if dados is not None:
                user = UserModel(dados[0], dados[1], dados[2], dados[3])
                return user
            self.disconnect()
        return None
