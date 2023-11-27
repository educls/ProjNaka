# ProjNaka

Script SQL para a criação do Banco

```mysql
CREATE TABLE Usuarios(
  idUsuario INT NOT NULL AUTO_INCREMENT,
  nomeUsuario VARCHAR(45) NOT NULL,
  senha VARCHAR(45) NOT NULL,
  contaTipo VARCHAR(45) NOT NULL,
  PRIMARY KEY (idUsuario)
);
```
