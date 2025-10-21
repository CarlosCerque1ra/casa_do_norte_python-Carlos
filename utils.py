# Importa o módulo do tkinter para recursos extras de interface.
import tkinter as tk  

# Importa o método para abrir conexões com o banco de dados.
from db import getconnection  

def gerarcodigo():
    # Usa o banco de dados para determinar o ultimo id cadastrado
    with getconnection() as conn:
        # Busca o id mais alto da tabela de comidas
        cur =  conn.execute("SELECT if from comidas ORDER BY id DESC LIMIT 1")
        row = cur.fetchone()
        # Se nao huver cadastros, retorna o primeiro codigo padrão
        if not row:
            return "C001"
        # Gera o proximo codigo baseado no maior id atual
        # f"c{numero:03d}" formata o numero com 3 digitos, preenchendo com zeros a esquerda
        return f"C{int(row[0][1:]) + 1:03d}"

def mergesortproducts(products, key="nome"):
    """
    Ordena lista de comidas por atributo escolhido.
    Utiliza o algoritmo mergesort para garantir ordenação estável, eficiente e insensível a maiúsculas/minúsculas.
    """
    if len(products) <= 1:
        # Lista de tamanho <=1 já está ordenada
        return products

    mid = len(products) // 2
    left = mergesortproducts(products[:mid], key)
    right = mergesortproducts(products[mid:], key)

    merged = []
    i = j = 0
    # Faz a mesclagem dos blocos ordenados
    while i < len(left) and j < len(right):
        # Compara os valores do atributo selecionado (ignorando maiúscula/minúscula)
        if str(left[i][key]).lower() < str(right[j][key]).lower():
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Junta o que restou de cada metade (se sobrar)
    merged.extend(left[i:])
    merged.extend(right[j:])
    # Retorna lista ordenada
    return merged

def centralizarjanela(win, largura=800, altura=600):
    """Centraliza uma janela Tkinter na tela."""
    win.update_idletasks()  # Atualiza geometria da janela para garantir cálculo correto
    screenw = win.winfo_screenwidth()  # Largura da tela do computador
    screenh = win.winfo_screenheight()  # Altura da tela do computador
    # Calcula posição superior esquerda para centralizar
    x = screenw // 2 - largura // 2
    y = screenh // 2 - altura // 2
    win.geometry(f"{largura}x{altura}+{x}+{y}")  # Define posição e tamanho da janela
