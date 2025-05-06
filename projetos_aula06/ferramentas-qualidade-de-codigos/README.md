# 🧼 Aula 06 – Qualidade de Código com Ferramentas Python | Jornada de Dados

Este repositório faz parte da **Jornada de Dados** e registra o conteúdo aprendido na **aula 06**, cujo foco foi entender a importância da **qualidade de código** e como ferramentas do ecossistema Python podem nos ajudar com **padronização, segurança e legibilidade** do código.

---

## 🎯 Objetivo

Conhecer, instalar e aplicar ferramentas que analisam, corrigem e previnem más práticas em projetos Python. As ferramentas estudadas foram:

- [**Black**](https://black.readthedocs.io/en/stable/)
- [**Blue**](https://blue.readthedocs.io/en/latest/)
- [**isort**](https://pycqa.github.io/isort/)
- [**Flake8**](https://flake8.pycqa.org/en/latest/)
- [**Bandit**](https://bandit.readthedocs.io/en/latest/)

---

## 📦 Ferramentas utilizadas

### 🖤 Black
Formata automaticamente o código Python com um estilo padronizado e opinativo.

```bash
pip install black
black nome_do_arquivo.py
```

📘 [Documentação oficial](https://black.readthedocs.io/en/stable/)

---

### 💙 Blue
Alternativa ao Black com menos rigidez em certas decisões de formatação.

```bash
pip install blue
blue nome_do_arquivo.py
```

📘 [Documentação oficial](https://blue.readthedocs.io/en/latest/)

---

### 📚 isort
Organiza automaticamente os blocos de importação no início dos arquivos.

```bash
pip install isort
isort nome_do_arquivo.py
```

📘 [Documentação oficial](https://pycqa.github.io/isort/)

---

### 🧯 Flake8
Linter que verifica problemas de sintaxe, estilo e boas práticas.

```bash
pip install flake8
flake8 nome_do_arquivo.py
```

📘 [Documentação oficial](https://flake8.pycqa.org/en/latest/)

---

### 🛡️ Bandit
Analisa o código em busca de vulnerabilidades de segurança.

```bash
pip install bandit
bandit -r nome_do_diretorio/
```

📘 [Documentação oficial](https://bandit.readthedocs.io/en/latest/)

---

## ⚙️ Como configurar tudo automaticamente com o Pre-commit

### 🛠️ Instalação

```bash
pip install pre-commit
```

---

### 📄 Crie o arquivo `.pre-commit-config.yaml`

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black

  - repo: https://github.com/pre-commit/mirrors-isort
    rev: v5.12.0
    hooks:
      - id: isort

  - repo: https://gitlab.com/pycqa/flake8
    rev: 6.1.0
    hooks:
      - id: flake8

  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.5
    hooks:
      - id: bandit
        args: ["-r", "."]
```

---

### ✅ Ativando o `pre-commit`

```bash
pre-commit install
```

Para rodar manualmente:

```bash
pre-commit run --all-files
```

---

## 🚨 Possíveis conflitos entre as ferramentas e como resolver

### 1. **Black vs isort**
**Conflito**: o `black` tem uma ordem de imports diferente do padrão default do `isort`.

**Solução**:
Configure o `isort` para seguir o estilo do `black`.

Crie um arquivo `pyproject.toml` com:

```toml
[tool.isort]
profile = "black"
```

---

### 2. **Black vs Flake8**
**Conflito**: o `black` pode formatar linhas com mais de 88 caracteres, mas o `flake8` por padrão só aceita até 79.

**Solução**:
Configure o `flake8` para aceitar até 88 caracteres, o padrão do Black:

Crie ou edite o arquivo `.flake8` com:

```ini
[flake8]
max-line-length = 88
```

---

### 3. **Bandit vs regras de estilo**
**Conflito**: o `bandit` acusa práticas de segurança (ex: uso de `eval`) que podem passar despercebidas pelas outras ferramentas.

**Solução**:
- Nunca ignore alertas de segurança.
- Use comentários como `# nosec` com muita cautela se tiver certeza de que não é um risco.

---

## 🧪 Tutorial: ordem correta de execução em um projeto real

1. **Organize imports com isort**  
   `isort .`

2. **Formate código com Black (ou Blue)**  
   `black .`

3. **Verifique estilo com Flake8**  
   `flake8 .`

4. **Analise segurança com Bandit**  
   `bandit -r .`

Ou use o comando completo com `pre-commit`:

```bash
pre-commit run --all-files
```

---

## ✅ Tabela resumo das ferramentas

| Ferramenta | Função                       | Modifica código? | Tipo         |
|------------|------------------------------|------------------|--------------|
| Black      | Formata código               | Sim              | Formatador   |
| Blue       | Formata código (flexível)    | Sim              | Formatador   |
| isort      | Organiza importações         | Sim              | Organizador  |
| Flake8     | Checa estilo e boas práticas | Não              | Linter       |
| Bandit     | Detecta falhas de segurança  | Não              | Segurança    |

---

## 📎 Links úteis

- [Black](https://black.readthedocs.io/en/stable/)
- [Blue](https://blue.readthedocs.io/en/latest/)
- [isort](https://pycqa.github.io/isort/)
- [Flake8](https://flake8.pycqa.org/en/latest/)
- [Bandit](https://bandit.readthedocs.io/en/latest/)
- [Pre-commit](https://pre-commit.com)

---

> ⚠️ **Recomendação final**: Adotar essas ferramentas no início de um projeto ajuda a manter a qualidade e segurança do código desde o primeiro commit. Isso é especialmente importante em projetos colaborativos ou em produção.
