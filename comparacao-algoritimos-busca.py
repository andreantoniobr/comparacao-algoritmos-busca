import random
import time
import matplotlib.pyplot as plt

# Geração de uma lista com números aleatórios entre valores que variam ate o tamanho da lista
def gerar_lista_aleatoria(tamanho=1000):
    return random.sample(range(0, tamanho + 1), tamanho)

# Busca Sequencial
def busca_sequencial(lista, alvo):
    comparacoes = 0
    for i, elemento in enumerate(lista):
        comparacoes += 1
        if elemento == alvo:
            return i, comparacoes
    return -1, comparacoes

# Busca Binária (lista precisa estar ordenada)
def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    comparacoes = 0
    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1
        if lista[meio] == alvo:
            return meio, comparacoes
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1, comparacoes

# Função para medir tempo e comparações
def comparar_algoritmos(lista, alvo, is_sorted=False):
    lista_ordenada = sorted(lista) #Ordena a lista, pois o algoritimo de busca binária precisa que a lista seja ordenada para encontrar o alvo.
    
    lista_seq = lista
    if(is_sorted):
        lista_seq = lista_ordenada #Se o algoritimo for comparar as listas ordenadas, entao a lista da busca linear vai ser ordenada tambem
    
    # --- Busca Sequencial ---
    inicio = time.perf_counter()
    indice_seq, comp_seq = busca_sequencial(lista_seq, alvo)
    tempo_seq = time.perf_counter() - inicio
   

    # --- Busca Binária ---    
    inicio = time.perf_counter()
    indice_bin, comp_bin = busca_binaria(lista_ordenada, alvo)
    tempo_bin = time.perf_counter() - inicio
    
    print("-"*30)    
    print(f"\nTamanho da lista: {len(lista)}")
    print(f"Alvo para ser encontrado: {alvo}")  
    
    print("\n--- Busca Sequencial ---")
    print(f"Índice na lista: {indice_seq} ")
    print(f"Comparações: {comp_seq}")
    print(f"Tempo: {tempo_seq:.8f} segundos")    

    print("\n--- Busca Binária ---")
    print(f"Índice na lista: {indice_bin} ")
    print(f"Comparações: {comp_bin}")
    print(f"Tempo: {tempo_bin:.8f} segundos")
    print("-"*30)  

    return tempo_seq, tempo_bin
    

# Executando os testes
def gerar_teste(tamanho, is_sorted=False):
    lista = gerar_lista_aleatoria(tamanho)    
    alvo = random.choice(lista)  # Escolhe um número da lista para garantir que existe
    return comparar_algoritmos(lista, alvo, is_sorted)

# Criando o gráfico comparativo
def gerar_grafico(titulo, valores_n, tempos_busca_sequencial, tempos_busca_binaria):    
    plt.figure(figsize=(10, 5))
    plt.plot(valores_n, tempos_busca_sequencial, label='Busca Sequencial', marker='o')
    plt.plot(valores_n, tempos_busca_binaria, label='Busca Binária', marker='o')
    plt.xlabel('Tamanho da Entrada (n)')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.title(titulo)
    plt.legend()
    plt.grid()
    plt.show()


# Criando comparativo em lista nao ordenada
def gerar_testes_lista_nao_ordenada():
    valores_n = [10, 100, 500, 1000, 2000, 4000, 6000, 10000]
    tempos_busca_sequencial = []
    tempos_busca_binaria = []
    print("\n")
    print("="*50) 
    print("Busca em lista Não Ordenada")
    for n in valores_n:
        tempo_busca_sequencial, tempo_busca_binaria = gerar_teste(n)
        tempos_busca_sequencial.append(tempo_busca_sequencial)
        tempos_busca_binaria.append(tempo_busca_binaria)
    print("-"*30)

    gerar_grafico("Comparação de tipos de Busca em lista Não Ordenada", valores_n, tempos_busca_sequencial , tempos_busca_binaria)

def gerar_testes_lista_ordenada():
    valores_n = [10, 100, 500, 1000, 2000, 4000, 6000, 10000]
    tempos_busca_sequencial = []
    tempos_busca_binaria = []
    print("\n")
    print("="*50) 
    print("Busca em lista Ordenada")
    for n in valores_n:
        tempo_busca_sequencial, tempo_busca_binaria = gerar_teste(n, is_sorted=True)
        tempos_busca_sequencial.append(tempo_busca_sequencial)
        tempos_busca_binaria.append(tempo_busca_binaria)
    print("-"*30)

    gerar_grafico("Comparação de tipos de Busca em lista Ordenada", valores_n, tempos_busca_sequencial , tempos_busca_binaria)


gerar_testes_lista_nao_ordenada()
gerar_testes_lista_ordenada()

