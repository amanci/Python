from registro import Registro

class Main:

  agenda = []


  @staticmethod
  def CadastrarContato(lista_reg = []):

    opcao_sair = int(-1)

    while True:

      nome = str("")
      telefone = str("")
      aniversario = str("")

      nome = input("NOME: ")

      telefone = input("TELEFONE: ")

      aniversario = input("ANIVERSARIO: ")

      registro = Registro(nome, telefone, aniversario)

      lista_reg.append(registro)
      
      print("REALIZAR OUTRO CADASTRO ?")
      print(" [1] CONTINUAR \n [2] SAIR")
      opcao_sair = int(input("SELECIONE A OPÇÃO: "))
      
      if opcao_sair != 1:
        break

    return lista_reg


  @staticmethod
  def RemoverContatos(lista_reg = []):
    
    id_contato = int(-1)
    tipo_busca = int(-1)
    
    Main.ListarContatos(lista_reg)
    
    id_contato = int(input("DIGITE O ID: "))
    
    print("CONTATO REMOVIDO")
    print()
    print(f"ID: {id_contato} | NOME: {lista_reg[id_contato -1].nome} | TELEFONE: {lista_reg[id_contato - 1].telefone} | ANIVERSÁRIO: {lista_reg[id_contato - 1].aniversario}")
    lista_reg.pop(id_contato - 1)

    return lista_reg


  @staticmethod
  def AtualizarContatos(lista_reg = []):
    
    id_contato = int(-1)
    tipo_busca = int(-1)
    nome = str("")

    Main.ListarContatos(lista_reg)

    id_contato = int(input("DIGITE O ID: "))

    print(" [1] NOME \n [2] TELEFONE \n [3] ANIVERSÁRIO \n [4] TODOS")
    print()
    tipo_busca = int(input("OPÇÃO: "))

    if tipo_busca == 1:
      nome = input("NOME: ")
      lista_reg[id_contato -1].nome = nome
      
    elif tipo_busca == 2:
      telefone = input("TELEFONE: ")
      lista_reg[id_contato -1].telefone = telefone
      
    elif tipo_busca == 3:
      aniversario = input("ANIVERSÁRIO: ")
      lista_reg[id_contato -1].aniversario = aniversario
      
    elif tipo_busca == 4:
      nome = input("NOME: ")
      lista_reg[id_contato -1].nome = nome
      
      telefone = input("TELEFONE: ")
      lista_reg[id_contato -1].telefone = telefone
      
      aniversario = input("ANIVERSÁRIO: ")
      lista_reg[id_contato -1].aniversario = aniversario
    else:
      print("OPÇÃO INVÁLIDA")
      
    return lista_reg


  @staticmethod
  def ListarContatos(lista_reg = []):
        
    id_contato = int(1)

    for contato in lista_reg:
      print(f"ID: {id_contato} | NOME: {contato.nome} | TELEFONE: {contato.telefone} | ANIVERSÁRIO {contato.aniversario}")
      id_contato+=1
      
      
Main.agenda = Main.CadastrarContato(Main.agenda)

Main.agenda = Main.RemoverContatos(Main.agenda)

Main.agenda = Main.AtualizarContatos(Main.agenda)

Main.ListarContatos(Main.agenda)