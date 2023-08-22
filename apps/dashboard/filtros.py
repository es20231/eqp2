from abc import ABC, abstractmethod
import cv2

class Filtro(ABC):
    @abstractmethod
    def aplicar_filtro(self, imagem):
        pass

class FiltroBlur(Filtro):   
    def aplicar_filtro(self, imagem):
        imagem = cv2.GaussianBlur(imagem,(15,15),0)
        return imagem

class FiltroGrayScale(Filtro):
    def aplicar_filtro(self, imagem):
        imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
        return imagem
    
class FiltroClahe(Filtro):
    def aplicar_filtro(self, imagem):
        imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2Lab)
        clahe = cv2.createCLAHE(clipLimit=5,tileGridSize=(8,8))
        imagem[:,:,0] = clahe.apply(imagem[:,:,0])
        imagem = cv2.cvtColor(imagem, cv2.COLOR_Lab2RGB)
        return imagem
