# Especificação Oficial do Protótipo no Figma — Performalog Atendimento & Agente de Cobrança

**Projeto:** APEX V — Tecnologia em Banco de Dados (Faculdade Unyleya)  
**Organização Parceira:** Performa Energy  
**Mídia Digital:** Protótipo Interativo no Figma (Módulos 3 e 4)  
**Base de Referência:** Código e design system do `Performalog Atendimento` (`performalog_atendimento/index.html` e `contexto/telas.html`).

---

## 1. Visão Geral e Propósito do Protótipo

O protótipo no Figma materializa a implementação do módulo **Atendimento** e do **Agente Inteligente de Cobrança** diretamente na interface corporativa do CRM **Performalog**, da Performa Energy. 

O produto resolve três problemas críticos:
1. **Unificação do Atendimento Omnichannel:** Migração da ferramenta legada (Maxbot) para a WhatsApp Cloud API oficial da Meta (Graph API v26.0), eliminando a fragmentação de canais.
2. **Automação Inteligente com Grounding em Banco de Dados:** O agente de IA opera como assistente de negociação e esclarecimento tarifário (créditos de energia solar CEMIG em kWh e faturas da Digital Grid), sem alucinações de valores.
3. **Supervisão Humana Ativa (Human-in-the-Loop):** Interface clara para que atendentes humanos assumam conversas instantaneamente e gestores aprovem exceções comerciais.

---

## 2. Design System Corporativo (Performalog)

### Paleta de Cores (Tokens de Design)
| Token | Cor Hex | Uso na Interface |
|---|---|---|
| `--plog-bar` | `#191E3A` | Barra superior corporativa do Performalog |
| `--accent` | `#1B55E2` | Cor primária, botões de ação principal, abas ativas |
| `--accent-soft` | `#EAF1FF` | Fundo de itens selecionados e balão do agente bot |
| `--bg` | `#F1F2F3` | Plano de fundo geral da aplicação (modo claro) |
| `--surface` | `#FFFFFF` | Cartões, painéis laterais e janelas |
| `--fg` / `--title`| `#0E1726` / `#3B3F5C` | Tipografia principal e cabeçalhos |
| `--muted` | `#515365` | Textos secundários, legendas e metadados |
| `--line` | `#E0E6ED` | Bordas e divisores estruturais |
| `--ok` / `--ok-soft` | `#5C8A1E` / `#EEF6E2` | Status positivo, faturas pagas, balão do cliente |
| `--warn` / `--warn-soft` | `#A8670F` / `#FCF2E3` | Alertas de vencimento, promessas de pagamento |
| `--bad` / `--bad-soft` | `#DC3545` / `#FCE8EA` | Faturas vencidas, erros de webhook, bloqueios |

### Tipografia
- **Títulos e Interface Geral:** `Roboto` (400 regular, 500 medium, 700 bold).
- **Dados Numéricos, Códigos e Protocolos:** `IBM Plex Mono` (tabular numbers para valores em R$, kWh, datas e CPFs).

---

## 3. Arquitetura das 5 Telas Principais para o Protótipo no Figma

### Tela 1: App Shell & Painel ao Vivo (Dashboard de Operação)
- **Barra Superior Fixa:** Menus do Performalog (`Dashboard`, `Cadastros`, `Sucesso do Cliente`, `Vendas`, e a nova aba destacada `Atendimento` com badge de fila em tempo real).
- **Trilho Lateral de Navegação (Sidebar):** Ícones e rótulos para `Início`, `Conversas`, `Contatos`, `Campanhas`, `Cobrança`, `Automação`, `Relatórios` e `⚙ Configurações`.
- **Cards de Métricas (KPIs):** Total de conversas ativas, fila por setor (Sucesso do Cliente vs Cobrança), tempo médio de resposta e taxa de resolução pelo agente.
- **Painel de Autorizações Pendentes:** Lista de propostas geradas pelo agente que ultrapassam a alçada automática (ex.: desconto de juros acima do limite) aguardando aprovação do supervisor.

