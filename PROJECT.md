# Projeto: APEX V — Performalog Atendimento (Tecnologia em Banco de Dados / Unyleya)

## 1. Visão Geral da Arquitetura
O núcleo do trabalho extensionista agora é a implementação do módulo **Atendimento** e do **Agente Inteligente de Cobrança** no CRM/ERP corporativo **Performalog**, da **Performa Energy**.
O projeto integra a **WhatsApp Cloud API oficial da Meta (Graph API v26.0)** ao banco de dados relacional MySQL (Azure), resolvendo a fragmentação da comunicação legada (Maxbot), reduzindo a inadimplência e esclarecendo dúvidas complexas sobre o rateio de créditos de energia solar (concessionária CEMIG).

### Princípio Arquitetural de Ouro: Grounding Determinístico
O agente de IA atua exclusivamente na camada conversacional humanizada. **A IA nunca calcula nem inventa valores monetários, encargos ou saldos de energia.** Todos os dados de consumo em kWh, faturas e propostas autorizadas são consultados diretamente nas tabelas relacionais do banco de dados e injetados de forma estrita no contexto.

---

## 2. Modelagem do Banco de Dados Relacional (MySQL Performalog)

### Tabelas do Subsistema de Mensageria (WhatsApp Cloud API)
- `wa_phone_number`: Cadastro dos números empresariais oficiais, WABA ID, limites e status de qualidade da linha da Meta.
- `wa_contact`: Identidade do cliente (telefone E.164, BSUID, vínculo com `cliente_id` do Performalog, opt-in/opt-out e conformidade com a LGPD).
- `wa_conversation`: Registro de cada protocolo de atendimento, setor atribuído, atendente, situação (bot, fila, atendimento, encerrada) e controle da janela de 24 horas da Meta.
- `wa_message`: Histórico integral de mensagens com identificador global `wamid`, autor (cliente, bot, atendente, sistema), payload, status de entrega (`sent`, `delivered`, `read`) e carimbo de tempo.
- `wa_campaign` & `wa_campaign_recipient`: Gestão de réguas de cobrança automatizadas e disparos em massa com templates pré-aprovados pela Meta.
- `wa_webhook_event`: Registro bruto de webhooks recebidos com validação de assinatura SHA-256 para auditoria de segurança.

### Tabelas de Energia e Faturamento Integradas
- `cemig_gd_report`: Leitura analítica mensal de créditos por Unidade Consumidora (UC), consumo ativo e injeção solar.
- `energy_balance_item`: Balanço mensal comparando relatório XML da concessionária, planilhas e previsões.
- `client_integration_bill`: Faturas integradas via API da Digital Grid (status, saldo devedor, Pix e linha digitável).

---

## 3. Mapeamento das Entregas Acadêmicas na Unyleya (APEX V — 100 Horas)

| Etapa | Módulo AVA | Entregável Oficial | Status Técnico Atual |
|:---:|:---:|---|---|
| **1ª Etapa** | **Módulo 1** (Até 10 pts) | Slides 1 a 6 do Template Padrão (Identificação, Ementa Oficial, ODS 7, 9 e 12, Local de Implementação) | **100% Gerado no PPTX e PDF modular.** Pronto para envio. |
| **2ª Etapa** | **Módulo 2** (Até 10 pts) | Slides 1 a 10 do Template Padrão (Participantes, Diagnóstico de Problema, Aprofundamento Teórico em Banco de Dados e IA) | **100% Gerado no PPTX e PDF modular.** Pronto para envio assim que liberar no AVA. |
| **3ª Etapa** | **Módulo 3** (Até 10 pts) | Certificado iTalents do curso de Figma + Template completo (Slides 1 a 20) | Template de 20 slides preenchido integralmente. Pendente realização do curso iTalents pelo estudante. |
| **4ª Etapa** | **Módulo 4** (Até 70 pts) | (a) Link do protótipo interativo no Figma + Certificado (Até 20 pts)<br>(b) Apresentação presencial com as 3 fotos obrigatórias e fichas de avaliação (Até 50 pts) | Especificação das 37 telas e 5 fluxos principais mapeada no Figma. Roteiro e Ficha de Avaliação Likert finalizados. |

---

## 4. Inventário dos Arquivos do Projeto

- `TEMPLATE_PREENCHIDO_APEX_V_PERFORMA_ENERGY.pptx` e `.pdf`: Apresentação completa com os 20 slides preenchidos, com layout e ABNT rigorosamente aplicados.
- `APEX_V_Modulo_1_Etapa_1_Slides_1_a_6.pptx` e `.pdf`: Pacote dedicado para submissão da 1ª Etapa no Módulo 1 (slides 1 a 6).
- `APEX_V_Modulo_2_Etapa_2_Slides_1_a_10.pptx` e `.pdf`: Pacote dedicado para submissão da 2ª Etapa no Módulo 2 (slides 1 a 10).
- `DOCUMENTO_ENTREGA_SLIDES_APEX_V_PERFORMA_ENERGY.md`: Transcrição textual integral de todos os 20 slides em estrita correspondência com a apresentação.
- `build_updated_apex_v.py`: Script Python oficial para geração determinística dos slides preenchidos e das versões modulares.
- `convert_all_pptx_to_pdf.py`: Script para conversão de apresentações em PDF com limpeza de marcas d'água.
- `ESPECIFICACAO_FIGMA_APEX_V_REVISTA.md`: Guia de arquitetura de interface e tokens de design para o Figma.
- `GUIA_APRESENTACAO_APEX_V_REVISTO.md`: Roteiro de 90 minutos para a oficina presencial e protocolo das 3 fotos.
- `FICHA_DE_AVALIACAO_PRESENCIAL_PERFORMA_ENERGY.html`: Instrumento de avaliação em escala Likert pronto para impressão em 1 página A4.
- `performalog_atendimento/`: Diretório com o protótipo funcional completo e especificações detalhadas de negócio e APIs.
