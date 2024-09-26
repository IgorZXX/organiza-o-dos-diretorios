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
    # o comando def(definition->definição) define uma fnção
    # neste caso estamos definindo a função de inicialização
    
    def __init__(self):
         super().__init__()
    #adicionar um texto ao titulo da janela
    self.setWindowTiltle("janela de casdastro")
    
    #configurar o tamaho e posição
    # o pirmeiro valor é a posçao x medida em pixel
    # o segundo valor é a posição em y medidaa em pixel
    # o terceiro valor é a largura (width) medida em pixel
    # o quarto valor é a altura(height) medida em pixel
    
    self.setGeometry(50,200,500,200)
     # uma label(rótulo) é um texto que é apresentado
     # em uma janela para indicar o que deve ser feito
     # frente(geralmente uma caixa de texto). no exemplo abaixo
     # estamos criando uma label para apresentarmos o texto
     # nome completo, indica o que o usuario deve escrever
     # o nome de uma caixa de texto a frente 
     # geralmete, uma label é usada em uma combinação de caixa
     # de texto (Qlineedit)
     # adicionar uma label a janela 
     
    self.label_nome = Qlabel("nome completo: ")

    #adicionar uma caixa de texto
    self.edit_nome = QlineEdit() 
    
    # estamos usando o gerenciador de layout vertical (QVboxLayout)
    # ele é ultilizado para organizar os controles que irão aparecer
    # na janela2. O QVBoxLayout foiu ultilizado para dipor os 
    # os controles um abaxio do outro. Para exibir um ao lado do outro
    # usamos o comando QVBoxLayout.
    #adicionar layout para organizar os elementos
    
    Layout = QVboxLayout()
    # para adicionar a label_nome e edit_nome ao
    # organizador (layout) vertical, usamos o comando
    # add(adicionar)Widget(controle). assim os controles
    # irão aparecer um embaixo do outro, pois este organizado
    # é do tipo vartical
    
    layout.addwigdet(self.label_nome)
    layout.addWigdet(self.edit_nome)

    #adicionar o layout a tela
    self.setLayout(Layout)

app = QApplication(sys.argv)
jan = janela2()
jan.show()
app.exec_()
