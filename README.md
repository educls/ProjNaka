# ProjNaka

Script SQL para a criação do Banco

```mysql
CREATE DATABASE IF NOT EXISTS projnaka;

USE projnaka;

CREATE TABLE Usuarios(
  idUsuario INT NOT NULL AUTO_INCREMENT,
  nomeUsuario VARCHAR(45) NOT NULL,
  senha VARCHAR(45) NOT NULL,
  contaTipo VARCHAR(45) NOT NULL,
  PRIMARY KEY (idUsuario)
);
```

## Mysql Connector
```bash
$ pip install mysql-connector-python
```


## PyQt5
```bash
$ pip install PyQt5
```


## PyQt5 Tools
```bash
$ pip install PyQt5-Tools
```


## PyQt5 Designer
```bash
$ pip install PyQtDesigner
```
