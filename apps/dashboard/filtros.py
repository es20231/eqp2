from abc import ABC, abstractmethod
import cv2

class Filtro(ABC):
    @abstractmethod
    def aplicar_filtro(self, imagem):
        pass

class FiltroBlur(Filtro):   
    def aplicar_filtro(self, imagem):
        imagem = cv2.GaussianBlur(imagem,(5,5),0)
        return imagem

class FiltroGrayScale(Filtro):
    def aplicar_filtro(self, imagem):
        imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
        return imagem