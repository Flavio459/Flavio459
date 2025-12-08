# ⚡ QUICK START - Execução do Script de Labels

## Em 4 Passos

### 1️⃣ Criar Token PAT

```
🔗 Vá para: https://github.com/settings/tokens/new

1. Nome: GitHub-Labels-Automation
2. Escopo: Marque apenas 'repo'
3. Clique em 'Generate token'
4. COPIE o token (não será mostrado novamente!)
```

### 2️⃣ Configurar Ambiente

#### Windows (CMD):
```batch
setx GITHUB_TOKEN "seu_token_aqui"
git clone https://github.com/Flavio459/Flavio459.git
cd Flavio459
python -m venv venv
venv\Scripts\activate
pip install PyGithub python-dotenv
```

#### macOS/Linux:
```bash
export GITHUB_TOKEN="seu_token_aqui"
git clone https://github.com/Flavio459/Flavio459.git
cd Flavio459
python3 -m venv venv
source venv/bin/activate
pip install PyGithub python-dotenv
```

### 3️⃣ Executar Script

```bash
python scripts/setup_labels.py
```

**Saída esperada:**
```
✅ Connected as: Flavio459

Processing: Alma-Ego
Processing: PH-ICE-PMOC-Assistente
...

============================================================
SUMMARY
============================================================
Repositories processed: 29
Labels created: 156
Labels assigned: 87
Errors: 0
✅ All repositories labeled successfully!
```

### 4️⃣ Verificar Resultados

```
1. Acesse: https://github.com/Flavio459/Alma-Ego
2. Clique em "Issues" → "Labels"
3. Você deve ver labels como: active, ai-powered, typescript, etc.
```

---

## 💡 Comandos Completos (Cópia e Cola)

### Windows:
```batch
REM Defina o token
setx GITHUB_TOKEN "seu_token_aqui"

REM Feche e reabra o CMD
REM Depois execute:
git clone https://github.com/Flavio459/Flavio459.git
cd Flavio459
python -m venv venv
venv\Scripts\activate
pip install PyGithub python-dotenv
python scripts/setup_labels.py
```

### macOS/Linux:
```bash
export GITHUB_TOKEN="seu_token_aqui"
git clone https://github.com/Flavio459/Flavio459.git
cd Flavio459
python3 -m venv venv
source venv/bin/activate
pip install PyGithub python-dotenv
python scripts/setup_labels.py
```

---

## 🐛 Erros Comuns

| Erro | Solução |
|------|----------|
| `ModuleNotFoundError: No module named 'github'` | `pip install PyGithub --upgrade` |
| `GITHUB_TOKEN environment variable not set` | Feche e reabra o terminal após definir `setx` |
| `Bad credentials` ou `401 Unauthorized` | Token inválido. Gere um novo em https://github.com/settings/tokens/new |
| `Repository not found` | Verifique se o repositório existe e você tem acesso |

---

## ⏱️ Tempo: ~15 minutos

- Preparar ambiente: 5 min
- Executar script: 3 min
- Verificar resultados: 2 min

---

## 📞 Precisa de Ajuda?

📄 **Guia completo:** `EXECUTION_GUIDE.md`
📚 **Documentação:** https://pygithub.readthedocs.io/
🔗 **API Docs:** https://docs.github.com/en/rest

---

**Versão:** 1.0 | **Status:** 🛸 Pronto para Execução
