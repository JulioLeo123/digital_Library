# 📚 Matriz de Rastreabilidade - Sistema Biblioteca Digital

> **Objetivo:** Garantir que todos os requisitos funcionais estejam cobertos por casos de teste, facilitando a rastreabilidade entre requisitos, testes e status de implementação.

---

## 🗂️ Tabela de Rastreabilidade

| Requisito | Descrição Resumida                | Casos de Teste                | Cobertura | Status      |
|-----------|-----------------------------------|-------------------------------|-----------|-------------|
| RF01      | Cadastro de Usuários              | CT001, CT002, CT015, CT016    | 100%      | ✅ Completo |
| RF02      | Autenticação de Usuários          | CT003, CT017, CT018, CT019    | 100%      | ✅ Completo |
| RF03      | Catálogo de Livros                | CT020, CT021, CT022, CT023    | 100%      | ✅ Completo |
| RF04      | Empréstimo de Livros              | CT004, CT024, CT025, CT026    | 100%      | ✅ Completo |
| RF05      | Devolução de Livros               | CT027, CT028, CT029, CT030    | 100%      | ✅ Completo |

---

## 📝 Legenda dos Campos
- **Requisito:** Código do requisito funcional.
- **Descrição Resumida:** Breve explicação do requisito.
- **Casos de Teste:** IDs dos testes que cobrem o requisito.
- **Cobertura:** Percentual de cobertura do requisito por testes.
- **Status:** Situação atual da cobertura (Completo, Parcial, Pendente).

---

## 🔍 Exemplos Detalhados de Casos de Teste

### CT001 - Cadastro de Usuário Válido
- **Requisito:** RF01
- **Tipo:** Positivo
- **Prioridade:** Alta
- **Dados de Entrada:**
	- Nome: João Silva Santos
	- Email: joao.silva@email.com
	- Senha: MinhaSenh@123
	- Tipo: Estudante
- **Resultado Esperado:**
	- Usuário cadastrado com sucesso
	- Redirecionamento para login
	- Email de confirmação enviado
	- Dados persistidos corretamente

### CT002 - Cadastro com Email Duplicado
- **Requisito:** RF01
- **Tipo:** Negativo
- **Prioridade:** Alta
- **Dados de Entrada:**
	- Nome: Maria Oliveira
	- Email: teste@email.com (já existente)
	- Senha: OutraSenh@456
	- Tipo: Professor
- **Resultado Esperado:**
	- Mensagem de erro clara: "Email já cadastrado no sistema"
	- Cadastro não realizado
	- Campo email destacado

### CT003 - Login com Bloqueio por Tentativas
- **Requisito:** RF02
- **Tipo:** Negativo
- **Prioridade:** Crítica
- **Dados de Entrada:**
	- Email: joao.silva@email.com
	- Senhas incorretas: senha123, wrong456, invalid789
- **Resultado Esperado:**
	- Conta bloqueada após 3 tentativas
	- Mensagem de bloqueio exibida
	- Timestamp do bloqueio registrado

### CT004 - Empréstimo Bem-sucedido
- **Requisito:** RF04
- **Tipo:** Positivo
- **Prioridade:** Alta
- **Dados de Entrada:**
	- Usuário: João Silva
	- Livro: Clean Code (ISBN: 978-0132350884)
	- Data: 2025-01-28
- **Resultado Esperado:**
	- Empréstimo realizado com sucesso
	- Data de devolução correta
	- Status do livro alterado
	- Registro no histórico do usuário

---

## ✅ Critérios de Aceitação dos Testes
- 100% dos requisitos funcionais cobertos por pelo menos um caso de teste
- 80% de cobertura de código nos módulos críticos
- Todos os fluxos principais e pelo menos 2 alternativos por funcionalidade
- Testes de validação de campos (boundary testing)
- Performance: resposta < 2 segundos para 95% das operações
- Zero defeitos críticos em aberto
- Aprovação dos stakeholders de negócio

---

## 📎 Referências
- [Requisitos do Sistema](../README.md)
- [Casos de Teste](../tests/)
