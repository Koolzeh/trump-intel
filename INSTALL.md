# TRUMP INTEL — GUIA DE INSTALAÇÃO COMPLETO
## Do zero ao app no celular em ~30 minutos

---

## ARQUIVOS QUE VOCÊ BAIXOU

```
trump-intel-completo.zip
└── trump-intel/
    ├── index.html                          ← O app inteiro (PWA)
    ├── manifest.json                       ← Configuração PWA (ícone, nome)
    ├── sw.js                               ← Service Worker (cache offline)
    ├── data/
    │   └── .gitkeep                        ← Mantém a pasta no Git
    ├── python/
    │   ├── daily_briefing.py               ← Script do briefing diário
    │   └── weekly_report.py                ← Script do relatório Excel
    └── .github/
        └── workflows/
            ├── daily_briefing.yml          ← Agenda o briefing às 7h
            └── weekly_report.yml           ← Agenda o Excel toda segunda
```

---

## PARTE 1 — CRIAR CONTA E REPOSITÓRIO NO GITHUB

### 1.1 Criar conta (pular se já tiver)

1. Acesse **github.com**
2. Clique em **Sign up**
3. Preencha: email, senha, username
4. Confirme o email

### 1.2 Criar o repositório

1. Após logar, clique no **+** (canto superior direito) → **New repository**
2. Preencha:
   - **Repository name:** `trump-intel`
   - **Visibility:** ✅ **Public** (obrigatório para GitHub Pages gratuito)
   - Deixe tudo desmarcado (sem README, sem .gitignore)
3. Clique em **Create repository**
4. **Guarde a URL** — vai ser: `https://github.com/SEU_USUARIO/trump-intel`

---

## PARTE 2 — SUBIR OS ARQUIVOS

### 2.1 Pelo navegador (sem instalar nada)

1. No repositório recém-criado, clique em **uploading an existing file**
2. Descompacte o `trump-intel-completo.zip` no seu computador
3. **Arraste** os seguintes arquivos para a área de upload do GitHub:
   - `index.html`
   - `manifest.json`
   - `sw.js`
4. No campo **Commit changes**, escreva: `primeiro deploy`
5. Clique em **Commit changes**

### 2.2 Criar as pastas manualmente

O GitHub não aceita upload de pastas vazias pela interface. Faça assim:

**Criar pasta `data/`:**
1. Clique em **Add file** → **Create new file**
2. No campo do nome, escreva: `data/.gitkeep`
3. Deixe o conteúdo vazio
4. Clique em **Commit new file**

**Criar pasta `python/`:**
1. Clique em **Add file** → **Create new file**
2. Nome: `python/daily_briefing.py`
3. Abra o arquivo `python/daily_briefing.py` do seu computador, copie todo o conteúdo e cole
4. Clique em **Commit new file**

Repita para `python/weekly_report.py`

**Criar pasta `.github/workflows/`:**
1. Clique em **Add file** → **Create new file**
2. Nome: `.github/workflows/daily_briefing.yml`
3. Abra o arquivo `.github/workflows/daily_briefing.yml` do seu computador, copie e cole
4. Clique em **Commit new file**

Repita para `.github/workflows/weekly_report.yml`

### ✅ Alternativa mais rápida: usar GitHub Desktop

1. Baixe **GitHub Desktop** em desktop.github.com
2. Faça login com sua conta GitHub
3. Clone o repositório: **File → Clone repository → trump-intel**
4. Abra a pasta clonada, copie TODOS os arquivos descompactados para dentro
5. No GitHub Desktop, escreva "primeiro deploy" e clique **Commit to main**
6. Clique **Push origin**

---

## PARTE 3 — ATIVAR O GITHUB PAGES

1. No repositório, clique em **Settings** (aba no topo)
2. No menu lateral esquerdo, clique em **Pages**
3. Em **Source**, selecione:
   - Branch: **main**
   - Folder: **/ (root)**
4. Clique em **Save**
5. Aguarde 2–3 minutos
6. Aparecerá: *"Your site is live at https://SEU_USUARIO.github.io/trump-intel/"*

**Teste:** abra essa URL no navegador. O app deve aparecer.

---

## PARTE 4 — OBTER AS API KEYS

### 4.1 Finnhub (cotações em tempo real)

1. Acesse **finnhub.io**
2. Clique em **Get free API key**
3. Cadastre com email
4. Após login, a key aparece no Dashboard — começa com `pk_`
5. **Guarde essa key**

### 4.2 Anthropic / Claude (IA)

1. Acesse **console.anthropic.com**
2. Faça login ou crie conta
3. No menu lateral, clique em **API Keys**
4. Clique em **Create Key**
5. Dê um nome: `trump-intel`
6. **Copie a key imediatamente** — ela começa com `sk-ant-` e só aparece uma vez
7. **Defina um limite de gasto:** clique em **Billing** → **Usage limits** → coloque **$2/mês** para segurança

---

## PARTE 5 — CONFIGURAR OS SECRETS DO GITHUB ACTIONS

Os scripts Python precisam das API keys para rodar. Você vai guardá-las como "secrets" (variáveis seguras) no GitHub:

1. No repositório, vá em **Settings → Secrets and variables → Actions**
2. Clique em **New repository secret**
3. Crie o primeiro secret:
   - **Name:** `ANTHROPIC_API_KEY`
   - **Secret:** cole sua key do Claude (`sk-ant-...`)
   - Clique **Add secret**
