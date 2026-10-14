# Performalog Atendimento & Agente de Cobrança — APEX V (Performa Energy)

Repositório oficial dos materiais do projeto de extensão universitária da disciplina **Ambiente Profissional e de Extensão em Banco de Dados V** (Curso Superior de Tecnologia em Banco de Dados — Faculdade Unyleya).

---

## 📌 Visão Geral do Projeto

* **Título Oficial**: *Performalog Atendimento: Agente Inteligente de Cobrança e Arquitetura de Banco de Dados para Gestão de Energia Solar na Performa Energy*
* **Instituição de Ensino**: Faculdade Unyleya (MEC Portaria nº 1.263/2012)
* **Curso**: Tecnologia em Banco de Dados (100 Horas de Extensão Curricular)
* **Disciplina**: AMBIENTE PROFISSIONAL E DE EXTENSÃO EM BANCO DE DADOS V
* **Empresa Parceira**: **Performa Energy** (Gestão de Créditos de Energia Solar por Assinatura / Geração Distribuída — Lei nº 14.300/2022)
* **Alinhamento com os Objetivos de Desenvolvimento Sustentável (Agenda 2030)**:
  * **ODS 7 — Energia Limpa e Acessível (Metas 7.2 e 7.b)**: Fomento à geração solar distribuída e clareza no rateio de créditos em kWh.
  * **ODS 9 — Indústria, Inovação e Infraestrutura (Metas 9.4 e 9.5)**: Modernização da infraestrutura de mensageria com WhatsApp Cloud API oficial da Meta e banco relacional.
  * **ODS 12 — Consumo e Produção Responsáveis (Meta 12.8)**: Transparência em cobranças e sustentabilidade da cadeia fotovoltaica.

---

## 📂 Mapa de Entregas e Arquivos Principais

| Arquivo | Descrição | Finalidade no AVA |
|---|---|---|
| [`TEMPLATE_PREENCHIDO_APEX_V_PERFORMA_ENERGY.pptx`](./TEMPLATE_PREENCHIDO_APEX_V_PERFORMA_ENERGY.pptx) / [`.pdf`](./TEMPLATE_PREENCHIDO_APEX_V_PERFORMA_ENERGY.pdf) | Apresentação oficial completa com os 20 slides preenchidos | Envio no Módulo 3 |
| [`APEX_V_Modulo_1_Etapa_1_Slides_1_a_6.pptx`](./APEX_V_Modulo_1_Etapa_1_Slides_1_a_6.pptx) / [`.pdf`](./APEX_V_Modulo_1_Etapa_1_Slides_1_a_6.pdf) | Pacote dedicado com Slides 1 a 6 | Submissão no Módulo 1 (1ª Etapa) |
| [`APEX_V_Modulo_2_Etapa_2_Slides_1_a_10.pptx`](./APEX_V_Modulo_2_Etapa_2_Slides_1_a_10.pptx) / [`.pdf`](./APEX_V_Modulo_2_Etapa_2_Slides_1_a_10.pdf) | Pacote dedicado com Slides 1 a 10 | Submissão no Módulo 2 (2ª Etapa) |
| [`DOCUMENTO_ENTREGA_SLIDES_APEX_V_PERFORMA_ENERGY.md`](./DOCUMENTO_ENTREGA_SLIDES_APEX_V_PERFORMA_ENERGY.md) | Transcrição textual integral lâmina por lâmina | Roteiro de apoio e conferência |
| [`PLANO_CORRECOES_SLIDES_APEX_V.md`](./PLANO_CORRECOES_SLIDES_APEX_V.md) | Checklist de conformidade, auditoria e status de cada etapa | Acompanhamento do projeto |
| [`ESPECIFICACAO_FIGMA_APEX_V.md`](./ESPECIFICACAO_FIGMA_APEX_V.md) | Especificação das 37 telas, design system e fluxos no Figma | Guia para o Módulo 4 (Envio 1) |
| [`GUIA_APRESENTACAO_PRESENCIAL_APEX_V.md`](./GUIA_APRESENTACAO_PRESENCIAL_APEX_V.md) | Roteiro de 90 min e protocolo das 3 fotos obrigatórias | Guia para o Módulo 4 (Envio 2) |
| [`FICHA_DE_AVALIACAO_PRESENCIAL_PERFORMA_ENERGY.html`](./FICHA_DE_AVALIACAO_PRESENCIAL_PERFORMA_ENERGY.html) | Formulário interativo e imprimível em 1 página A4 (escala Likert) | Aplicação pós-oficina na empresa |
| [`performalog_atendimento/`](./performalog_atendimento/) | Protótipo interativo web completo com arquitetura de negócio e APIs | Demonstração técnica |
| [`referencias_unyleya/`](./referencias_unyleya/) | Roteiro oficial, ementa da disciplina e template mestre da Unyleya | Documentos de referência |

---

## 🚀 Como Executar e Gerar os Entregáveis

- Para regenerar a apresentação em PowerPoint e os pacotes modulares (M1 e M2):
  ```bash
  python build_updated_apex_v.py
  ```
- Para exportar todos os PPTX em PDF limpos e sem marca d'água:
  ```bash
  python convert_all_pptx_to_pdf.py
  ```
- Para visualizar e imprimir a ficha de avaliação presencial:
  Abra o arquivo `FICHA_DE_AVALIACAO_PRESENCIAL_PERFORMA_ENERGY.html` em qualquer navegador web e clique no botão **Imprimir Ficha**.
