# Reqres API Test Suite

Suíte de testes automatizados para a API [ReqRes](https://reqres.in/), desenvolvida com **pytest** e **requests** como parte da disciplina de Qualidade de Software — INATEL.

---

## Tecnologias

- Python 3.10+
- pytest 9.0.3
- pytest-html 4.2.0
- requests 2.33.1
- python-dotenv

---

## Estrutura do Projeto
reqres-api-tests/
├── tests/
│   ├── test_valid.py       # TC-001 a TC-010 — Caminho feliz
│   └── test_invalid.py     # TC-011 a TC-020 — Dados inválidos
├── fixtures/
│   └── users.json          # Dados de teste separados do código
├── reports/                # Relatório HTML gerado após execução
├── conftest.py             # Fixtures globais (sessões, base_url, test_data)
├── pytest.ini              # Configuração do pytest
├── requirements.txt        # Dependências do projeto
└── .env                    # Variáveis de ambiente (não versionado)

---

## Configuração do Ambiente

### 1. Clone o repositório

```bash
git clone https://github.com/LlmaDev/backendAPITTestSuit.git
cd backendAPITTestSuit
```

### 2. Crie e ative o ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou no Windows:
.venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure a API Key

Crie um arquivo `.env` na raiz do projeto:

```bash
echo "REQRES_API_KEY=sua_chave_aqui" > .env
```

Obtenha sua chave gratuita em: https://app.reqres.in/api-keys

---

## Executando os Testes

### Execução completa (com relatório HTML)

```bash
pytest
```

### Execução com output detalhado

```bash
pytest -v
```

### Executar apenas um arquivo

```bash
pytest tests/test_valid.py -v
pytest tests/test_invalid.py -v
```

### Executar um teste específico

```bash
pytest tests/test_valid.py::test_TC001_list_users_page1 -v
```

O relatório HTML é gerado automaticamente em `reports/report.html`.

---

## Casos de Teste

### Caminho Feliz (TC-001 a TC-010)

| ID | Nome | Endpoint |
|----|------|----------|
| TC-001 | Listar usuários página 1 | GET /api/users?page=1 |
| TC-002 | Buscar usuário por ID | GET /api/users/2 |
| TC-003 | Listar recursos de cores | GET /api/unknown |
| TC-004 | Login com sucesso | POST /api/login |
| TC-005 | Registro com sucesso | POST /api/register |
| TC-006 | Criar produto | POST /api/collections/products/records |
| TC-007 | Listar produtos | GET /api/collections/products/records |
| TC-008 | Buscar produto por ID | GET /api/collections/products/records/:id |
| TC-009 | Atualizar produto (PATCH) | PATCH /api/collections/products/records/:id |
| TC-010 | Deletar produto | DELETE /api/collections/products/records/:id |

### Dados Inválidos (TC-011 a TC-020)

| ID | Nome | Endpoint |
|----|------|----------|
| TC-011 | Usuário inexistente | GET /api/users/9999 |
| TC-012 | Recurso inexistente | GET /api/unknown/9999 |
| TC-013 | Login sem senha | POST /api/login |
| TC-014 | Login sem email | POST /api/login |
| TC-015 | Login com email inválido | POST /api/login |
| TC-016 | Registro sem senha | POST /api/register |
| TC-017 | Criar produto sem wrapper data | POST /api/collections/products/records |
| TC-018 | Acessar collections sem API key | GET /api/collections/products/records |
| TC-019 | Buscar produto com ID inválido | GET /api/collections/products/records/:id |
| TC-020 | Deletar produto com ID inválido | DELETE /api/collections/products/records/:id |

---

## Resultado Esperado
