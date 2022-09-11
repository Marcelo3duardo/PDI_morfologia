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
    
    
    
centro = 8     #valor da mascara laplaciana
lateral = -1
    
def AplicaLaplaciano(x,y,matrizOriginal):
    soma = 0
    #if x < len(matrizOriginal) & y < len(matrizOriginal) :
    
    
    for a in range(0,3):
        for b in range(0,3):
            if a == 1 and b == 1:
                soma += matrizOriginal[x-1 + a][y-1 + b]*(centro)
                #meio
            else:
                auxX = x-1 + a
                auxY = y-1 + b
                if auxX >= 0 and auxX < len(matrizOriginal) and auxY >= 0 and auxY < len(matrizOriginal[0]):
                    soma += matrizOriginal[x-1 + a][y-1 + b]*(lateral)
                    
    soma = soma/9   
    if soma < 0:
        soma = 0     
    return soma    #laplaciano[x][y] = soma /9


#       

        
def main():
    matrizOriginal =  lerImg()
    print('Inicio Laplaciano')
    laplaciano = matrizOriginal.copy()
    
    for xLap in range(0,len(laplaciano)):
        for yLap in range(0,len(laplaciano[xLap])):
            laplaciano[xLap][yLap] = AplicaLaplaciano(xLap,yLap,matrizOriginal)
    plt.imshow(laplaciano,cmap='gray')
    #plt.show()
    
    #somando laplaciano 
    c = centro/8
    for xLap in range(0,len(laplaciano)):
        for yLap in range(0,len(laplaciano[xLap])):
            matrizOriginal[xLap][yLap] = matrizOriginal[xLap][yLap] + (c)*laplaciano[xLap][yLap]
    plt.imshow(matrizOriginal,cmap='gray')
    plt.show()
    print('fin laplaciano')
    
    
    
main()