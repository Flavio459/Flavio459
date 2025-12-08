# EXECUTION GUIDE - GitHub Repository Labels Automation

## 🎯 OBJETIVO
Automatizar a criação e aplicação de labels em todos os seus 29 repositórios GitHub para melhor organização e discoverabilidade.

---

## 📋 PRÉ-REQUISITOS

### 1. **Python 3.8 ou superior**
```bash
python --version
```

### 2. **Git instalado**
```bash
git --version
```

### 3. **Acesso ao repositório local**
Você deve ter uma cópia local do repositório Flavio459 clonado.

---

## 🔐 PASSO 1: Criar Token de Acesso Pessoal (PAT)

### No GitHub (online):

1. **Acesse:** https://github.com/settings/tokens/new
2. **Nome do Token:** `GitHub-Labels-Automation`
3. **Expiração:** 30 dias (recomendado para segurança)
4. **Escopos necessários:** Marque apenas `repo` (acesso completo a repositórios privados/públicos)
5. **Gere o token** e **COPIE IMEDIATAMENTE** (não será mostrado novamente)

⚠️ **SEGURANÇA:** Nunca compartilhe este token. Tratá-lo como uma senha.

---

## 💻 PASSO 2: Configurar Variáveis de Ambiente

### No Windows (CMD):
```bash
setx GITHUB_TOKEN "seu_token_aqui"
setx PYTHONPATH %CD%
```

### No Windows (PowerShell):
```powershell
$env:GITHUB_TOKEN = "seu_token_aqui"
```

### No macOS/Linux:
```bash
export GITHUB_TOKEN="seu_token_aqui"
```

💡 **Dica:** Para fazer permanente, adicione ao seu `~/.bashrc` ou `~/.zshrc`

---

## 🚀 PASSO 3: Preparar o Ambiente

### 1. **Clonar ou atualizar o repositório:**
```bash
git clone https://github.com/Flavio459/Flavio459.git
cd Flavio459
```

### 2. **Criar ambiente virtual (recomendado):**

#### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. **Instalar dependências:**
```bash
pip install PyGithub python-dotenv
```

Verificar instalação:
```bash
pip list | grep -i github
```

---

## ⚡ PASSO 4: Executar o Script

### Comando (a partir do diretório raiz do repositório):
```bash
python scripts/setup_labels.py
```

### Saída esperada:
```
============================================================
GitHub Repository Labels Automation
============================================================

✓ Connected as: Flavio459

Processing: Alma-Ego
  Setting up labels in Alma-Ego...
  ✓ Created label: active
  ✓ Created label: ai-powered
  ...
  ✓ Added 5 labels as topics

Processing: PH-ICE-PMOC-Assistente
  ...

============================================================
SUMMARY
============================================================
Repositories processed: 29
Labels created: 156
Labels assigned: 87
Errors: 0
============================================================

✅ All repositories labeled successfully!
```

---

## 📊 O QUE O SCRIPT FAZ

### Cria os seguintes tipos de labels:

#### **Status Labels** (estado do projeto)
- `active` - Desenvolvimento ativo
- `paused` - Desenvolvimento pausado
- `maintenance-only` - Apenas correções de bugs
- `archived` - Projetos legado
- `deprecated` - Não mais utilizado

#### **Feature Labels** (características)
- `ai-powered` - Usa AI/LLM
- `app-core` - Aplicação principal
- `integration` - Integrações de terceiros
- `experimental` - POCs e testes
- `documentation` - Docs e especificações

#### **Type Labels** (linguagem/tipo)
- `typescript` - TypeScript/JavaScript
- `python` - Python
- `fullstack` - Frontend + Backend
- `frontend` - Interface focada
- `open-source` - Contribuições públicas

#### **Audience Labels** (público-alvo)
- `commercial` - Negócio/Wii Group
- `personal-project` - Uso pessoal

### Mapeamento de repositórios:

