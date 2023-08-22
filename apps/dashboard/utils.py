import os
import cv2

def especificar_filtro_no_nome_da_imagem(nome_da_imagem, tipo_de_filtro):
    nome_do_arquivo, extensao = nome_da_imagem.split(".")
    nome_do_arquivo += "(" + tipo_de_filtro + ")"
    return nome_do_arquivo + "." + extensao

def copiar_imagem_se_copia_nao_existir(caminho_da_copia, caminho_da_original):
    imagem_original = cv2.imread(caminho_da_copia, cv2.IMREAD_COLOR)

    if not os.path.isfile(caminho_da_copia):
        print(f"caminho da copia:{caminho_da_copia}. Não foi criada ainda")
        #cv2.imwrite(caminho_da_copia, imagem_original)

def tratar_caminho_da_imagem_para_filtragem(nome_da_imagem):
    '''Necessário para acessar o caminho da imagem'''
    return "." + nome_da_imagem # Ex: \static\media\galeria -> .\static\media\galeria