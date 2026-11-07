
# Fundamentos de Segurança de Aplicações

## 1. Segurança de aplicações (AppSec)

AppSec é a prática de identificar, prevenir e corrigir vulnerabilidades durante o desenvolvimento e a operação de aplicações.

O objetivo é reduzir riscos e proteger dados, sistemas e usuários.

## 2. Princípios fundamentais

### Confidencialidade
Garantir que informações sejam acessadas somente por pessoas ou sistemas autorizados.

### Integridade
Garantir que informações não sejam alteradas indevidamente.

### Disponibilidade
Garantir que sistemas e informações permaneçam acessíveis quando necessário.

Esses três princípios formam a tríade CIA.

## 3. Vulnerabilidade, ameaça e risco

- **Vulnerabilidade:** fraqueza que pode ser explorada.
- **Ameaça:** circunstância ou agente capaz de causar dano.
- **Risco:** possibilidade de uma ameaça explorar uma vulnerabilidade e produzir impacto.

Uma vulnerabilidade identificada não significa automaticamente que houve exploração.

## 4. Avaliação de risco

Considere:

- Probabilidade de exploração.
- Impacto técnico e operacional.
- Exposição do componente.
- Dados e funcionalidades envolvidos.

A severidade deve ser justificada pelas evidências e pelo contexto.

## 5. SQL Injection

SQL Injection ocorre quando entradas controladas pelo usuário alteram indevidamente a estrutura de uma consulta SQL.

Uma causa comum é a concatenação direta de entradas em comandos SQL.

### Prevenção

Utilize consultas parametrizadas, evitando incorporar entradas do usuário diretamente na instrução SQL.

Exemplo com Python e SQLite:

```python
cursor.execute(
    "SELECT * FROM users WHERE username = ? AND password = ?",
    (username, password)
)
```

## 6. Autorização e escopo

Antes de qualquer teste de segurança:

- Confirme a autorização.
- Identifique os ativos permitidos.
- Respeite os limites definidos.
- Evite impactos desnecessários.
- Interrompa atividades quando houver dúvida sobre o escopo.

Laboratórios próprios e ambientes de teste autorizados são preferíveis para aprendizagem.

## 7. Evidências e disciplina técnica

Toda análise deve distinguir:

- **Fatos:** observações diretamente verificadas.
- **Inferências:** conclusões sustentadas por evidências.
- **Hipóteses:** possibilidades ainda não confirmadas.

Não invente resultados nem declare vulnerabilidades sem sustentação técnica.

## 8. Classificações e referências

### CWE
Catálogo de fraquezas comuns de software. Exemplo: CWE-89, Improper Neutralization of Special Elements used in an SQL Command (SQL Injection).

### OWASP
Referência para riscos e boas práticas de segurança de aplicações.

### MITRE ATT&CK
Base de conhecimento sobre táticas e técnicas adversárias.

Utilize ATT&CK somente quando houver correspondência técnica justificável. Uma vulnerabilidade não representa automaticamente uma técnica ATT&CK.

## 9. Correção e validação

Uma análise completa deve:

1. Identificar a causa raiz.
2. Recomendar uma correção.
3. Implementar a mitigação.
4. Repetir os testes relevantes.
5. Verificar se a funcionalidade legítima continua funcionando.
6. Registrar as evidências e limitações.

Correção implementada e correção validada são estados diferentes.