O script aplica labels específicos para cada repositório baseado em `REPO_LABELS_MAP` no arquivo `scripts/setup_labels.py`.

**Exemplos:**
- **Alma-Ego:** `ai-powered`, `app-core`, `typescript`, `active`, `commercial`
- **PH-ICE-PMOC-Assistente:** `app-core`, `typescript`, `commercial`, `active`
- **archived-project:** `archived`, `maintenance-only`

---

## 🔍 VERIFICAR RESULTADOS

### Após a execução:

1. **Ir para um repositório qualquer:**
   ```
   https://github.com/Flavio459/Alma-Ego
   ```

2. **Clicar na aba "Issues"**

3. **Clicar em "Labels"**

4. **Verificar se os labels aparecem** (ex: "active", "ai-powered", etc.)

5. **Ver labels como "Topics" na página principal do repositório**

---

## 🐛 SOLUÇÃO DE PROBLEMAS

### Erro: `ModuleNotFoundError: No module named 'github'`
```bash
# Solução:
pip install PyGithub --upgrade
```

### Erro: `GITHUB_TOKEN environment variable not set`
```bash
# Verifique se a variável foi definida:
echo $GITHUB_TOKEN  # macOS/Linux
echo %GITHUB_TOKEN%  # Windows CMD

# Se vazio, defina novamente e reinicie o terminal
```

### Erro: `Bad credentials` ou `401 Unauthorized`
```bash
# Token inválido ou expirado
# Gere um novo token em: https://github.com/settings/tokens/new
# Certifique-se de que tem escopo 'repo'
```

### Erro: `Repository not found`
```bash
# Verifique:
# 1. O nome do repositório está correto
# 2. Você tem acesso (repositório não foi deletado)
# 3. Não há espaços extras no REPO_LABELS_MAP
```

### Script cria labels mas não os aplica aos repositórios
```bash
# Logs mostram erro ao "Assigning labels"
# Isso é normal - os labels como "Topics" têm limite de 30
# Os labels de Issue ainda foram criados com sucesso
```

---

## ⏱️ TEMPO ESTIMADO

- **Preparação:** 5 minutos
- **Execução do script:** 2-5 minutos (29 repositórios)
- **Verificação:** 2 minutos

**Total:** ~10-15 minutos

---

## ✅ CHECKLIST DE EXECUÇÃO

- [ ] Token PAT criado e copiado
- [ ] Variável de ambiente GITHUB_TOKEN definida
- [ ] Repositório clonado localmente
- [ ] Ambiente virtual criado e ativado
- [ ] Dependências instaladas (PyGithub)
- [ ] Script executado sem erros
- [ ] Labels verificados em um repositório
- [ ] Relatório de execução salvo

---

## 📝 REGISTRAR EXECUÇÃO

Ao executar com sucesso, documente:

```markdown
## Execução Realizada

- **Data:** [DATA]
- **Hora:** [HORA]
- **Repositórios processados:** [NÚMERO]
- **Labels criados:** [NÚMERO]
- **Erros:** [NÚMERO]
- **Duração:** [TEMPO]
- **Notas:** [OBSERVAÇÕES]
```

---

## 🔄 PRÓXIMOS PASSOS

Após a execução com sucesso:

1. **Revisar labels em alguns repositórios** para validar aplicação
2. **Personalizar REPO_LABELS_MAP** se necessário
3. **Criar GitHub Actions** para aplicar labels automaticamente em novos repositórios
4. **Documentar política de labeling** para futuros repositórios
5. **Usar labels em Issues** para melhor triagem e organização

---

## 📞 SUPORTE

Se encontrar problemas:

1. Verifique a documentação de PyGithub: https://pygithub.readthedocs.io/
2. Consulte GitHub API docs: https://docs.github.com/en/rest
3. Revise logs de erro completos no console
4. Teste com um único repositório primeiro

---

**Versão:** 1.0
**Atualizado:** 2024
**Status:** Pronto para Execução ✅
