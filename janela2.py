# importar s  controles (QtWidgets) para a biblioteca grafifica
# PyQt5. neste exemplo estamos ultilizando o comando import
# com a opção de asteristico(*) qiue importa os controles 
# da biblioteca
from PYytQt5.Qtwidgets import *
#  imoportação da bibloteca  de sistema para abir e fechar a
# janela que será construida. Ao fechar a janela, tambem
# estaemos retirando -a da memoria 
import sys
# criação da estrutura geral da nossa janela
# a janla e sus controles estão sendo criadas de forma agrupada dentro de uma classe.
# a classe janela está herdando todas as 
# configurações esteruturais de uma tela normal
# classe widget. esta classe define os botões:
# miniminiza, maximiza e fechar. além de apresentar
# um título para a janela 

class janela2(QWidget):
    
    def __init__(self):
         super().__init__()
    #adicionar um texto ao titulo da janela
    self.setWindowTiltle("janela de casdastro")
    #configurar o tamaho e posição
    self.setGeometry(50,200,500,200)

    #adicionar uma label a janela
    self.label_nome = Qlabel("nome completo: ")

    #adicionar uma caixa de texto
    self.edit_nome = QlineEdit()

    #adicionar layout para organizar os elementos
    Layout = QVboxLayout()

    layout.addwigdet(self.label_nome)
    layout.addWigdet(self.edit_nome)

    #adicionar o layout a tela
    self.setLayout(Layout)

app = QApplication(sys.argv)
jan = janela2()
jan.show()
app.exec_()
