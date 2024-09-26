import os
# para criar uma função em python iremos ulrilizar o comando
# def(definição)
def MudarNome(ar_or,nv_ar):
    """    

    a função mudarNome, altera o nome de um arquivo que o usuario deve passar o nome original do arquivo e o novo nome.
    args:
        ar_or (str): o nome original do arquivo 
        nv_ar (str): o novo nome do arquivo   
        returns:
            retorna uma mensagem fr confirmação    
    """
    os.rename(ar_or,nv_ar)
    msg = "o nome da parada foi alterada com successo"
    return msg

arquivo_original = input("Digite o nome do arquivo que sera alterado: ")
novo_arquivo = input ("Digite o nome do novo arquivo: ")

rs = MudarNome(arquivo_original, novo_arquivo)
print(rs)
