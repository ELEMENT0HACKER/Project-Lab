# Project-Lab
Brute Force (Kali Linux &amp; Metasploitable2)
# Laboratório de Segurança: Testes de Autenticação FTP com Medusa

## 📌 Sobre o projeto

Este projeto documenta um exercício prático de segurança cibernética realizado em um ambiente de laboratório controlado, utilizando Kali Linux e Metasploitable 2.

O objetivo foi identificar o serviço FTP, preparar listas de teste, avaliar o mecanismo de autenticação com o Medusa e analisar os riscos associados ao uso de credenciais fracas.

**Contexto:** projeto educacional desenvolvido durante os estudos de cibersegurança.

## 🎯 Objetivos

- Identificar um serviço FTP e sua versão anunciada.
- Verificar a conectividade com o alvo.
- Preparar e validar listas de usuários e senhas.
- Utilizar o Medusa para testar a autenticação FTP.
- Interpretar os resultados obtidos.
- Identificar riscos e recomendar medidas de mitigação.

## 🧪 Ambiente de laboratório

| Componente | Descrição |
|---|---|
| Máquina de testes | Kali Linux |
| Alvo | Metasploitable 2 |
| Endereço do alvo | `192.168.56.103` |
| Serviço analisado | FTP |
| Porta | TCP/21 |
| Ferramentas principais | Nmap, cliente FTP e Medusa |

Todos os testes foram realizados no ambiente de laboratório autorizado.

## 🛠️ Ferramentas utilizadas

- **Nmap 7.95:** reconhecimento de portas e identificação de serviços.
- **Cliente FTP:** observação da conexão e do processo de autenticação.
- **Medusa 2.3:** avaliação controlada de credenciais no serviço FTP.

## 🔎 1. Reconhecimento do serviço

Para identificar o serviço na porta 21, foi executado:

```bash
nmap -sV -p 21 192.168.56.103
```

**Resultado observado:**

- Porta TCP/21 aberta.
- Serviço identificado como FTP.
- Versão anunciada: `vsftpd 2.3.4`.

A identificação da versão anunciada não comprova, isoladamente, a presença de uma vulnerabilidade específica.

### Inspeção do serviço

Também foi executado:

```bash
nmap -sV -p 21 --script ftp-syst 192.168.56.103
```

A resposta do servidor indicou que as conexões de controle e de dados utilizavam texto simples.

**Risco:** a ausência de criptografia pode expor credenciais e dados transmitidos a agentes capazes de capturar o tráfego de rede.

## 🔐 2. Observação da autenticação

Foi estabelecida uma conexão FTP interativa:

```bash
ftp 192.168.56.103
```

Durante uma tentativa com o usuário `admin`, o servidor retornou:

```text
331 Please specify the password.
530 Login incorrect.
```

A resposta `530` indicou que a tentativa de autenticação foi rejeitada.

Esse resultado isolado não permite determinar se o usuário existe ou se a senha informada estava incorreta.

## 📋 3. Preparação das listas de teste

Foram preparados dois arquivos:

- `users.txt`: lista de usuários de teste.
- `password.txt`: lista de senhas de teste.

As listas foram verificadas antes da execução.

**Quantidade de entradas:**

| Arquivo | Entradas |
|---|---:|
| `users.txt` | 4 |
| `password.txt` | 7 |
| Combinações teóricas | 28 |

A quantidade de combinações representa o produto entre o número de usuários e o número de senhas. Ela não representa, por si só, autenticações bem-sucedidas.

## ⚙️ 4. Verificação do Medusa

A ferramenta identificou sua versão como 2.3.

Para verificar a disponibilidade do módulo FTP, foi executado:

```bash
medusa -d | grep -i ftp
```

A saída apresentou:

```text
ftp.mod : Brute force module for FTP/FTPS sessions : version 2.1
```

Isso confirmou que o módulo FTP estava listado entre os módulos conhecidos pela ferramenta.

## ✅ 5. Teste de autenticação

O teste foi executado contra o serviço FTP do Metasploitable 2, utilizando as listas preparadas.

**Comando executado:**

```bash
medusa -h 192.168.56.103 -U users.txt -P password.txt -M ftp
```

### Resultado observado

O Medusa apresentou a seguinte mensagem:

```text
ACCOUNT FOUND: [ftp] Host: 192.168.56.103 User: msfadmin Password: msfadmin [SUCCESS]
```

**Resultado:** a ferramenta reportou a combinação `msfadmin` / `msfadmin` como uma autenticação bem-sucedida no serviço FTP do laboratório.

## 📊 6. Análise do resultado

A combinação encontrada utiliza o mesmo valor como nome de usuário e senha, tornando-a simples e previsível.

O resultado demonstra que, no ambiente testado, uma credencial fraca permitiu autenticação FTP.

Em um sistema real, credenciais previsíveis podem facilitar o acesso não autorizado, especialmente quando o serviço está acessível a agentes que não deveriam utilizá-lo.

A evidência não comprova que a mesma combinação funcione em outros sistemas nem que exista uma vulnerabilidade específica na versão anunciada do servidor.

## 🛡️ 7. Recomendações de mitigação

Com base nas observações realizadas, recomenda-se:

1. Utilizar senhas fortes, únicas e não previsíveis.
2. Evitar senhas iguais aos nomes de usuário.
3. Desabilitar contas desnecessárias e revisar permissões.
4. Preferir SFTP ou configurar FTPS adequadamente.
5. Restringir o acesso ao serviço por meio de firewall e segmentação de rede.
6. Implementar controles proporcionais contra tentativas repetidas de autenticação.
7. Monitorar os registros de acesso e as falhas de autenticação.
8. Manter o software atualizado e revisar sua configuração.

## 🧠 8. Principais aprendizados

Durante este exercício, foram praticadas as seguintes competências:

- Reconhecimento de serviços com Nmap.
- Interpretação de respostas de protocolos.
- Preparação e validação de arquivos de teste.
- Utilização do Medusa em um laboratório controlado.
- Análise de resultados de autenticação.
- Distinção entre evidência observada e conclusão técnica.
- Identificação de riscos e proposição de medidas de mitigação.

## 🏁 9. Conclusão

O laboratório permitiu investigar o serviço FTP do Metasploitable 2, preparar listas de teste e avaliar o mecanismo de autenticação.

O principal resultado foi a identificação, pelo Medusa, da combinação `msfadmin` / `msfadmin` como válida no serviço FTP do ambiente testado.

O exercício demonstrou a importância de utilizar credenciais robustas, proteger as comunicações e restringir o acesso aos serviços conforme a necessidade.

Também reforçou que uma conclusão técnica deve estar apoiada em evidências observadas e apresentar claramente as limitações do teste.

## ⚖️ Escopo e uso responsável

Este projeto tem finalidade educacional e documenta testes realizados em um laboratório controlado e autorizado.

Os resultados se aplicam ao ambiente testado e não devem ser generalizados para sistemas externos sem investigação independente e autorização explícita.

---
## Evidência visual do projeto

![Evidência visual da atividade prática](PROJECT-CLASS%28LAB%29.png)

**Projeto educacional de cibersegurança — Kali Linux, Metasploitable 2, Nmap e Medusa.**
