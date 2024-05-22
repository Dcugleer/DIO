#a primeira parte do desafio, você precisará implementar uma aplicação que integre com SQLite utilizando SQLAlchemy. 

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Criando a conexão com o banco de dados SQLite
engine = create_engine('sqlite:///clientes_contas.db', echo=True)

# Criando uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Declarando a base para as classes do SQLAlchemy
Base = declarative_base()

# Definindo as classes correspondentes às tabelas do banco de dados
class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    endereco = Column(String)
    telefone = Column(String)
    email = Column(String)

    contas = relationship("Conta", back_populates="cliente")


class Conta(Base):
    __tablename__ = 'contas'

    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    saldo = Column(Integer)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))

    cliente = relationship("Cliente", back_populates="contas")

# Criando as tabelas no banco de dados
Base.metadata.create_all(engine)

# Inserindo um conjunto mínimo de dados para manipulação
cliente1 = Cliente(nome='Fulano', endereco='Rua X', telefone='123456', email='fulano@example.com')
cliente2 = Cliente(nome='Ciclano', endereco='Rua Y', telefone='789012', email='ciclano@example.com')

conta1 = Conta(tipo='Corrente', saldo=1000)
conta2 = Conta(tipo='Poupança', saldo=500)

cliente1.contas.append(conta1)
cliente2.contas.append(conta2)

session.add_all([cliente1, cliente2])
session.commit()

# Exemplo de recuperação de dados
clientes = session.query(Cliente).all()
for cliente in clientes:
    print("Cliente:", cliente.nome)
    for conta in cliente.contas:
        print("   Conta:", conta.tipo, "- Saldo:", conta.saldo)



# Para a segunda parte, você irá implementar um banco de dados NoSQL com MongoDB usando pymongo

import pymongo

# Conectando ao MongoDB Atlas
client = pymongo.MongoClient("mongodb+srv://<username>:<password>@<cluster-url>/test?retryWrites=true&w=majority")
db = client['banco']
collection = db['clientes']

# Inserindo documentos com a estrutura mencionada
cliente1_doc = {
    "nome": "Fulano",
    "endereco": "Rua X",
    "telefone": "123456",
    "email": "fulano@example.com",
    "contas": [
        {"tipo": "Corrente", "saldo": 1000},
        {"tipo": "Poupança", "saldo": 500}
    ]
}

cliente2_doc = {
    "nome": "Ciclano",
    "endereco": "Rua Y",
    "telefone": "789012",
    "email": "ciclano@example.com",
    "contas": [
        {"tipo": "Investimento", "saldo": 2000},
        {"tipo": "Poupança", "saldo": 1000}
    ]
}

collection.insert_many([cliente1_doc, cliente2_doc])

# Recuperação de informações com base nos pares de chave e valor
cliente = collection.find_one({"nome": "Fulano"})
print("Cliente:", cliente['nome'])
for conta in cliente['contas']:
    print("   Conta:", conta['tipo'], "- Saldo:", conta['saldo'])


#
Para a primeira parte do desafio, você precisará implementar uma aplicação que integre com SQLite utilizando SQLAlchemy. Aqui está um exemplo de como você pode estruturar suas classes baseadas no esquema fornecido:

python
Copiar código
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Criando a conexão com o banco de dados SQLite
engine = create_engine('sqlite:///clientes_contas.db', echo=True)

# Criando uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Declarando a base para as classes do SQLAlchemy
Base = declarative_base()

# Definindo as classes correspondentes às tabelas do banco de dados
class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    endereco = Column(String)
    telefone = Column(String)
    email = Column(String)

    contas = relationship("Conta", back_populates="cliente")


class Conta(Base):
    __tablename__ = 'contas'

    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    saldo = Column(Integer)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))

    cliente = relationship("Cliente", back_populates="contas")

# Criando as tabelas no banco de dados
Base.metadata.create_all(engine)

# Inserindo um conjunto mínimo de dados para manipulação
cliente1 = Cliente(nome='Fulano', endereco='Rua X', telefone='123456', email='fulano@example.com')
cliente2 = Cliente(nome='Ciclano', endereco='Rua Y', telefone='789012', email='ciclano@example.com')

conta1 = Conta(tipo='Corrente', saldo=1000)
conta2 = Conta(tipo='Poupança', saldo=500)

cliente1.contas.append(conta1)
cliente2.contas.append(conta2)

session.add_all([cliente1, cliente2])
session.commit()

# Exemplo de recuperação de dados
clientes = session.query(Cliente).all()
for cliente in clientes:
    print("Cliente:", cliente.nome)
    for conta in cliente.contas:
        print("   Conta:", conta.tipo, "- Saldo:", conta.saldo)
Para a segunda parte, você irá implementar um banco de dados NoSQL com MongoDB usando pymongo. Aqui está um exemplo de como você pode fazer isso:

python
Copiar código
import pymongo

# Conectando ao MongoDB Atlas
client = pymongo.MongoClient("mongodb+srv://<username>:<password>@<cluster-url>/test?retryWrites=true&w=majority")
db = client['banco']
collection = db['clientes']

# Inserindo documentos com a estrutura mencionada
cliente1_doc = {
    "nome": "Fulano",
    "endereco": "Rua X",
    "telefone": "123456",
    "email": "fulano@example.com",
    "contas": [
        {"tipo": "Corrente", "saldo": 1000},
        {"tipo": "Poupança", "saldo": 500}
    ]
}

cliente2_doc = {
    "nome": "Ciclano",
    "endereco": "Rua Y",
    "telefone": "789012",
    "email": "ciclano@example.com",
    "contas": [
        {"tipo": "Investimento", "saldo": 2000},
        {"tipo": "Poupança", "saldo": 1000}
    ]
}

collection.insert_many([cliente1_doc, cliente2_doc])

# Recuperação de informações com base nos pares de chave e valor
cliente = collection.find_one({"nome": "Fulano"})
print("Cliente:", cliente['nome'])
for conta in cliente['contas']:
    print("   Conta:", conta['tipo'], "- Saldo:", conta['saldo'])
  
# Certifique-se de substituir <username>, <password> e <cluster-url>com suas credenciais e URL do seu cluster MongoDB Atlas.
#Este código assume que você já configurou um cluster no MongoDB Atlas e tem as credenciais adequadas para acessá-lo.





