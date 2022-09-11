import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def lerImg():
    fileName = "imagens\lena_gray.bmp"
    # ler como imagem
    imgTest = Image.open(fileName)
    plt.imshow(imgTest, cmap='gray')
    print('mostrar img')
    plt.show()
    # ler como matriz
    matrizOriginal = plt.imread(fileName)

    return matrizOriginal


def mascaraHorizontal(x, y, matrizOriginal):
    soma = 0
    for AuxX in range(0, 3):
        for AuxY in range(0, 3):
            posX = x - 1 + AuxX
            posY = y - 1 + AuxY
            if posX >= 0 and posX <= 255 and posY >= 0 and posY <= 255:
                if AuxX == 0:
                    if AuxY == 1:
                        soma += matrizOriginal[posX][posY] * -2
                    else:
                        soma += matrizOriginal[posX][posY] * -1
                if AuxX == 1:
                    soma += matrizOriginal[posX][posY] * 0
                if AuxX == 2:
                    if AuxY == 1:
                        soma += matrizOriginal[posX][posY] * 2
                    else:
                        soma += matrizOriginal[posX][posY]

    soma = soma / 9
    return soma


def mascaraVertical(x, y, matrizOriginal):
    soma = 0
    for AuxY in range(0, 3):
        for AuxX in range(0, 3):
            posX = x - 1 + AuxX
            posY = y - 1 + AuxY
            if posX >= 0 and posX <= 255 and posY >= 0 and posY <= 255:
                if AuxX == 0:
                    if AuxY == 1:
                        soma += matrizOriginal[posX][posY] * -2
                    else:
                        soma += matrizOriginal[posX][posY] * -1
                if AuxX == 1:
                    soma += matrizOriginal[posX][posY] * 0
                if AuxX == 2:
                    if AuxY == 1:
                        soma += matrizOriginal[posX][posY] * 2
                    else:
                        soma += matrizOriginal[posX][posY]

    soma = soma / 9
    return soma


def modulo(v):
    if v < 0:
        v = -v
    return v


def main():
    matrizOriginal = lerImg()
    sobel = matrizOriginal.copy()

    for xMed in range(0, len(sobel)):
        for yMed in range(0, len(sobel[xMed])):
            h = modulo(mascaraHorizontal(xMed, yMed, matrizOriginal))
            v = modulo(mascaraVertical(xMed, yMed, matrizOriginal))

            sobel[xMed][yMed] = h + v
    plt.imshow(sobel, cmap='gray')
    plt.show()


main()
