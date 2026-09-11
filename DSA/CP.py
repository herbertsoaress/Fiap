def bubble_sort(lista):
    comparacoes = 0
    movimentacoes = 0
    n = len(lista)
    for i in range(n):
        for j in range(n - 1 - i):
            comparacoes += 1
            if lista[j] > lista[j + 1]:
                movimentacoes += 1
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
 
    return lista, comparacoes, movimentacoes
 
 
def analisar_carga(carga):
    menor = 100000
    maior = 0
 
    for numero in carga:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
 
    return len(carga), maior, menor
 
def busca_linear(lista, codigo):
    comparacoes = 0
    n = len(lista)
    for i in range(n):
        for j in range(n - 1 - i):
            if lista[j] == codigo or lista[j + 1] == codigo:
                comparacoes += 1
 
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
 
   
 
    return lista.index(codigo), comparacoes
 
containers_A = [
    482, 173, 905, 241, 667, 318, 754, 126, 590, 433, 812, 205, 691, 347, 978, 154, 526, 739, 284, 861,
    615, 92, 447, 830, 271, 704, 358, 999, 116, 563, 790, 225, 648, 401, 876, 139, 512, 733, 296, 944,
    187, 620, 455, 808, 332, 571, 14, 684, 253, 917, 365, 742, 198, 536, 889, 307, 651, 420, 773, 105,
    598, 246, 934, 381, 719, 160, 547, 825, 293, 672, 438, 981, 121, 504, 756, 339, 690, 214, 867, 475,
    928, 146, 583, 261, 714, 396, 845, 72, 631, 287, 960, 518, 352, 799, 183, 606, 449, 874, 235, 697,
    323, 910, 167, 552, 781, 409, 995, 128, 644, 274, 835, 491, 759, 203, 576, 341, 888, 64, 622, 457,
    936, 312, 705, 149, 539, 820, 266, 681, 427, 973, 111, 594, 748, 384, 862, 229, 517, 301, 793, 176,
    655, 470, 921, 137, 568, 245, 730, 414, 856, 98, 609, 286, 947, 361, 712, 194, 525, 804, 257, 678,
    443, 986, 119, 591, 764, 335, 841, 208, 549, 392, 913, 155, 632, 278, 725, 461, 870, 83, 603, 319,
    958, 171, 557, 240, 699, 406, 823, 132, 586, 270, 932, 375, 716, 201, 531, 788, 349, 663, 454, 902
]
 
def busca_binaria(lista, codigo):
    esquerda = 0
    direita = len(lista) - 1
    comparacoes = 0
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
 
        if lista[meio] == codigo:
            comparacoes += 1
            return meio, comparacoes
        elif lista[meio] < codigo:
            comparacoes += 1
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1
 
 
 
tamanho_da_lista, maior, menor = analisar_carga(containers_A)
lista, comparacoes, movimentacoes = bubble_sort(containers_A)
codigo_procurado = 684
posicao_linear, comparacao_linear = busca_linear(lista, codigo_procurado)
posicao_binaria, comapracao_binaria = busca_binaria(lista, codigo_procurado)
 
print("========== CENTRAL DE TRIAGEM ==========")
print(f'Quantidade de contêineres: {tamanho_da_lista}')
print(f'Menor código: {menor}')
print(f"Maior código: {maior}")
print('---------- ORDENAÇÃO ----------')
print('Algoritmo: Bubble sort')
print(f'Comparações: {comparacoes}')
print(f"Movimentações: {movimentacoes} ")
print("---------- BUSCAS ----------")
print(f'Código procurado: {codigo_procurado}')
print(f'Busca Linear - Posição: {posicao_linear} | Comparações: {comparacao_linear}  ')
print(f'Busca Binária - Posição: {posicao_binaria} | Comparações: {comapracao_binaria}')
print("========================================")
 