### Tela 2: Inbox Unificado e Chat Omnichannel
- **Coluna Esquerda (Filtros e Fila de Atendimento):** Abas `Minhas`, `Fila do Setor` e `Todas`. Cards de conversas com nome do cliente, última mensagem, tempo de espera e tags coloridas (`[Bot Cobrança]`, `[Promessa Pgto]`, `[Vencido D+5]`).
- **Coluna Central (Área de Conversa / Chat):**
  - Cabeçalho com nome do contato, telefone E.164, protocolo gerado e botões `Transferir`, `Pausar Bot` e `Encerrar`.
  - Histórico de mensagens com balões estilizados:
    * Mensagem recebida do cliente (branco com borda).
    * Mensagem enviada pelo atendente humano (verde suave).
    * Mensagem gerada pelo Agente Inteligente (azul suave com badge `IA`).
  - Indicador de status da **Janela de 24 horas da Meta** (Graph API v26.0).
  - Caixa de composição (Composer) com atalhos de respostas rápidas e disparo de 2ª via de fatura.

### Tela 3: Ficha 360° do Cliente e Conciliação Financeira
- **Painel Lateral Direito Integrado ao Chat:**
  - **Identificação:** Nome, CPF/CNPJ mascarado (LGPD), e-mail e status de opt-in.
  - **Unidade Consumidora (UC) & Dados CEMIG:** Número da instalação, classe de consumo, créditos de energia solar disponíveis em kWh (`cemig_gd_report`), rateio mensal e economia acumulada.
  - **Extrato Financeiro (Digital Grid):** Faturas em aberto com valor principal, juros e multa calculados, botão de copiar código de barras Pix e PDF.
  - **Histórico de Negociação:** Registro de acordos prévios, promessas cumpridas e categorias de contestação anteriores.

### Tela 4: Central de Cobrança e Parametrização da Régua
- **Visão da Régua de Cobrança:** Fluxo cronológico com etapas parametrizáveis:
  * `D-3` (Lembrete preventivo com Pix).
  * `D0` (Aviso amigável de vencimento no dia).
  * `D+5` (Oferta de 2ª via sem encargos adicionais).
  * `D+10` (Acionamento do Agente de Cobrança para proposta à vista com isenção de multa).
  * `D+20` / `D+30` (Avisos de negativação e opção de parcelamento no cartão).
- **Editor de Políticas de Acordo:** Configuração de alçadas (limite de parcelas no cartão e boleto, teto de isenção de encargos e regras de transbordo imediato).

### Tela 5: Console de Governança, Webhooks e API da Meta
- **Monitoramento de Integração:** Status de conexão com a WhatsApp Cloud API da Meta, qualidade do número (`HIGH`), throughput de envio.
- **Log de Eventos (Auditoria de Banco):** Tabela em tempo real com eventos de webhook (`wa_webhook_event`), confirmações de entrega (`sent`, `delivered`, `read`), tempo de processamento e logs de conformidade com a LGPD.

---

## 4. Roteiro de Interação para Apresentação no Figma (Fluxo Navegável)

1. **Passo 1:** O usuário inicia no **Painel ao Vivo**, visualiza o alerta de fila e clica em **Conversas**.
2. **Passo 2:** Clica em uma conversa sinalizada com a tag `[Bot Cobrança]`.
3. **Passo 3:** Acompanha o diálogo onde o cliente contesta a cobrança (`CONT-04 - Energia/crédito não recebido`).
4. **Passo 4:** O atendente consulta a **Ficha 360°** no painel lateral, verifica o relatório da CEMIG de créditos compensados e aciona a explicação automática detalhada.
5. **Passo 5:** O cliente solicita negociação para pagamento imediato; o agente sugere a proposta autorizada à vista via Pix, gerando a linha digitável diretamente do banco de dados.
6. **Passo 6:** O supervisor visualiza o encerramento do protocolo e o retorno à tela inicial com as métricas atualizadas.

---

## 5. Checklist de Entrega Acadêmica (Módulos 3 e 4)

- [x] Estrutura visual derivada diretamente do CRM corporativo Performalog.
- [x] Respeito estrito aos requisitos de acessibilidade (contraste legível, tipografia escalável).
- [x] Dados fictícios anonimizados para demonstração pública (sem exposição de CPFs ou contas reais de terceiros).
- [x] Link funcional do protótipo navegável gerado para submissão no AVA da Unyleya acompanhado do Certificado iTalents.
