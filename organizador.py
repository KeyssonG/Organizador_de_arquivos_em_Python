import os 

from tkinter.filedialog import askdirectory


# Nesta linha escolhemos o diretório onde iremos trabalhar
caminho = askdirectory(title="Selecione uma pasta")

# Aqui conseguimos visualizar os arq que estão no diretório
lista_arquivos = os.listdir(caminho)
print(lista_arquivos)

# Aqui definimos quais pastas serão criadas e qual o parametro verificado
locais = {
    "imagens": [".png", ".jpg"],
    "executaveis" : [".cmd", ".zip", ".iso", ".exe", ".rar"],
    "documentos" : [".docx"]
}

# Aqui temos alguns laços, o primeiro irá verificar o nome e a extensão do arquivo 
for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais: # a variavel pasta verificar de forma sequencial cada pasta
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"): # aqui verifica se as pastas existem dentro do diretório
                os.mkdir(f"{caminho}/{pasta}") # se a pasta não existir, ela é criada 
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}") #caso a pasta seja criada na linha acima,
                                                                                #o arquivo é movido da pasta antiga para a nova    
                                                                                