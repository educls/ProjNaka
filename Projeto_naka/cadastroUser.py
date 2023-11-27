from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from userControl import UserControl

class CadastroUsuario:
    tela=None
    def __init__(self):
        self.userControle=UserControl()
        app=QtWidgets.QApplication([])
        self.tela=uic.loadUi("TelaProj.ui")
        ##self.tela.leBusca.focusOutEvent = self.consultarFocusOut
        self.tela.pbCadastrar.clicked.connect(self.cadastrar)
        self.tela.pbAtualizar.clicked.connect(self.atualizar)
        self.tela.pbExcluir.clicked.connect(self.excluir)
        self.tela.leBusca.editingFinished.connect(self.consultar)
        self.tela.lvUsuarioList.clicked.connect(self.itemClicado)
        self.tela.leIdUsuario.setEnabled(False)
        self.tela.pbAtualizar.setEnabled(False)
        self.tela.pbCadastrar.setEnabled(True)
        self.tela.pbExcluir.setEnabled(False)
        self.tela.show()
        app.exec()

    ##def consultarFocusOut(self, event):
    ##    QtWidgets.QLineEdit.focusOutEvent(self.tela.leBusca, event)
    ##    self.consultar()

    def consultar(self):
        dados=self.userControle.consultar(self.tela.leBusca.text())

        if dados==None:
            return True

        model = QStandardItemModel()

        item = QStandardItem(str(dados[1]))
        model.appendRow([item])
        self.tela.lvUsuarioList.setModel(model)

        if dados:
            self.tela.pbAtualizar.setEnabled(True)
            self.tela.pbExcluir.setEnabled((True))
            self.tela.pbCadastrar.setEnabled(False)
        else:
            self.tela.pbExcluir.setEnabled(False)
            self.tela.pbAtualizar.setEnabled(False)
        return dados

    def cadastrar(self):

        if self.tela.checkAdm.isChecked():
            checkadm = "administrador"
        else:
            checkadm = "usuario"

        if self.userControle.cadastrar(self.tela.leIdUsuario.text(),
                                    self.tela.leNome.text(),
                                    self.tela.leSenha.text(),
                                    checkadm):
            print("Usuario Cadastrado!")
            self.limpar()

    def atualizar(self):

        if self.tela.checkAdm.isChecked():
            checkadm = "administrador"
        else:
            checkadm = "usuario"

        if self.userControle.atualizar(self.tela.leNome.text(),
                                            self.tela.leSenha.text(),
                                            checkadm):
            print('Usuario atualizado')
            self.limpar()

        self.tela.leNome.setEnabled(True)

    def excluir(self):
        if self.userControle.excluir(self.tela.leIdUsuario.text()):
            print('Usuario deletado')
            self.limpar()
        self.tela.leNome.setEnabled(True)

    def limpar(self):
        self.tela.leIdUsuario.setText('')
        self.tela.leNome.setText('')
        self.tela.leSenha.setText('')
        self.tela.leBusca.setText('')
        self.tela.checkAdm.setChecked(False)
        self.tela.checkUser.setChecked(False)
        self.tela.leIdUsuario.setFocus()
        self.tela.pbCadastrar.setEnabled(True)
        self.tela.pbAtualizar.setEnabled(False)
        self.tela.pbExcluir.setEnabled(False)


        self.tela.lvUsuarioList.setModel(None)

    def itemClicado(self, index):
        row = index.row()
        self.tela.leNome.setEnabled(False)
        linha = self.consultar()
        self.tela.leIdUsuario.setText(str(linha[0]))
        self.tela.leNome.setText(str(linha[1]))
        self.tela.leSenha.setText(str(linha[2]))
        if linha[3] == "administrador":
            self.tela.checkAdm.setChecked(True)
            self.tela.checkUser.setChecked(False)
        else:
            self.tela.checkUser.setChecked(True)
            self.tela.checkAdm.setChecked(False)




produto=CadastroUsuario()

##if dados[3] == "administrador":
##    self.tela.checkAdm.setChecked(True)
##else:
##    self.tela.checkUser.setChecked(False)