4. Crie o segundo secret:
   - **Name:** `FINNHUB_API_KEY`
   - **Secret:** cole sua key do Finnhub (`pk_...`)
   - Clique **Add secret**

---

## PARTE 6 — CONFIGURAR O APP NO CELULAR

### 6.1 Abrir o app

1. No celular, abra o Chrome
2. Acesse: `https://SEU_USUARIO.github.io/trump-intel/`
3. O app vai carregar e pedir para criar um PIN de 6 dígitos

### 6.2 Criar o PIN de segurança

1. Digite um PIN de 6 dígitos
2. Digite novamente para confirmar
3. **Guarde esse PIN** — após 5 tentativas erradas, bloqueia por 1 hora

### 6.3 Inserir as API keys no app

1. Abra a aba **CONFIG** (último item do menu)
2. Em **Finnhub API Key**, cole sua key do Finnhub
3. Em **Claude API Key**, cole sua key do Claude
4. Clique **SALVAR**
5. Volte ao Dashboard — os preços devem carregar

### 6.4 Instalar como app nativo (PWA)

**No Android (Chrome):**
1. Toque no menu **⋮** (três pontos, canto superior direito)
2. Toque em **Adicionar à tela inicial**
3. Confirme o nome "Trump Intel"
4. Um ícone aparece na sua tela inicial — igual a um app nativo

**No iPhone (Safari):**
1. Abra no Safari (não Chrome)
2. Toque no botão **Compartilhar** (ícone de caixa com seta)
3. Toque em **Adicionar à Tela de Início**
4. Confirme

---

## PARTE 7 — TESTAR O BRIEFING AUTOMÁTICO

### 7.1 Testar manualmente (sem esperar às 7h)

1. No GitHub, vá em **Actions** (aba no topo do repositório)
2. No menu lateral, clique em **Briefing Diário**
3. Clique em **Run workflow** → **Run workflow**
4. Aguarde ~30 segundos
5. Verifique se apareceu um commit novo em `data/briefing.json`

### 7.2 Verificar no app

1. Abra o app no celular
2. Vá na aba **ANÁLISE IA**
3. O briefing do dia deve estar lá com o badge **"✓ AUTO 7H"**

### 7.3 Agendamento automático

O GitHub Actions roda automaticamente:
- **Briefing:** segunda a sexta, 07:00 BRT
- **Excel:** toda segunda-feira, 09:00 BRT

---

## PARTE 8 — BAIXAR O EXCEL SEMANAL

Após o GitHub Actions gerar o relatório:

1. No repositório, clique na pasta `data/`
2. Clique em `report_latest.xlsx`
3. Clique em **Download raw file**

Ou diretamente pela URL:
```
https://raw.githubusercontent.com/SEU_USUARIO/trump-intel/main/data/report_latest.xlsx
```

---

## PARTE 9 — ALPHA VANTAGE (opcional — sparklines 5 dias)

Se quiser os mini gráficos de 5 dias na watchlist:

1. Acesse **alphavantage.co/support/#api-key**
2. Preencha o formulário (gratuito)
3. Copie a API key
4. No app, vá em **CONFIG** → campo **Alpha Vantage API Key**
5. Cole a key e clique **SALVAR**

Limite gratuito: 25 chamadas/dia — suficiente para os principais ativos.

---

## RESUMO RÁPIDO — CHECKLIST

- [ ] Conta GitHub criada
- [ ] Repositório `trump-intel` criado (Public)
- [ ] Arquivos enviados: `index.html`, `manifest.json`, `sw.js`
- [ ] Pastas criadas: `data/`, `python/`, `.github/workflows/`
- [ ] GitHub Pages ativado (branch main, root)
- [ ] App acessível em `https://SEU_USUARIO.github.io/trump-intel/`
- [ ] Finnhub key obtida
- [ ] Claude key obtida (limite $2/mês definido)
- [ ] Secrets configurados no GitHub Actions
- [ ] App aberto no celular, PIN criado
- [ ] API keys inseridas no app
- [ ] App instalado na tela inicial
- [ ] Briefing manual testado via GitHub Actions
- [ ] Excel semanal verificado

---

## CUSTO TOTAL ESTIMADO

| Item | Custo |
|------|-------|
| GitHub Pages | **$0/mês** |
| Finnhub (free tier) | **$0/mês** |
| TradingView embeds | **$0/mês** |
| Briefing diário (Claude Haiku, ~22 dias úteis) | **~$0.07/mês** |
| Análise semanal (opcional) | **~$0.04/mês** |
| **TOTAL** | **~$0.11/mês** |

---

## PROBLEMAS COMUNS

**App não carrega após ativar Pages:**
→ Aguarde até 5 minutos. Às vezes demora para propagar.

**Preços não aparecem:**
→ Verifique se a Finnhub key está correta em CONFIG. Keys gratuitas têm limite de 60 calls/min.

**GitHub Actions falha:**
→ Vá em Actions → clique no workflow com ❌ → leia o erro. Geralmente é key errada ou digitada com espaço.

**PIN bloqueado:**
→ Aguarde 1 hora ou limpe o localStorage: no Chrome, DevTools → Application → Local Storage → limpar.

**Briefing não aparece no app:**
→ Verifique se o commit do `data/briefing.json` foi feito. O arquivo precisa existir no repositório.
