# Guia Oficial para a Apresentação Presencial — APEX V (Performa Energy)

**Disciplina:** APEX V — Tecnologia em Banco de Dados (Faculdade Unyleya)  
**Projeto:** Performalog Atendimento: Agente Inteligente de Cobrança e Arquitetura de Banco de Dados para Gestão de Energia Solar  
**Local:** Sede Corporativa da Performa Energy (Sala de Reuniões Multimídia / Homologação)  
**Duração Prevista:** 90 minutos  
**Público-Alvo:** 14 colaboradores multidisciplinares (Atendimento/Sucesso do Cliente, Cobrança, Faturamento e TI)  

---

## 1. Objetivos da Intervenção Extensionista

1. **Apresentar a Arquitetura de Banco de Dados:** Demonstrar a modelagem relacional proposta (`wa_*`), integrada ao CRM corporativo Performalog (MySQL Azure), relatórios de injeção da CEMIG (`cemig_gd_report`) e faturas da Digital Grid (`client_integration_bill`).
2. **Demonstrar o Funcionamento do Agente de Cobrança:** Explicar o princípio de *Grounding Determinístico* (a IA nunca inventa valores; todos os saldos e propostas vêm de dados reais do banco) e as réguas de negociação automatizadas (à vista $\to$ cartão $\to$ parcelado).
3. **Oficina Prática Hands-On com o Protótipo no Figma:** Permitir que os colaboradores naveguem pelas 5 telas principais da nova aba **Atendimento** no Performalog, testem simulações de atendimento, consultem a Ficha 360° do Cliente e validem as regras de transbordo humano.
4. **Coleta de Evidências Oficiais:** Captura das **3 fotos obrigatórias** (Módulo 4) e aplicação da Ficha de Avaliação da Comunidade Atendida (escala Likert).

---

## 2. Cronograma Detalhado da Apresentação (90 Minutos)

| Bloco | Tempo | Etapa | Descrição e Ações do Discente |
|:---:|:---:|---|---|
| **Bloco 1** | 00–15 min | **Abertura Institucional e Contexto da APEX V** | Acolhida da equipe, apresentação do programa extensionista "Educando para a Cidadania" da Faculdade Unyleya, contextualização dos ODS 7 (Energia Limpa) e ODS 9 (Infraestrutura Digital), e exposição dos objetivos da intervenção. |
| **Bloco 2** | 15–35 min | **Diagnóstico, Banco de Dados e WhatsApp Cloud API** | Demonstração do gargalo operacional com a ferramenta legada (Maxbot) e apresentação técnica da modelagem relacional de mensageria (`wa_contact`, `wa_conversation`, `wa_message`), webhooks da Meta (Graph API v26.0) e integração com faturas e relatórios da CEMIG. **(Momento ideal para o enquadramento da FOTO 1)** |
| **Bloco 3** | 35–65 min | **Oficina Hands-On: Navegação no Figma e Simulação do Agente** | Os analistas utilizam laptops corporativos ou acompanham na Smart TV a navegação no protótipo interativo da aba *Atendimento* do Performalog. Simulação de: (a) cliente contestando cobrança de energia não recebida; (b) visualização da Ficha 360° com saldo em kWh; (c) negociação com proposta pré-autorizada via Pix; (d) aprovação de exceção pelo supervisor. **(Momento ideal para o enquadramento da FOTO 2)** |
| **Bloco 4** | 65–80 min | **Debate sobre Governança, LGPD e Transbordo Humano** | Discussão aberta sobre as regras de interrupção da automação (ameaça jurídica, insatisfação extrema, erro de leitura) e garantia de conformidade com a LGPD (Privacy by Design). |
| **Bloco 5** | 80–90 min | **Avaliação da Comunidade, Registros Finais e Encerramento** | Distribuição da Ficha de Avaliação em escala Likert (impressa ou digital), coleta de depoimentos voluntários dos setores, registro da foto conclusiva com a equipe e agradecimentos finais à diretoria e colaboradores. **(Momento para a FOTO 3)** |

