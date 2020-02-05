# DECLARANDO LISTA
clients = ["CLIENTE 0", "CLIENTE 1", "CLIENTE 2"]
print(clients)

# EXIBINDO ÍNDICE ZERO
print(clients[0])

# ADICIONANDO ELEMENTOS NO FINAL DA LISTA
clients.append("CLIENTE 4")
clients.append("CLIENTE 5")
clients.append("CLIENTE 3")
print(clients)

# ORDENANDO LISTA EM ORDEM DE PRECEDÊNCIA
clients.sort()
print(clients)

# INVERTENDO ORDEM DE EXIBIÇÃO DA LISTA
clients.reverse()
print(clients)

# REMOVENDO ELEMENTO DA LISTA clients PELO VALOR. REMOVE A PRIMEIRA OCORRÊNCIA.
clients.remove("CLIENTE 2")
clients.remove("CLIENTE 1")
clients.remove("CLIENTE 0")
print(clients)

clients.sort()

# ADICIONANDO ELEMENTOS NO ÍNCIDE ESPECIFICADO
clients.insert(3, "CLIENTE 6")
print(clients)

# REMOVE TODOS OS ELEMENTOS DA LISTA
clients.clear()
print(clients)
