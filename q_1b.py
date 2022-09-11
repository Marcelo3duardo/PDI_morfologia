import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def lerImg():
    fileName = "imagens\lena_gray.bmp"
    #ler como imagem
    imgTest = Image.open(fileName)
    plt.imshow(imgTest,cmap='gray')
    print('mostrar img')
    #plt.show()
    #ler como matriz
    matrizOriginal = plt.imread(fileName)
    
    return matrizOriginal
    
    
    

#       
def AplicandoSuavizacao(x,y,matrizOriginal):
    soma = 0
    
    for a in range(0,3):
        for b in range(0,3):
            auxX = x-1 + a
            auxY = y-1 + b
            if auxX >= 0 and auxX < len(matrizOriginal) and auxY >= 0 and auxY < len(matrizOriginal[0]):
                soma += matrizOriginal[auxX][auxY]

    soma = soma/9
    return soma
 
 
        
def main():
    matrizOriginal =  lerImg()
    
    print('inicio nitidez')
    matrizMedia = matrizOriginal.copy()
    for xMed in range(0,len(matrizMedia)):
        for yMed in range(0,len(matrizMedia[xMed])):
            matrizMedia[xMed][yMed] = AplicandoSuavizacao(xMed,yMed,matrizOriginal)
    
    plt.imshow(matrizMedia,cmap='gray')
    #plt.show()    
    #   suavização aplicada
    #   fazendo a diferença
    matrizR = matrizOriginal.copy()
    for xMed in range(0,len(matrizMedia)):
        for yMed in range(0,len(matrizMedia[xMed])):
            aux = matrizOriginal[xMed][yMed] - matrizMedia[xMed][yMed]
            if aux < 0:
                aux = 0
            if aux >255:
                aux = 255  
            matrizR[xMed][yMed] =  aux
    
    matrizNitida = matrizOriginal.copy()
    
    k = 2 #define o valor de k 
            
        #k = 1 -> unsharp masking
        #K > 1 -> highboost filtering (filtragem alto-reforço)
        #K < 1 -> atenua a contribuição da máscara de  
                        
    for xMed in range(0,len(matrizNitida)):
        for yMed in range(0,len(matrizNitida[xMed])):
            aux = matrizOriginal[xMed][yMed] + int(k * matrizR[xMed][yMed])
            '''if aux < 0:
                aux = 0
            if aux > 255:
                aux = 255'''  
            matrizNitida[xMed][yMed] =  aux
    #   Somando a original com a mascara 
    plt.imshow(matrizNitida,cmap='gray')
    plt.show()
    print('aaaaa')
    
main()