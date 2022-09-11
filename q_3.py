
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def lerImg(fileName):
    #fileName = "imagens\lena_ruido.bmp"
    #ler como imagem
    imgTest = Image.open(fileName)
    plt.imshow(imgTest,cmap='gray')
    print('mostrar img')
    #plt.show()
    #ler como matriz
    matrizOriginal = plt.imread(fileName)
    
    return matrizOriginal

def uniao(img1,img2):
    #cria uma img de tamanho len(img1)
    uniao = np.zeros((len(img1),len(img1[0])))
    for Xaux in range(0,len(img1)):
        for Yaux in range(0,len(img1[Xaux])):
            #determinar limite do preto v < 125
            if img1[Xaux][Yaux] > 125:
                uniao[Xaux][Yaux] += img1[Xaux][Yaux]
            if img2[Xaux][Yaux] > 125:
                uniao[Xaux][Yaux] += img2[Xaux][Yaux]
    print('uniao --->')
    plt.imshow(uniao,cmap='gray')
    plt.show()
            
def intersecao(img1,img2):
    #cria uma img de tamanho len(img1)
    intersecao = np.zeros((len(img1),len(img1[0])))
    for Xaux in range(0,len(img1)):
        for Yaux in range(0,len(img1[Xaux])):
            #determinar limite do preto v < 125
            vImg1 = False
            vImg2 = False
            if img1[Xaux][Yaux] > 125:
                vImg1 = True    
            if img2[Xaux][Yaux] > 125:
                vImg2 = True
            if vImg2 and vImg1:       #intesecao
                intersecao[Xaux][Yaux] += img2[Xaux][Yaux] + img1[Xaux][Yaux]
    print('interseção --->')
    plt.imshow(intersecao,cmap='gray')
    plt.show()

def diferenca(img1,img2):
    #cria uma img de tamanho len(img1)
    
    diferenca = np.zeros((len(img1),len(img1[0])))
    for Xaux in range(0,len(img1)):
        for Yaux in range(0,len(img1[Xaux])):
            #determinar limite do preto v < 125
            vImg1 = False
            vImg2 = False
            if img1[Xaux][Yaux] > 125:
                vImg1 = True    
            if img2[Xaux][Yaux] > 125:
                vImg2 = True
            if vImg1 != vImg2:
                diferenca[Xaux][Yaux] = 250
    print('diferença --->')
    plt.imshow(diferenca,cmap='gray')
    plt.show()
            

def modulo(v):
    if v < 0:
        v = -v
    return v

def main():
    #nomeImg1 = input('Digite o diretório da imagem 1:')
    #nomeImg2 = input('Digite o diretório da imagem 2:')
    nomeImg1 = 'imagens\lena_gray.bmp'
    nomeImg2 = 'imagens\lena_ruido.bmp'
    matrizImg1 =  lerImg(nomeImg1)
    matrizImg2 =  lerImg(nomeImg2)
    
    uniao(matrizImg1,matrizImg2)
    intersecao(matrizImg1,matrizImg2)
    diferenca(matrizImg1,matrizImg2)
    
    
    
        
main()