---

## 3. Protocolo Fotográfico Obrigatório (Módulo 4 — 50 Pontos)

Para garantir a pontuação integral da avaliação presencial, os três registros devem atender aos seguintes requisitos de composição e enquadramento:

- **FOTO 1 — Abertura e Apresentação da Arquitetura do Banco na Sala Corporativa:**
  - *Composição:* O discente extensionista em pé ao lado da tela de projeção/Smart TV (exibindo o slide com o diagrama de entidades e relacionamentos ou a arquitetura da WhatsApp Cloud API), com a plateia de colaboradores da Performa Energy em primeiro plano, participando ativamente.
- **FOTO 2 — Oficina Hands-On e Simulação de Atendimentos no Protótipo:**
  - *Composição:* Registro lateral em plano médio mostrando colaboradores em suas estações de trabalho/laptops interagindo com o protótipo no Figma da aba *Atendimento*, com o discente mediando e orientando a navegação. *(Evitar expor dados pessoais reais de clientes nas telas).*
- **FOTO 3 — Debate Conclusivo, Coleta da Avaliação e Encerramento:**
  - *Composição:* Registro amplo da equipe reunida na sala de reuniões colaborativa, com colaboradores preenchendo as fichas de avaliação impressas, validando o impacto da extensão universitária.

---

## 4. Roteiro de Falas do Discente Extensionista

### Abertura (Bloco 1):
> "Bom dia a todos os colaboradores e gestores da Performa Energy. Meu nome é Rafael Silva, sou estudante do Curso Superior de Tecnologia em Banco de Dados da Faculdade Unyleya. Como parte da disciplina de extensão curricular APEX V, desenvolvemos uma proposta técnica de ponta pensada sob medida para a nossa realidade: o **Performalog Atendimento**. Nosso foco hoje é demonstrar como uma arquitetura de banco de dados robusta, integrada à API oficial da Meta e com um Agente Inteligente de Cobrança ancorado em dados reais, pode solucionar nosso maior gargalo: o atendimento sobre faturas e a recuperação amigável de crédito de energia solar."

### Demonstração do Banco de Dados e Agente (Blocos 2 e 3):
> "Um dos pilares deste projeto é que a Inteligência Artificial nunca inventa valores de cobrança. O agente de cobrança não é um chatbot genérico: ele opera conectado diretamente às consultas relacionais do nosso CRM Performalog, lendo o relatório de compensação em kWh da CEMIG (`cemig_gd_report`) e as faturas da Digital Grid. Se o cliente questionar a cobrança, o agente explica a matemática exata da fatura com base no rateio real. E na negociação, ele segue uma régua estrita: 1º à vista com isenção de encargos sobre o principal, 2º cartão de crédito, e 3º parcelamento, sempre com supervisão humana e transbordo para os atendentes quando houver qualquer complexidade."

### Encerramento e Avaliação (Bloco 5):
> "Gostaria de agradecer imensamente à diretoria da Performa Energy e a cada um de vocês pela acolhida e pelas contribuições durante os testes hands-on. Para consolidar as evidências acadêmicas exigidas pelo Ministério da Educação e pela Unyleya, peço a gentileza de que cada um preencha nossa ficha de avaliação anônima em escala Likert, registrando sua percepção sobre a usabilidade da ferramenta, o ganho operacional e a segurança dos dados."

---

## 5. Checklist Pré-Apresentação

- [ ] Sala de reuniões reservada com Smart TV / Projetor HDMI testado.
- [ ] Protótipo no Figma aberto e pré-carregado no modo apresentação (`Present`).
- [ ] 14 vias da `FICHA_DE_AVALIACAO_PRESENCIAL_PERFORMA_ENERGY.html` impressas.
- [ ] Câmera do celular carregada e espaço de memória livre para os registros fotográficos.
- [ ] Canetas disponíveis para o preenchimento das fichas.
