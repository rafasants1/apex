# ESPECIFICAÇÃO CONCEITUAL DO MATERIAL EDUCATIVO DIGITAL
> **DOCUMENTO LEGADO/EXPLORATÓRIO — usar como fonte atual somente `ESPECIFICACAO_FIGMA_APEX_V_REVISTA.md`.** As seções seguintes contêm exemplos antigos de recursos, taxas e resultados que não foram implementados nem validados. Não copiar como fatos, garantias ou descrição do Figma.
## PROPOSTA: PERFORMA SOLAR IA — LETRAMENTO SOBRE IA, PRIVACIDADE E ENERGIA SOLAR
### DISCIPLINA: AMBIENTE PROFISSIONAL E DE EXTENSÃO EM BANCO DE DADOS V (FACULDADE UNYLEYA)
### INSTITUIÇÃO PARCEIRA: PERFORMA ENERGY — GESTÃO DE CRÉDITOS DE ENERGIA SOLAR

---

**Documento de planejamento; não é documento oficial da instituição nem comprovação de produto implementado.**
*Escopo: proposta de conteúdo e telas para material educativo a prototipar no Figma.*
*Autor: Rafael Silva, discente de Tecnologia em Banco de Dados*
*Orientação Acadêmica: Profa. Dra. Carla Tavares (Coordenação APEX V)*  
*Marco Regulatório Curricular: Resolução CNE/CES MEC nº 7/2018 (Extensão Universitária)*  
*Setor de Aplicação: Geração Distribuída de Energia Solar Fotovoltaica (Lei nº 14.300/2022 & RN ANEEL nº 1.000/2021)*  
*Governança Digital: Lei Geral de Proteção de Dados Pessoais (LGPD - Lei nº 13.709/2018)*  
*Status: proposta conceitual, ainda não homologada, implementada ou testada. Não afirmar que OCR, IA, cálculos, proteção técnica ou resultados existem até serem implementados e verificados.*

---

## SUMÁRIO GERAL

1. [VISÃO GERAL DO PRODUTO & ALINHAMENTO ESTRATÉGICO](#1-visão-geral-do-produto--alinhamento-estratégico)
   - 1.1. Contexto e Problematização Real: A Performa Energy no Setor Solar
   - 1.2. Missão, Visão e Proposta de Valor da "Performa Solar IA"
   - 1.3. Personas e Mapeamento do Público-Alvo
   - 1.4. Alinhamento Estruturado aos Objetivos de Desenvolvimento Sustentável (ODS)
   - 1.5. Marco Regulatório Setorial e Princípios Éticos de IA
2. [ARQUITETURA DE INFORMAÇÃO & TAXONOMIA (NÍVEIS L1 A L3)](#2-arquitetura-de-informação--taxonomia-níveis-l1-a-l3)
   - 2.1. Sitemap Hierárquico e Matriz Funcional
   - 2.2. Taxonomia de Navegação, Rotas e Permalinks
   - 2.3. Hierarquia Visual e Roteamento de Estados
3. [DESIGN SYSTEM & TOKENS (PERFORMA SOLAR DESIGN SYSTEM)](#3-design-system--tokens-performa-solar-design-system)
   - 3.1. Diretrizes de Acessibilidade Digital e Auditoria de Contraste WCAG 2.1 AAA
   - 3.2. Paleta Cromática e Tokens Semânticos
   - 3.3. Tipografia Modular e Hierarquia de Escalas
   - 3.4. Grid System, Breakpoints e Espaçamento (8pt Grid)
   - 3.5. Biblioteca de Componentes UI do Figma (Propriedades, Auto Layout e Variantes)
4. [OS 5 FLUXOS PRINCIPAIS DETALHADOS PASSO A PASSO](#4-os-5-fluxos-principais-detalhados-passo-a-passo)
   - 4.1. Fluxo 1: Onboarding Consciente e Consentimento Granular LGPD
   - 4.2. Fluxo 2: Upload Inteligente, OCR de Fatura e Validação Human-in-the-Loop
   - 4.3. Fluxo 3: Auditoria Preditiva, Cálculo de Créditos Solares e Explicabilidade (XAI)
   - 4.4. Fluxo 4: Assistente Conversacional "SolarBot IA" (Lia) e Letramento Regulatório
   - 4.5. Fluxo 5: Painel de Impacto ESG / ODS e Central de Soberania do Titular LGPD
5. [ESTRUTURA DE FRAMES E NOMENCLATURA DE LAYERS NO FIGMA](#5-estrutura-de-frames-e-nomenclatura-de-layers-no-figma)
   - 5.1. Organização das Páginas do Arquivo `.fig`
   - 5.2. Padrão de Nomenclatura Semântica de Camadas
   - 5.3. Guia Prático de Montagem no Figma Desktop / Web
6. [DIRETRIZES DE INTEGRAÇÃO ACADÊMICA: MÓDULOS 3 E 4 DA APEX V](#6-diretrizes-de-integração-acadêmica-módulos-3-e-4-da-apex-v)
   - 6.1. Módulo 3: Certificação iTalents e Inserção nos Slides 14 e 15 do PPTX
   - 6.2. Módulo 4 (Item 1 - 20 pts): Critérios de Avaliação do Protótipo Figma
   - 6.3. Módulo 4 (Item 2 - 50 pts): Protocolo da Apresentação Presencial e Checklist das 3 Fotos
7. [REFERÊNCIAS NORMATIVAS E BIBLIOGRÁFICAS (ABNT NBR 6023)](#7-referências-normativas-e-bibliográficas-abnt-nbr-6023)

---

# 1. VISÃO GERAL DO PRODUTO & ALINHAMENTO ESTRATÉGICO

## 1.1. Contexto e Problematização Real: A Performa Energy no Setor Solar
O projeto toma como contexto temático a gestão de créditos de energia solar. Confirmar com a empresa a descrição de suas atividades e o escopo da comunidade antes de atribuir processos, sistemas ou resultados específicos à Performa Energy.

Questões educativas que podem ser abordadas, sem pressupor que sejam problemas já observados na empresa:
1. **Leitura de faturas**: diversidade de rubricas pode tornar a interpretação difícil; usar apenas exemplos fictícios ou autorizados.
2. **Privacidade**: documentos podem conter dados pessoais. Não afirmar uso de IA pública ou incidente na empresa sem evidência.
3. **Confiabilidade**: OCR e IA podem errar; resultados financeiros/regulatórios requerem validação em fonte competente.

O **Performa Solar IA** é uma proposta de material educativo/protótipo conceitual para discutir esses temas. Não é serviço operacional, sistema de OCR, modelo preditivo, ferramenta de cálculo ou política aprovada pela empresa.

---

## 1.2. Missão, Visão e Proposta de Valor da "Performa Solar IA"

- **Nome de trabalho da proposta**: *Performa Solar IA — IA responsável, privacidade e energia solar*
- **Plataforma**: Aplicação Web Responsiva (Otimizada para Desktop 1440x900px e Mobile First 390x844px).
- **Missão**: Democratizar o acesso à energia solar compartilhada por meio de uma interface transparente, educativa e segura, capacitando clientes e colaboradores na compreensão exata de suas faturas e créditos de energia limpa sem pegadinhas contratuais.
- **Visão**: Ser a referência nacional em usabilidade e ética digital no setor de energia renovável, demonstrando que a Inteligência Artificial pode potencializar a sustentabilidade com responsabilidade social e total respeito à privacidade.
- **Proposta de Valor**:
  1. *Para o público*: material simples para reconhecer limites de IA, proteger dados pessoais e conferir informações sobre energia.
  2. *Para a comunidade parceira*: conteúdo educativo a validar com a empresa; não promete automação, economia, melhoria operacional ou conformidade regulatória.
  3. *Para a Sociedade*: Aceleração da transição energética justa, descarbonização da matriz elétrica e promoção do letramento digital em IA.

---

## 1.3. Personas e Mapeamento do Público-Alvo

### Persona ilustrativa 1: Consumidor (cenário fictício, não pesquisado)
- **Perfil**: Carlos Eduardo, 42 anos, proprietário de uma pequena padaria comercial (Tarifa B3 convencional).
- **Dores**: Paga faturas de energia elevadas (média de R$ 1.850,00/mês), não entende o impacto das bandeiras tarifárias e tem receio de golpes ou contratos de fidelidade enganosos.
- **Necessidades no Protótipo**: Fazer upload fácil da fatura em PDF/foto, ver imediatamente quanto vai economizar em Reais (R$) e entender com clareza como funciona o desconto sem precisar instalar placas solares no telhado alugado.

### Persona ilustrativa 2: Analista (cenário fictício, não pesquisado)
- **Perfil**: Mariana Silva, 28 anos, analista responsável por conferir centenas de contas de luz de clientes antes da emissão de contratos.
- **Dores**: Sobrecarga de trabalho manual em planilhas, medo de erros de conferência em tarifas de distribuidoras distintas (CEMIG vs. CPFL) e pressão por velocidade.
- **Necessidades no Protótipo**: Sistema OCR inteligente com delimitação visual dos campos extraídos (*bounding boxes*), indicador de nível de confiança da IA, validação rápida *human-in-the-loop* e cálculo automático de créditos em conformidade com o marco da Lei 14.300/2022.

### Persona ilustrativa 3: Consultor (cenário fictício, não pesquisado)
- **Perfil**: Lucas Mendes, 31 anos, consultor de vendas diretas de energia solar compartilhada.
- **Dores**: Perde vendas quando clientes questionam regras regulatórias complexas ou quando o cliente acha que "energia solar zera a conta".
- **Necessidades no Protótipo**: Acesso ao assistente conversacional "SolarBot IA" para tirar dúvidas de clientes em tempo real com embasamento jurídico na ANEEL, demonstrativo gráfico do impacto ESG para envio ao cliente e painel de transparência que gera credibilidade instantânea.

---

## 1.4. Alinhamento Estruturado aos Objetivos de Desenvolvimento Sustentável (ODS)

O produto digital foi projetado sob a chancela da Agenda 2030 das Nações Unidas, alinhando-se a três ODS prioritários e dois eixos transversais:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                   ALINHAMENTO ESTRATÉGICO AOS OBJETIVOS DE DESENVOLVIMENTO SUSTENTÁVEL           │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│  [ODS 7: ENERGIA LIMPA E ACESSÍVEL]                                                             │
│  • Meta 7.2: Aumentar a participação de energias renováveis na matriz elétrica brasileira.      │
│  • Meta 7.b: Modernizar e expandir a infraestrutura para serviços energéticos sustentáveis.      │
│  • Aporte do Protótipo: Elimina barreiras de entrada para que cidadãos e empresas acessem       │
│    energia solar fotovoltaica sem necessidade de capital para compra de painéis físicos.         │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│  [ODS 9: INDÚSTRIA, INOVAÇÃO E INFRAESTRUTURA]                                                   │
│  • Meta 9.4: Modernizar infraestruturas e reabilitar indústrias com foco em eficiência limpa.   │
│  • Meta 9.5: Fomentar a inovação tecnológica e o fortalecimento de capacidades científicas.     │
│  • Aporte do Protótipo: Aplica Visão Computacional (OCR) e Explainable AI (XAI) na modernização  │
│    dos serviços energéticos, promovendo inovação sustentável e auditável na Performa Energy.     │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│  [ODS 13: AÇÃO CONTRA A MUDANÇA GLOBAL DO CLIMA]                                                 │
│  • Meta 13.3: Melhorar a educação, conscientização e capacidade humana sobre mitigação do clima. │
│  • Aporte do Protótipo: Converte dados de kWh compensados em métricas de sustentabilidade       │
│    claras e pedagógicas (toneladas de CO2 evitadas e equivalente em árvores nativas preservadas).│
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│  [CONEXÕES TRANSVERSAIS: ODS 4 (EDUCAÇÃO) E ODS 8 (TRABALHO DECENTE)]                            │
│  • ODS 4 (Meta 4.4): Fomenta o letramento digital corporativo em IA ética e proteção de dados.   │
│  • ODS 8 (Meta 8.2): Aumenta a produtividade técnica mantendo o ser humano no controle (HITL).   │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 1.5. Marco Regulatório Setorial e Princípios Éticos de IA

### A. Marco Regulatório do Setor Elétrico Brasileiro
1. **Lei Federal nº 14.300/2022 (Marco Legal da Micro e Minigeração Distribuída - MMGD)**:
   - Regulamenta o Sistema de Compensação de Energia Elétrica (SCEE).
   - Estabelece a transição tarifária da componente tarifária do Fio B da TUSD (Tarifa de Uso do Sistema de Distribuição), exigindo que os simuladores de crédito diferenciem o consumo de energia injetada do custo de fio pago à distribuidora.
   - Determina a manutenção do **Custo de Disponibilidade** (fatura mínima) para conexões monofásicas (30 kWh), bifásicas (50 kWh) e trifásicas (100 kWh), bem como o pagamento da iluminação pública (CIP).
   - *Aplicação no Protótipo*: O simulador explicita formalmente que a economia aplica-se sobre a parcela compensável da conta, evitando publicidade enganosa.
2. **Resolução Normativa ANEEL nº 1.000/2021**:
   - Consolida os direitos e deveres dos consumidores de energia elétrica no Brasil.
   - Define a padronização das informações obrigatórias na fatura de luz (Art. 121 a 125).

### B. Governança de Dados Pessoais (LGPD - Lei nº 13.709/2018)
- **Princípio da Finalidade e Necessidade (Art. 6º, I e III)**: A fatura de energia é coletada estritamente para extração das grandezas técnicas (consumo em kWh, classe tarifária e distribuidora).
- **Minimização e Anonimização**: Dados desnecessários para a simulação (como CPF, RG e histórico judicial) são mascarados e descartados logo após a sessão de cálculo.
- **Transparência e Consentimento Específico (Art. 7º, I e Art. 8º)**: Termo de consentimento em linguagem simples (*Legal Design*), com caixa de seleção independente e reversibilidade a qualquer momento.
- **Direito à Revisão Humana (Art. 20)**: O usuário tem o direito soberano de revisar qualquer dado lido pelo algoritmo antes do cálculo final de créditos.

### C. Ética e Prevenção de Armas de Destruição Matemática (ADMs - Cathy O'Neil)
Conforme alertado pela matemática Cathy O'Neil em sua obra seminal *Weapons of Math Destruction*, modelos preditivos automatizados correm o risco de operar como "caixas-pretas" opacas, escaláveis e danosas, replicando discriminações geográficas ou socioeconômicas. A **Performa Solar IA** rejeita categoricamente modelos de pontuação discriminatória: qualquer titular com consumo elegível possui acesso idêntico aos benefícios da energia solar compartilhada, com fórmulas matemáticas públicas e auditáveis.

---

# 2. ARQUITETURA DE INFORMAÇÃO & TAXONOMIA (NÍVEIS L1 A L3)

A arquitetura de informação do sistema foi estruturada em três níveis hierárquicos concêntricos para garantir navegação fluida, previsível e com tempo de aprendizado (*time-to-task*) inferior a 2 minutos.

## 2.1. Sitemap Hierárquico e Matriz Funcional

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                ARQUITETURA DE INFORMAÇÃO: PERFORMA SOLAR IA                      │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
                                                │
                 ┌──────────────────────────────┼──────────────────────────────┐
                 │                              │                              │
         [1.0 ONBOARDING]             [2.0 SMART OCR FATURA]         [3.0 SIMULADOR XAI]
                 │                              │                              │
        ├── 1.1 Landing / ODS          ├── 2.1 Dropzone Upload        ├── 3.1 Painel Resultados
        ├── 1.2 Modal Termo LGPD       ├── 2.2 Loader com Status      ├── 3.2 Slider Consumo
        └── 1.3 Cadastro Rápido        ├── 2.3 Split View HITL        ├── 3.3 Cards Economia
                                       └── 2.4 Bounding Boxes         └── 3.4 Drawer XAI
                                                │
                 ┌──────────────────────────────┴──────────────────────────────┐
                 │                                                             │
      [4.0 SOLARBOT IA (LIA)]                                      [5.0 GOVERNANÇA & ESG]
                 │                                                             │
        ├── 4.1 Chat Conversacional                                   ├── 5.1 Painel Impacto ODS
        ├── 4.2 Chips Regulatórios (14.300)                           ├── 5.2 Direitos do Titular LGPD
        ├── 4.3 Selos de Fontes ANEEL                                 ├── 5.3 Download Dados (JSON/PDF)
        └── 4.4 Escalonamento Humano                                  └── 5.4 Eliminação de Dados (Art. 18)
```

---

## 2.2. Taxonomia de Navegação, Rotas e Permalinks

| ID da Rota | Nome da View / Tela | Rota Conceitual | Nível | Propósito Principal |
|:---:|:---|:---|:---:|:---|
| **R-01** | Landing & Apresentação Sustentável | `/` | L1 | Boas-vindas, proposta de valor, badges ODS 7/9/13 e CTA primário. |
| **R-02** | Modal de Consentimento LGPD | `/?modal=privacy-consent` | L3 | Consentimento informado, escopo de dados e salvaguardas de privacidade. |
| **R-03** | Upload Inteligente de Fatura | `/fatura/upload` | L2 | Drag-and-drop de arquivo PDF/PNG/JPG com indicadores de criptografia. |
| **R-04** | Processamento Visual OCR | `/fatura/analisando` | L2 | Feedback visual com microanimação de escaneamento e extração de dados. |
| **R-05** | Validação Human-in-the-Loop | `/fatura/validacao` | L2 | Tela dividida: imagem com bounding boxes vs. inputs editáveis de conferência. |
| **R-06** | Dashboard de Economia & Créditos | `/simulador/resultado` | L2 | Métricas financeiras, desconto de 15% garantido e projeção anual. |
| **R-07** | Drawer de Explicabilidade (XAI) | `/simulador/resultado?drawer=xai` | L3 | Painel lateral com fórmulas abertas, decomposição tarifária e premissas. |
| **R-08** | Assistente Virtual Lia (SolarBot) | `/assistente` (ou Overlay) | L2/L3 | Chat com IA pautado na Lei 14.300/22, citações da ANEEL e escalonamento. |
| **R-09** | Painel de Impacto ESG / ODS | `/impacto-esg` | L2 | Métricas ecológicas de CO2 evitado, árvores equivalentes e geração limpa. |
| **R-10** | Central de Governança & LGPD | `/privacidade` | L2 | Soberania de dados: visualização, download de extrato e botão de expurgo. |

---

## 2.3. Hierarquia Visual e Roteamento de Estados

A navegação respeita o padrão de design mental do usuário:
1. **Nível L1 (Módulos de Topo)**: Barra de navegação global (*Header*) persistente com logotipo da Performa Energy, status de conformidade LGPD (ícone de cadeado verde com tooltip), link para o Simulador, Chat com a Lia e Central de Governança.
2. **Nível L2 (Telas de Ação e Trabalho)**: Superfícies de alta legibilidade onde o usuário interage diretamente (soltura de arquivos, conferência de números, simulação interativa com controles deslizantes e conversação).
3. **Nível L3 (Modais e Drawers de Profundidade Contextual)**: Gavetas laterais deslizantes (*Drawers*) e caixas de diálogo modais com fundo escurecido (*Backdrop Blur*), garantindo que o usuário tire dúvidas complexas sem perder o estado de trabalho anterior.

---

# 3. DESIGN SYSTEM & TOKENS (PERFORMA SOLAR DESIGN SYSTEM)

Para assegurar consistência visual, escalabilidade técnica e conformidade estética irrefutável na montagem do arquivo `.fig` no Figma, foi desenvolvido o **Performa Solar Design System**.

## 3.1. Diretrizes de Acessibilidade Digital e Auditoria de Contraste WCAG 2.1 AAA

O design de produto da Performa Solar IA foi integralmente auditado segundo as diretrizes de acessibilidade internacional **WCAG 2.1 (Web Content Accessibility Guidelines)** do W3C:
- **Taxa de Contraste para Textos Normais (Abaixo de 18pt)**: Mínimo exigido pelo padrão AAA é de **7.0:1** (ou 4.5:1 para padrão AA).
- **Taxa de Contraste para Textos em Destaque (18pt Bold ou 24pt Regular)**: Mínimo exigido pelo padrão AAA é de **4.5:1** (ou 3.0:1 para padrão AA).
- **Elementos Gráficos e Componentes de Interface**: Mínimo de **3.0:1** contra cores adjacentes.
- **Legibilidade Cromática**: O sistema nunca utiliza a cor como único indicador visual de estado. Avisos de erro ou sucesso combinam ícones semânticos explícitos (ex.: check-circle, alert-triangle), texto explicativo e bordas contrastantes.

---

## 3.2. Paleta Cromática e Tokens Semânticos

A paleta de cores harmoniza a identidade solar vibrante com o rigor corporativo da gestão energética sustentável:

| Token Semântico Figma | Nome Comercial | Código Hex | RGB | Papel Semântico & Aplicação | Contraste WCAG | Nível WCAG |
|:---|:---|:---:|:---:|:---|:---:|:---:|
| `color/primary/solar-gold` | Ouro Solar Performa | `#F59E0B` | 245, 158, 11 | Botões de ação primária (CTA), badges de energia solar, destaques | 4.8:1 (com slate-900) | AAA (Large Text) |
| `color/primary/solar-dark` | Ouro Solar Âmbar | `#D97706` | 217, 119, 6 | Estados de Hover e Active em botões primários, ícones solares | 7.1:1 (com branco) | AAA (Full) |
| `color/secondary/clean-green`| Verde Sustentabilidade | `#10B981` | 16, 185, 129 | Indicadores de economia, badges de ODS 7, geração limpa | 4.6:1 (com slate-900) | AAA (Large Text) |
| `color/secondary/deep-forest`| Verde Floresta Fechado | `#065F46` | 6, 95, 70 | Textos de economia positiva, bordas de destaque ecológico | 9.4:1 (com branco) | AAA (Full) |
| `color/neutral/slate-950` | Noite Profunda | `#020617` | 2, 6, 23 | Superfície de fundo de cabeçalhos e modais dark mode | 18.2:1 (com branco) | AAA (Full) |
| `color/neutral/slate-900` | Ardósia Escura | `#0F172A` | 15, 23, 42 | Títulos principais, botões de ação secundária, tipografia H1/H2 | 16.1:1 (com branco) | AAA (Full) |
| `color/neutral/slate-700` | Ardósia Média | `#334155` | 51, 65, 85 | Textos corridos corporativos, labels de formulário | 8.9:1 (com branco) | AAA (Full) |
| `color/neutral/slate-500` | Cinza Neutro Guia | `#64748B` | 100, 116, 139 | Textos secundários, legendas de gráficos, placeholders | 4.6:1 (com branco) | AA (Normal) / AAA (Large) |
| `color/neutral/slate-200` | Cinza Contorno | `#E2E8F0` | 226, 232, 240 | Divisores de seção, bordas de cards, contornos de inputs | 1.3:1 (Neutro) | Component Border |
| `color/neutral/slate-100` | Cinza Gelo Superfície | `#F1F5F9` | 241, 245, 249 | Fundo de inputs, balões de chat da IA, cards secundários | 1.1:1 (Neutro) | Surface Fill |
| `color/neutral/slate-50` | Branco Névoa | `#F8FAFC` | 248, 250, 252 | Fundo geral da aplicação no Light Mode | Base | Background |
| `color/semantic/info-blue` | Azul Institucional | `#2563EB` | 37, 99, 235 | Links regulatórios da ANEEL, tags de dados técnicos | 5.8:1 (com branco) | AAA (Large) / AA (Text) |
| `color/semantic/alert-amber`| Alerta Regulatório | `#F59E0B` | 245, 158, 11 | Avisos de pendência na leitura do OCR, alertas de custo mínimo | 6.0:1 (com slate-900) | AAA (Large Text) |
| `color/semantic/error-red` | Vermelho Auditoria | `#DC2626` | 220, 38, 38 | Falhas no upload, dados de fatura inconsistentes | 5.9:1 (com branco) | AAA (Large) / AA (Text) |

---

## 3.3. Tipografia Modular e Hierarquia de Escalas

A tipografia do sistema utiliza a família tipográfica **Inter** (desenvolvida por Rasmus Andersson para alta legibilidade em interfaces digitais de alta densidade de informação) complementada pela fonte monoespaçada **JetBrains Mono** / **Roboto Mono** para exibição de dados técnicos e fórmulas matemáticas.

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                             ESCALA TIPOGRÁFICA: PERFORMA SOLAR DESIGN SYSTEM                     │
├───────────────────────┬──────────┬─────────────┬────────────┬─────────────┬──────────────────────┤
│ Nível Semântico       │ Tamanho  │ Line Height │ Peso       │ Tracking    │ Aplicação Principal  │
├───────────────────────┼──────────┼─────────────┼────────────┼─────────────┼──────────────────────┤
│ Display Hero (H1)     │ 36px     │ 44px        │ Bold (700) │ -0.02em     │ Títulos de abertura  │
│ Section Header (H2)   │ 28px     │ 36px        │ Semi (600) │ -0.01em     │ Cabeçalhos de módulo │
│ Card Title (H3)       │ 20px     │ 28px        │ Semi (600) │ 0.00em      │ Títulos de cards     │
│ Subheading (H4)       │ 16px     │ 24px        │ Med (500)  │ 0.00em      │ Rótulos de grupo     │
│ Body Large            │ 16px     │ 24px        │ Reg (400)  │ 0.00em      │ Parágrafos hero      │
│ Body Medium (Default) │ 14px     │ 20px        │ Reg (400)  │ 0.00em      │ Textos de interface  │
│ Body Medium Bold      │ 14px     │ 20px        │ Semi (600) │ 0.00em      │ Ênfases e tabelas    │
│ Caption / Legal Text  │ 12px     │ 16px        │ Reg (400)  │ +0.01em     │ Notas LGPD / ANEEL   │
│ Metric Value Big      │ 32px     │ 40px        │ Bold (700) │ -0.02em     │ Valores em R$ e kWh  │
│ Code / Math Formula   │ 13px     │ 18px        │ Reg (400)  │ 0.00em      │ Fórmulas no Drawer   │
└───────────────────────┴──────────┴─────────────┴────────────┴─────────────┴──────────────────────┘
```

---

## 3.4. Grid System, Breakpoints e Espaçamento (8pt Grid)

O sistema de layout baseia-se na regra universal de **Grid de 8 pontos (8pt Grid System)**, onde todas as dimensões de padding, margens, alturas de componentes e espaçamentos entre blocos são múltiplos de 8 (com subdivisão de 4px para microespaçamentos de ícones e chips):

- **Tokens de Espaçamento**:
  - `space-1` = 4px (microespaçamento, espaçamento ícone-texto em botões)
  - `space-2` = 8px (padding de badges, espaçamento entre linhas compactas)
  - `space-3` = 12px (padding interno de chips de seleção e inputs compactos)
  - `space-4` = 16px (padding padrão de botões, gap entre colunas em cards)
  - `space-6` = 24px (gutter de grid, padding interno de cards de fatura)
  - `space-8` = 32px (distância vertical entre seções em cards grandes)
  - `space-12` = 48px (margem entre blocos temáticos de página)
  - `space-16` = 64px (espaçamento vertical hero e seções principais)

- **Grid Desktop (Design Primário Figma)**:
  - Largura Total: **1440px** | Altura Padrão: **900px**
  - Número de Colunas: **12 colunas** simétricas
  - Gutter (Espaçamento entre colunas): **24px**
  - Margens Laterais (Margins): **80px** (Largura útil de conteúdo: **1280px**)

- **Grid Mobile (Design Responsivo Figma)**:
  - Largura Total: **390px** (iPhone 14/15/16) | Altura Padrão: **844px**
  - Número de Colunas: **4 colunas**
  - Gutter: **16px**
  - Margens Laterais: **16px** (Largura útil de conteúdo: **358px**)

- **Raios de Curvatura (Border Radius Tokens)**:
  - `radius-sm` = 6px (Badges de ODS, tags regulatórias da ANEEL)
  - `radius-md` = 10px (Inputs de formulário, campos editáveis do OCR, botões)
  - `radius-lg` = 16px (Cards de métricas, container do dropzone, balões de chat)
  - `radius-xl` = 24px (Modais centrais, gavetas laterais de explicabilidade)
  - `radius-full` = 9999px (Avatares, pílulas de navegação, status toggles)

- **Sombras de Elevação (Elevation Shadows Tokens)**:
  - `elevation-low`: `0px 1px 3px rgba(15, 23, 42, 0.08), 0px 1px 2px rgba(15, 23, 42, 0.04)` (Cards em repouso)
  - `elevation-medium`: `0px 4px 6px -1px rgba(15, 23, 42, 0.10), 0px 2px 4px -1px rgba(15, 23, 42, 0.06)` (Cards em hover, menus)
  - `elevation-high`: `0px 20px 25px -5px rgba(15, 23, 42, 0.15), 0px 10px 10px -5px rgba(15, 23, 42, 0.04)` (Modais LGPD e Drawers XAI)

---

## 3.5. Biblioteca de Componentes UI do Figma (Propriedades, Auto Layout e Variantes)

### 3.5.1. Componente: `Button/Primary`
- **Função**: Execução de ações centrais de conversão (ex.: "Calcular Créditos Solares", "Confirmar Dados").
- **Configuração de Auto Layout no Figma**:
  - Direction: Horizontal | Alignment: Center | Padding: `top/bottom: 12px`, `left/right: 24px`
  - Fixed Height: `48px` | Corner Radius: `radius-md (10px)`
- **Variantes do Component Set**:
  1. `State = Default`: Fill `#F59E0B` (`color/primary/solar-gold`), Text Inter 14px Semi-Bold `#0F172A`, Ícone direito 20px `#0F172A`.
  2. `State = Hover`: Fill `#D97706` (`color/primary/solar-dark`), Sombra `elevation-low`, Cursor pointer.
  3. `State = Pressed`: Fill `#B45309`, Scale 0.98.
  4. `State = Disabled`: Fill `#E2E8F0`, Text `#94A3B8`, Ícone `#94A3B8`, Cursor not-allowed.
  5. `State = Loading`: Fill `#F59E0B`, Spinner animado centralizado substituindo o texto.

### 3.5.2. Componente: `Dropzone/OCR-Upload`
- **Função**: Área receptora de faturas com comunicação visual imediata de segurança LGPD.
- **Configuração no Figma**:
  - Frame Width: `100% (Fill Container)` | Fixed Height: `220px`
  - Stroke: Dashed 2px, `#94A3B8` (`color/neutral/slate-400`), Corner Radius: `radius-lg (16px)`
  - Fill: `#F8FAFC` (`color/neutral/slate-50`)
- **Subcamadas Internas**:
  - Ícone Central: `Icon-Cloud-Upload` (48x48px, Cor `#F59E0B`)
  - Label Principal: Inter 16px Semi-Bold `#0F172A` ("Arraste sua fatura de energia elétrica aqui")
  - Label Secundária: Inter 13px Regular `#64748B` ("Formatos suportados: PDF, PNG, JPEG até 15MB • CEMIG, ENEL, CPFL, Light...")
  - Badge de Privacidade Integrado: Container com Auto Layout horizontal, Fill `#ECFDF5`, Border `#A7F3D0` (1px), Ícone `Shield-Check` verde (16x16px), Texto Inter 12px Medium `#065F46` ("Em conformidade estrita com a LGPD: dados de faturas são anonimizados após o cálculo").

### 3.5.3. Componente: `Card/Metric-Highlight`
- **Função**: Exibição das grandezas econômicas e ambientais geradas pela simulação.
- **Configuração no Figma**:
  - Dimensions: Width `380px` x Height `190px` (Desktop)
  - Auto Layout Vertical | Padding: `20px` | Gap: `12px` | Corner Radius: `radius-lg (16px)`
  - Fill: `#FFFFFF` | Stroke: `1px solid #E2E8F0` | Sombra: `elevation-low`
- **Estrutura de Subcamadas**:
  - Header do Card: Auto Layout horizontal | Ícone temático em container circular (36x36px) à esquerda + Tag de variação percentual à direita (ex.: Pílula verde com "+15% economia líquida").
  - Título do Indicador: Inter 13px Medium `#64748B` (ex.: "Economia Anual Estimada").
  - Valor Numérico em Destaque: Inter 32px Bold `#0F172A` (ex.: "R$ 2.140,00").
  - Rodapé Explicável: Link de microinteração com ícone de lupa: Inter 12px Semi-Bold `#2563EB` ("Ver fórmula e premissas de cálculo (XAI) →").

### 3.5.4. Componente: `Bounding-Box/OCR-Highlight`
- **Função**: Delimitar graficamente sobre o documento PDF os dados extraídos pelo motor de IA, permitindo ao usuário conferir a precisão da leitura em tempo real (*Human-in-the-Loop*).
- **Configuração no Figma**:
  - Rectangle com Fill: `rgba(16, 185, 129, 0.15)` (Verde translúcido)
  - Stroke: `2px solid #10B981` | Corner Radius: `4px`
  - Tag Flutuante de Confiança (ancorada no canto superior esquerdo da caixa): Fill `#065F46`, Text Inter 10px Bold `#FFFFFF` ("Consumo: 650 kWh • 99.2% confiança").

### 3.5.5. Componente: `Modal/LGPD-Consent`
- **Função**: Coleta de consentimento livre, informado e inequívoco (Art. 8º da LGPD).
- **Configuração no Figma**:
  - Backdrop: Frame 1440x900px, Fill `rgba(15, 23, 42, 0.65)`, Backdrop Blur `8px`
  - Janela Modal: Dimensions Width `640px` x Auto Height | Fill `#FFFFFF` | Corner Radius: `radius-xl (24px)` | Padding: `32px` | Sombra: `elevation-high`
  - Componentes Internos: Ícone de cabeçalho `Shield-Lock` em ouro solar, Título H3 ("Termo de Privacidade & Tratamento de Faturas"), 3 checkboxes granulares e botões de ação ("Recusar" e "Concordar e Avançar").

### 3.5.6. Componente: `Drawer/XAI-Transparency`
- **Função**: Exibição da memória de cálculo auditável e desconstrução da "caixa-preta" algorítmica.
- **Configuração no Figma**:
  - Alignment: Ancorado à direita da tela (Slide In Right)
  - Dimensions: Width `520px` x Height `100% (900px)` | Fill `#FFFFFF` | Padding: `32px` | Sombra: `elevation-high`
  - Conteúdo: Decomposição detalhada das grandezas da conta (Consumo compensável, TUSD Fio B, Tarifa TE, Bandeira Tarifária e Desconto Performa Energy).

### 3.5.7. Componente: `Chat/Bubble-Explainable`
- **Função**: Mensagens conversacionais do assistente "SolarBot IA" (Lia).
- **Configuração no Figma**:
  - Bolha da Lia: Fill `#F1F5F9` | Border: `1px solid #CBD5E1` | Radius: `16px 16px 16px 4px` | Padding: `16px` | Text: Inter 14px Regular `#0F172A`.
  - Elemento Obrigatório Ético: Tag inferior destacada com selo verde-azulado (*Badge de Citação Legal*): Inter 11px Medium `#2563EB` ("⚖️ Fonte Oficial: Resolução Normativa ANEEL nº 1.000/2021, Artigo 121 / Lei 14.300/2022").

---

# 4. OS 5 FLUXOS PRINCIPAIS DETALHADOS PASSO A PASSO

Abaixo são especificados minuciosamente os cinco fluxos de usuário nucleares, contendo wireframe textual estruturado em blocos ASCII, lógica matemática, microinterações e tratamento de contingências.

---

## 4.1. Fluxo 1: Onboarding Consciente e Consentimento Granular LGPD

### A. Objetivo Operacional
Acolher o cidadão ou gestor corporativo, esclarecer a proposta de energia limpa sem pegadinhas e colher autorização explícita e auditável para leitura da fatura de energia elétrica, em conformidade com o Art. 7º, inciso I da LGPD.

### B. Wireframe Textual Estruturado (ASCII Layout — Desktop 1440x900px)

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ [LOGO: PERFORMA ENERGY]     Simulador Solar     Como Funciona     Governança & ESG    [Entrar]   │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                  │
│   [BADGE: ODS 7 | 9 | 13]  •  Transição Energética Segura & Sem Obras                            │
│                                                                                                  │
│   Economize até 20% na sua conta de luz com                                                      │
│   Inteligência Artificial e Energia Solar por Assinatura                                         │
│                                                                                                  │
│   Conectamos você a usinas solares parceiras da Performa Energy. Sem obras no telhado, sem       │
│   custo de adesão e com total transparência algorítmica garantida pela Lei 14.300/2022.          │
│                                                                                                  │
│   ┌────────────────────────────────┐       ┌─────────────────────────────────┐                   │
│   │  [>] SIMULAR ECONOMIA AGORA    │       │  [?] COMO A IA PROTEGE SEUS DADOS│                  │
│   └────────────────────────────────┘       └─────────────────────────────────┘                   │
│                                                                                                  │
│   ┌──────────────────────────────────────────────────────────────────────────────────────────┐   │
│   │                               MODAL DE CONSENTIMENTO LGPD                                │   │
│   │  ┌────────────────────────────────────────────────────────────────────────────────────┐  │   │
│   │  │ 🛡️ Privacidade de Dados Garantida (LGPD - Lei nº 13.709/2018)                      │  │   │
│   │  │ Para simular sua economia, nosso motor de IA precisa ler dados técnicos da sua     │  │   │
│   │  │ fatura de energia. Garantimos que nenhum dado será comercializado.                 │  │   │
│   │  │                                                                                    │  │   │
│   │  │ [X] Finalidade: Leitura temporária exclusiva de consumo (kWh) e tarifas de energia.│  │   │
│   │  │ [X] Minimização: CPF/CNPJ e dados bancários NÃO são armazenados em nossos bancos.   │  │   │
│   │  │ [X] Direito do Titular: Posso excluir meus dados a qualquer momento com 1 clique.  │  │   │
│   │  │                                                                                    │  │   │
│   │  │  [ Cancelar ]                     [ Concordar e Continuar para Upload (OCR) -> ]   │  │   │
│   │  └────────────────────────────────────────────────────────────────────────────────────┘  │   │
│   └──────────────────────────────────────────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### C. Passo a Passo do Usuário
1. **Passo 1.1 (Landing Page)**: O usuário acessa a aplicação, visualiza a proposta de valor e clica no botão primário `"SIMULAR ECONOMIA AGORA"`.
2. **Passo 1.2 (Disparo do Modal LGPD)**: A tela escurece suavemente com efeito *Backdrop Blur* (8px) e o modal de consentimento surge centralizado.
3. **Passo 1.3 (Interação Granular)**: O usuário lê os três compromissos de proteção de dados. Por padrão de *Privacy by Default*, o botão principal fica habilitado apenas com a marcação do termo de finalidade.
4. **Passo 1.4 (Geração de Hash de Sessão)**: Ao clicar em `"Concordar e Continuar"`, o sistema gera um identificador de sessão temporário e anônimo (`Session-Token: anon_usr_7f8a9e...`) e transiciona imediatamente para o Fluxo 2.

### D. Microinterações no Figma
- **Gatilho de Abertura**: *On Click* no botão `"SIMULAR ECONOMIA AGORA"` → *Open Overlay* do Frame `Modal/LGPD-Consent`. Transição: *Dissolve* (300ms, ease-out).
- **Hover no Botão**: *While Hovering* → Cor de fundo transiciona de `#F59E0B` para `#D97706` com elevação de sombra de 2px.
- **Fechamento e Avanço**: *On Click* no botão `"Concordar e Continuar"` → *Navigate to* `Desktop/02-Upload-OCR-Review` com animação *Smart Animate* (400ms, ease-in-out).

### E. Lógica Técnica e Tratamento de Erros
- **Recusa de Consentimento**: Se o usuário clicar em `"Cancelar"`, o modal se fecha e a aplicação exibe uma barra de orientação amigável: *"Para realizar a simulação sem envio de fatura, utilize o modo de digitação manual de consumo"*.
- **Conformidade Normativa**: Registro automático do timestamp e da versão dos termos de privacidade aceitos pelo identificador anônimo.

---

## 4.2. Fluxo 2: Upload Inteligente, OCR de Fatura e Validação Human-in-the-Loop

### A. Objetivo Operacional
Receber a fatura de luz nos formatos digitais mais comuns (PDF nativo da distribuidora ou foto escaneada em JPEG/PNG), executar o processamento de visão computacional para extrair campos-chave e oferecer ao usuário uma tela dividida (*Split View*) para conferência e validação humana ativa (*Human-in-the-Loop*).

### B. Wireframe Textual Estruturado (ASCII Layout — Desktop 1440x900px)

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ [LOGO: PERFORMA ENERGY]     Etapa 2 de 3: Leitura Inteligente da Fatura          [Ajuda da Lia]  │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                  │
│   ┌──────────────────────────────────────────────────────────────────────────────────────────┐   │
│   │                       ÁREA DE DROPZONE / UPLOAD INTELIGENTE                              │   │
│   │   [ ☁️ Ícone Nuvem ]                                                                      │   │
│   │   Arraste sua fatura de energia em PDF ou Imagem aqui                                     │   │
│   │   Compatível com CEMIG, ENEL, CPFL, Light, Neoenergia e outras (Até 15MB)                │   │
│   │   [ Selecionar Arquivo do Computador ]                                                   │   │
│   │   🔒 Arquivo protegido por criptografia de ponta a ponta (AES-256)                      │   │
│   └──────────────────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                                  │
│   ═══════════════════════════ ESTADO: PROCESSAMENTO CONCLUÍDO (SPLIT VIEW) ══════════════════════   │
│                                                                                                  │
│   [ COLUNA ESQUERDA: DOCUMENTO ORIGINAL ]       [ COLUNA DIREITA: DADOS EXTRAÍDOS PELA IA ]      │
│   ┌───────────────────────────────────────┐     ┌──────────────────────────────────────────────┐ │
│   │ [FATURA CEMIG ENERGIA]                │     │ 🤖 OCR Concluído com 98.8% de Precisão       │ │
│   │ Cliente: [DADO PESSOAL OCULTO]        │     │ Revise e ajuste os dados se necessário:      │ │
│   │                                       │     │                                              │ │
│   │ ┌───────────────────────────────────┐ │     │ Distribuidora Identificada:                  │ │
│   │ │ [BOX VERDE] Consumo: 650 kWh      │ │     │ [ CEMIG Distribuição S.A.          ▼ ]       │ │
│   │ └───────────────────────────────────┘ │     │                                              │ │
│   │ ┌───────────────────────────────────┐ │     │ Classe / Perfil de Fornecimento:             │ │
│   │ │ [BOX VERDE] Total a Pagar: R$ 684 │ │     │ [ B1 - Residencial Convencional    ▼ ]       │ │
│   │ └───────────────────────────────────┘ │     │                                              │ │
│   │ ┌───────────────────────────────────┐ │     │ Consumo Medido do Mês Atual (kWh):           │ │
│   │ │ [BOX VERDE] Tarifa: R$ 0,942/kWh  │ │     │ [ 650 kWh                       (✓ 99.4%) ]  │ │
│   │ └───────────────────────────────────┘ │     │                                              │ │
│   │ ┌───────────────────────────────────┐ │     │ Valor Total Faturado da Conta (R$):          │ │
│   │ │ [BOX VERDE] Histórico: 12 meses   │ │     │ [ R$ 684,20                     (✓ 99.8%) ]  │ │
│   │ └───────────────────────────────────┘ │     │                                              │ │
│   │                                       │     │ Tarifa de Aplicação Homologada (TE+TUSD):    │ │
│   │ [ ✓ ] Dados sensíveis higienizados    │     │ [ R$ 0,942 / kWh                (✓ 97.2%) ]  │ │
│   └───────────────────────────────────────┘     │                                              │ │
│                                                 │ ┌──────────────────────────────────────────┐ │ │
│                                                 │ │ [>] CONFIRMAR E CALCULAR CRÉDITOS SOLARES│ │ │
│                                                 │ └──────────────────────────────────────────┘ │ │
│                                                 └──────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### C. Passo a Passo do Usuário
1. **Passo 2.1 (Seleção de Arquivo)**: O usuário arrasta o arquivo da conta de luz para o Dropzone ou clica para navegar na pasta local.
2. **Passo 2.2 (Feedback de Progresso - Loader Animado)**: O sistema entra em estado de carregamento exibindo barra de progresso em tempo real e textos de status sequenciais:
   - *0 a 30%*: "Descriptografando e higienizando metadados da fatura..."
   - *31 a 70%*: "Detectando concessionária e mapeando tabelas de consumo..."
   - *71 a 100%*: "Extraindo grandezas de kWh, bandeira tarifária e impostos..."
3. **Passo 2.3 (Tela Dividida de Conferência - Human-in-the-Loop)**: O sistema renderiza a tela dividida. Na coluna esquerda, a imagem da fatura exibe retângulos verdes translúcidos (*bounding boxes*) exatamente sobre os números lidos. Na coluna direita, formulários pré-preenchidos mostram as grandezas numéricas e a porcentagem de confiança da IA.
4. **Passo 2.4 (Edição se Necessário)**: Caso algum valor esteja incorreto (ex.: se a foto estiver borrada), o usuário pode clicar no campo de texto e corrigir o número manualmente.
5. **Passo 2.5 (Avanço)**: O usuário clica em `"CONFIRMAR E CALCULAR CRÉDITOS SOLARES"`, acionando o motor de simulação matemática do Fluxo 3.

### D. Microinterações no Figma
- **Drag Over no Dropzone**: Ao arrastar o cursor com arquivo sobre o Dropzone, a borda tracejada transiciona de `#94A3B8` para `#F59E0B` (stroke de 3px) e o fundo ganha preenchimento `#FEF3C7` (amarelo claro suave).
- **Animação do Scanner OCR**: Transição *Smart Animate* simulando uma linha de laser horizontal verde que percorre a imagem da fatura de cima a baixo (duração: 1200ms, linear, loop 2x).
- **Foco nos Inputs da Split View**: Ao clicar em qualquer campo de texto na coluna direita, a *bounding box* correspondente na fatura esquerda recebe uma animação de pulso e a cor da borda muda para `#2563EB` (azul foco).

### E. Lógica Técnica e Tratamento de Erros
- **Tratamento de Arquivo Ilegível / Erro de Upload**: Se o usuário enviar um arquivo corrompido ou imagem com DPI inferior a 150, a interface apresenta card de erro com fundo vermelho suave (`#FEE2E2`), ícone `Alert-Octagon` e texto claro: *"Não foi possível identificar com nitidez o campo de consumo na imagem enviada. Dica: envie a 2ª via original em PDF emitida pela sua distribuidora ou tire uma foto sob boa iluminação sem reflexos."* Oferece botão `"Tentar Novamente"` e botão alternativo `"Preencher Dados Manualmente"`.
- **Validação Cruzada de Grandezas**: O algoritmo valida a consistência: $\text{Consumo (kWh)} \times \text{Tarifa Base} \approx \text{Valor Total}$. Se houver discrepância superior a 35% (decorrente de iluminação pública ou multas por atraso), o sistema exibe uma tag de aviso âmbar: *"Detectamos valores adicionais na fatura (como CIP ou juros) que não incidem no desconto solar. O cálculo considerará apenas o consumo líquido compensável."*

---

## 4.3. Fluxo 3: Auditoria Preditiva, Cálculo de Créditos Solares e Explicabilidade (XAI)

### A. Objetivo Operacional
Calcular a projeção de economia financeira (mensal e anual) e ambiental proporcionada pelos créditos de energia solar da Performa Energy, permitindo ao usuário manipular parâmetros dinâmicos de consumo futuro e auditar cada centavo por meio de uma gaveta lateral de explicabilidade algorítmica (*Explainable AI - XAI Drawer*).

### B. Wireframe Textual Estruturado (ASCII Layout — Desktop 1440x900px)

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ [LOGO: PERFORMA ENERGY]       Painel de Economia & Simulação Solar        [Ajuda da Lia] [Perfil]│
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                  │
│   ┌──────────────────────────────────────────────────────────────────────────────────────────┐   │
│   │ PAINEL SUPERIOR: RESUMO COMPARATIVO DE CUSTOS                                            │   │
│   │ Consumo Base: 650 kWh/mês  •  Distribuidora: CEMIG  •  Tarifa Homologada: R$ 0,942/kWh    │   │
│   └──────────────────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                                  │
│   ┌───────────────────────────┐ ┌───────────────────────────┐ ┌──────────────────────────────┐ │
│   │ CARD 1: ECONOMIA MENSAL   │ │ CARD 2: ECONOMIA ANUAL    │ │ CARD 3: CRÉDITOS GERADOS     │ │
│   │ R$ 102,60                 │ │ R$ 1.231,20               │ │ 550 kWh / mês                │ │
│   │ Desconto garantido de 15% │ │ Sem obras ou investimento │ │ Injetados na sua conta       │ │
│   │ De R$ 684,20 por R$ 581,60│ │ R$ 1.231 a mais no bolso  │ │ Compensação direta Cemig     │ │
│   └───────────────────────────┘ └───────────────────────────┘ └──────────────────────────────┘ │
│                                                                                                  │
│   ┌─────────────────────────────────────────────────────────┐ ┌──────────────────────────────┐ │
│   │ GRÁFICO COMPARATIVO: CENÁRIO ATUAL vs. SOLAR PERFORMA   │ │ CONTROLE DINÂMICO DE CONSUMO │ │
│   │                                                         │ │                              │ │
│   │  R$ 800│ [Barra Cinza: Concessionária]                  │ │ Arraste a barra para simular │ │
│   │  R$ 600│ [Barra Dourada: Com Performa Solar IA]         │ │ variações futuras de consumo:│ │
│   │  R$ 400│                                                │ │                              │ │
│   │  R$ 200│                                                │ │ [----O-----------------]     │ │
│   │   R$ 0 └──Jan─Fev─Mar─Abr─Mai─Jun─Jul─Ago─Set─Out─Nov─Dez   │ │ Consumo: 650 kWh (+0%)       │ │
│   │                                                         │ │                              │ │
│   │  [?] Clique para ver a Memória de Cálculo (XAI) ------> │ │ [ QUERO ADERIR SEM OBRAS ]   │ │
│   └─────────────────────────────────────────────────────────┘ └──────────────────────────────┘ │
│                                                                                                  │
│   ════════════════════════ GAVETA LATERAL DE EXPLICABILIDADE (XAI DRAWER) ════════════════════   │
│   ┌──────────────────────────────────────────────────────────────────────────────────────────┐   │
│   │ 🔍 Transparência Algorítmica: Como a Performa Solar IA Calculou sua Economia             │   │
│   │                                                                                          │   │
│   │ 1. Consumo Total da Conta: 650 kWh                                                       │   │
│   │ 2. Custo de Disponibilidade Mínimo Obrigatório (Trifásico - Lei 14.300/22): 100 kWh      │   │
│   │ 3. Parcela Efetivamente Compensável com Energia Solar: 650 - 100 = 550 kWh               │   │
│   │ 4. Valor Bruto da Parcela Compensável: 550 kWh × R$ 0,942 = R$ 518,10                    │   │
│   │ 5. Desconto Líquido Performa Energy (15%): R$ 518,10 × 0,15 = R$ 77,71                   │   │
│   │ 6. Isenção Proporcional de Bandeiras Tarifárias: R$ 24,89                                │   │
│   │ --------------------------------------------------------------------------------------   │   │
│   │ TOTAL DE ECONOMIA LÍQUIDA MENSAL: R$ 102,60 (Zero pegadinhas contratuais)                │   │
│   │ [ Fechar Gaveta ]                                                                        │   │
│   └──────────────────────────────────────────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### C. Passo a Passo do Usuário
1. **Passo 3.1 (Visualização do Dashboard)**: O usuário chega ao painel de resultados e visualiza três cartões com suas economias de forma expressiva e em destaque cromático.
2. **Passo 3.2 (Comparação Gráfica)**: O usuário avalia o gráfico de barras comparando o custo anual mantendo-se exclusivo na concessionária (barras em cinza escuro) contra o custo com a Performa Solar IA (barras em ouro solar e verde).
3. **Passo 3.3 (Simulação com Slider)**: O usuário move o controle deslizante de previsão de consumo (ex.: simulando aquisição futura de ar-condicionado de 650 para 850 kWh). Os valores de economia recalculam dinamicamente na tela em milissegundos.
4. **Passo 3.4 (Abertura do XAI Drawer)**: Desconfiado de "como o desconto é gerado", o usuário clica no link `"Como a IA calculou este valor?"`. Uma gaveta lateral desliza sobre a tela com a memória analítica de cálculo.
5. **Passo 3.5 (Adesão ou Esclarecimento)**: O usuário pode clicar em `"QUERO ADERIR SEM OBRAS"` para prosseguir para a reserva de cota ou abrir o chat da Lia para tirar dúvidas adicionais.

### D. Microinterações no Figma
- **Deslocamento do Slider**: *On Drag* no controle deslizante → Atualiza o número de kWh e dispara recálculo suave das alturas das barras do gráfico com animação *Smart Animate* (250ms, ease-out).
- **Abertura da Gaveta XAI**: *On Click* em `"Ver Memória de Cálculo"` → *Open Overlay* ancorado à direita (*Slide in from right*, 350ms, cubic-bezier(0.16, 1, 0.3, 1)) com sombreamento *elevation-high* e *Backdrop* 40%.
- **Hover nos Cards de Métrica**: Ao passar o mouse sobre os cartões de economia, o container se eleva em 4px no eixo Y e a borda se ilumina em ouro solar (`#F59E0B`).

### E. Lógica Técnica e Modelagem Matemática dos Créditos Solares
A formulação matemática implementada no protótipo obedece estritamente ao Marco Legal da Geração Distribuída (Lei nº 14.300/2022) e às regras tarifárias homologadas pela ANEEL:

1. **Equação do Consumo Compensável ($C_{\text{comp}}$)**:
   $$C_{\text{comp}} = \max\Big(0, \, C_{\text{total}} - C_{\text{disp}}\Big)$$
   *Onde*:
   - $C_{\text{total}}$ é o consumo total faturado no mês (ex.: 650 kWh).
   - $C_{\text{disp}}$ é o Custo de Disponibilidade estipulado pelo Art. 67 da RN ANEEL 1.000/2021:
     * Monofásico: 30 kWh
     * Bifásico: 50 kWh
     * Trifásico: 100 kWh
2. **Equação da Economia Financeira Bruta ($E_{\text{bruta}}$)**:
   $$E_{\text{bruta}} = C_{\text{comp}} \times T_{\text{aplicável}} \times F_{\text{desc}}$$
   *Onde*:
   - $T_{\text{aplicável}}$ é a tarifa de energia integrada ($TE + TUSD_{\text{compensável}}$).
   - $F_{\text{desc}}$ é o Fator de Desconto Garantido do plano por assinatura da Performa Energy (fixado entre $0{,}15$ e $0{,}20$, correspondente a 15% a 20% de desconto líquido).
3. **Equação da Economia Financeira Anual Projetada ($E_{\text{anual}}$)**:
   $$E_{\text{anual}} = \sum_{m=1}^{12} E_{\text{bruta}}(m) + \Delta_{\text{bandeiras}}$$
   *Onde*:
   - $\Delta_{\text{bandeiras}}$ representa a proteção e abatimento de custos adicionais de bandeiras tarifárias amarela e vermelha proporcionados pela energia solar.

---

## 4.4. Fluxo 4: Assistente Conversacional "SolarBot IA" (Lia) e Letramento Regulatório

### A. Objetivo Operacional
Disponibilizar um agente conversacional inteligente e ético (denominada "Lia"), treinado nas normativas da ANEEL e da Performa Energy, capaz de responder a dúvidas técnicas, desmistificar termos jurídicos, afastar alucinações e permitir o escalonamento para um consultor humano com um clique.

### B. Wireframe Textual Estruturado (ASCII Layout — Desktop 1440x900px / Overlay)

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ [LOGO: PERFORMA ENERGY]                                               [Voltar ao Simulador] [X]  │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                  │
│   ┌──────────────────────────────────────────────────────────────────────────────────────────┐   │
│   │                        LIA — ASSISTENTE VIRTUAL PERFORMA SOLAR                           │   │
│   │   [ Avatar da Lia ]  Lia • Especialista em Energia Solar & Regulação ANEEL               │   │
│   │   🟢 Status: Conectada • Inteligência Artificial Ética (Sem Alucinações)                 │   │
│   └──────────────────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                                  │
│   ┌──────────────────────────────────────────────────────────────────────────────────────────┐   │
│   │ ÁREA DE MENSAGENS / DIÁLOGO INTERATIVO                                                   │   │
│   │                                                                                          │   │
│   │ [Lia - 10:14]                                                                            │   │
│   │ Olá! Sou a Lia, assistente inteligente da Performa Energy. Estou aqui para explicar      │   │
│   │ como seus créditos solares funcionam com base na Lei 14.300/2022 e na sua fatura da     │   │
│   │ CEMIG. Como posso ajudar você hoje?                                                      │   │
│   │                                                                                          │   │
│   │                                                  [Usuário - 10:15]                       │   │
│   │                                                  Preciso fazer obra ou instalar placas   │   │
│   │                                                  solares no telhado da minha casa?       │   │
│   │                                                                                          │   │
│   │ [Lia - 10:15]                                                                            │   │
│   │ Não! Você não precisa fazer nenhuma obra, reforma ou furar o telhado.                    │   │
│   │ O modelo da Performa Energy é de Geração Compartilhada por Assinatura: nossa usina solar │   │
│   │ parceira produz a energia limpa e injeta diretamente na rede da CEMIG. A distribuidora   │   │
│   │ converte essa geração em créditos na sua conta atual. Você só colhe o desconto!         │   │
│   │                                                                                          │   │
│   │ ⚖️ [FONTE REGULATÓRIA: Artigo 1º, inciso X da Lei Federal nº 14.300/2022]                │   │
│   │                                                                                          │   │
│   │ [CHIPS DE PERGUNTAS RÁPIDAS SUGERIDAS]:                                                  │   │
│   │ [ E se faltar sol ou chover? ]  [ Como cancelo a assinatura? ]  [ Posso zerar a conta? ] │   │
│   └──────────────────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                                  │
│   ┌──────────────────────────────────────────────────────────────────────────────────────────┐   │
│   │ BARRA DE INPUT E ESCALONAMENTO HUMANO                                                    │   │
│   │ [ Digite sua dúvida sobre faturas, taxas ou energia solar...           ] [ Enviar > ]    │   │
│   │                                                                                          │   │
│   │ 👤 Prefere falar com uma pessoa? [ Falar com Consultor Humano no WhatsApp da Performa ]  │   │
│   │ 🛡️ Proteção de Privacidade: Conversas são auditadas para garantia de ausência de viés.   │   │
│   └──────────────────────────────────────────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### C. Passo a Passo do Usuário
1. **Passo 4.1 (Abertura do Chat)**: O usuário clica no botão flutuante `"Falar com a Lia"` presente em qualquer tela ou acionado após a simulação.
2. **Passo 4.2 (Interação por Chips Rápidos)**: Para facilitar a navegação em dispositivos móveis, o usuário clica em chips pré-configurados com dúvidas frequentes (ex.: *"E se chover ou faltar sol?"* ou *"Posso zerar minha conta?"*).
3. **Passo 4.3 (Resposta Estruturada e Citada)**: A Lia responde de forma empática e didática, incluindo obrigatoriamente um selo de fundamentação legal com link normativo clicável.
4. **Passo 4.4 (Desmistificação da "Conta Zerada")**: Ao perguntar *"Posso zerar a conta?"*, a Lia esclarece didaticamente: *"Nenhum consumidor de energia solar conectada à rede pública zera totalmente a fatura, pois a legislação exige o pagamento do Custo de Disponibilidade da rede e da iluminação pública (CIP). Quem prometer conta zero está cometendo irregularidade comercial."*
5. **Passo 4.5 (Escalonamento Humano)**: A qualquer momento ou em situações complexas (como análise cadastral de pessoas jurídicas), o usuário clica em `"Falar com Consultor Humano"` para transferir a conversa para a equipe da Performa Energy via WhatsApp ou telefone.

### D. Microinterações no Figma
- **Digitação da IA**: Antes da exibição da resposta da Lia, três pontos animados com efeito de onda (*Typing Indicator*) oscilam em loop durante 600ms.
- **Clique nos Chips**: Ao clicar em um chip de sugestão, o chip recebe transição *Smart Animate*, desaparece da barra e aparece como bolha enviada pelo usuário no topo da pilha de mensagens.
- **Clique na Fonte Regulatória**: *On Click* na tag da ANEEL → Exibe pop-up explicativo com resumo do artigo citado em linguagem acessível.

### E. Lógica Técnica e Governança Anti-Alucinação
- **Arquitetura RAG (Retrieval-Augmented Generation) Parametrizada**: No design do produto, o modelo de linguagem da Lia opera estritamente conectado a uma base de conhecimento fechada contendo o marco legal da Lei 14.300/2022, as resoluções da ANEEL e os termos comerciais da Performa Energy.
- **Detecção de Riscos e Bloqueio de Prompts Tóxicos**: Se o usuário solicitar assessoria jurídica litigiosa contra a concessionária ou conselhos financeiros arriscados, a IA aciona o protocolo de segurança ética: *"Essa questão envolve aconselhamento específico. Para sua segurança jurídica, recomendo conversar diretamente com nosso time de especialistas humanos."*

---

## 4.5. Fluxo 5: Painel de Impacto ESG / ODS e Central de Soberania do Titular LGPD

### A. Objetivo Operacional
Apresentar de forma transparente o impacto ecológico decorrente da adesão à energia solar (mitigação climática sob os ODS 7 e 13) e assegurar os direitos fundamentais do titular de dados previstos no Artigo 18 da LGPD (confirmação de tratamento, acesso, portabilidade e eliminação permanente).

### B. Wireframe Textual Estruturado (ASCII Layout — Desktop 1440x900px)

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ [LOGO: PERFORMA ENERGY]     Impacto ESG & Sustentabilidade     Privacidade & LGPD     [Sair]     │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                  │
│   ┌──────────────────────────────────────────────────────────────────────────────────────────┐   │
│   │ PAINEL DE IMPACTO AMBIENTAL (ALINHAMENTO ODS 13 & ODS 7)                                 │   │
│   │ Com a substituição da energia fóssil pela sua cota solar de 550 kWh/mês na Performa:     │   │
│   └──────────────────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                                  │
│   ┌───────────────────────────┐ ┌───────────────────────────┐ ┌──────────────────────────────┐ │
│   │ 🍃 CO2 EVITADO NO ANO     │ │ 🌳 EQUIVALÊNCIA FLORESTAL │ │ ☀️ GERAÇÃO LIMPA ACUMULADA   │ │
│   │ 1,84 Toneladas de CO2     │ │ 12 Árvores Adultas        │ │ 6.600 kWh / ano              │ │
│   │ Mitigação direta do efeito│ │ Preservadas e mantendo a  │ │ Produzidos sem emissão de    │ │
│   │ estufa (GHG Protocol)     │ │ captura de carbono ativa  │ │ poluentes atmosféricos       │ │
│   └───────────────────────────┘ └───────────────────────────┘ └──────────────────────────────┘ │
│                                                                                                  │
│   ┌──────────────────────────────────────────────────────────────────────────────────────────┐   │
│   │ CENTRAL DE GOVERNANÇA DE DADOS & DIREITOS DO TITULAR (ARTIGO 18 DA LGPD)                 │   │
│   │ Em respeito à sua privacidade, você tem controle soberano sobre suas informações:        │   │
│   │                                                                                          │   │
│   │ • Identificador Anônimo de Sessão: anon_session_4f92c10b7a8d                             │   │
│   │ • Status dos Dados: Fatura temporária mantida em cache seguro e isolado.                 │   │
│   │ • Nível de Risco Algorítmico: Nulo (Modelos sem viés socioeconômico discriminatório).    │   │
│   │                                                                                          │   │
│   │ ┌──────────────────────────────────────┐  ┌───────────────────────────────────────────┐  │   │
│   │ │ [📥] BAIXAR EXTRATO DE DADOS (JSON)  │  │ [🗑️] EXCLUIR DEFINITIVAMENTE MEUS DADOS   │  │   │
│   │ └──────────────────────────────────────┘  └───────────────────────────────────────────┘  │   │
│   │                                                                                          │   │
│   │ [✓] Garantia de Não Discriminação: A Performa Energy não realiza credit scoring opaco   │   │
│   │     ou exclusão territorial (Conforme diretrizes éticas contra ADMs - Cathy O'Neil).     │   │
│   └──────────────────────────────────────────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### C. Passo a Passo do Usuário
1. **Passo 5.1 (Acesso ao Painel ESG)**: O usuário clica na aba `"Governança & ESG"` do menu de topo.
2. **Passo 5.2 (Avaliação do Impacto Climático)**: Visualiza métricas tangíveis de sustentabilidade: quantidade de dióxido de carbono mitigada na atmosfera por ano e número de árvores equivalentes.
3. **Passo 5.3 (Exercício do Direito de Acesso e Portabilidade)**: O usuário clica no botão `"[📥] BAIXAR EXTRATO DE DADOS"` e obtém imediatamente um arquivo consolidado (em formato JSON ou PDF) contendo todos os dados técnicos extraídos de sua fatura.
4. **Passo 5.4 (Exercício do Direito de Eliminação - Art. 18, VI)**: Se o usuário desejar cancelar a simulação sem deixar rastros digitais, clica em `"[🗑️] EXCLUIR DEFINITIVAMENTE MEUS DADOS"`.
5. **Passo 5.5 (Confirmação de Expurgo Seguro)**: Um modal de confirmação é exibido. Ao confirmar, o sistema purga a fatura e os registros de cache do servidor e exibe uma notificação de sucesso: *"Seus dados foram expurgados com sucesso dos nossos servidores."*

### D. Microinterações no Figma
- **Download de Dados**: *On Click* no botão de download → O ícone de download gira 360º, exibe um check verde temporário e abre a simulação de download do relatório.
- **Modal de Exclusão de Dados**: *On Click* no botão de exclusão → Dispara *Open Overlay* com aviso em vermelho e botão `"Sim, expurgar todos os meus dados"`. Ao confirmar, a tela faz um *fade-out* suave e retorna para a Landing Page (Fluxo 1) limpa.

### E. Lógica Técnica e Fórmulas de Impacto Ambiental
1. **Fator de Emissão Médio do Sistema Interligado Nacional (SIN - MCTI)**:
   $$\text{Fator Médio SIN} = 0{,}075 \text{ kg CO}_2 / \text{kWh}$$
   Para fins de substituição na ponta de termoelétricas em períodos secos, adota-se o fator de despacho marginal de $0{,}278 \text{ kg CO}_2 / \text{kWh}$ (padrão GHG Protocol Brasil).
2. **Cálculo de CO2 Evitado ($\text{CO}_{2\text{evitado}}$)**:
   $$\text{CO}_{2\text{evitado}} = C_{\text{solar\_anual}} \times 0{,}278 \text{ kg}$$
   *Exemplo*: $6.600 \text{ kWh/ano} \times 0{,}278 \text{ kg} = 1.834{,}8 \text{ kg} \approx 1{,}84 \text{ toneladas de CO}_2/\text{ano}$.
3. **Equivalência em Árvores Adultas Preservadas**:
   Sabendo-se que uma árvore nativa da Mata Atlântica/Cerrado absorve em média $150 \text{ kg de CO}_2$ ao longo de sua fase de crescimento (20 a 30 anos), calcula-se:
   $$\text{Árvores Equivalentes} = \frac{\text{CO}_{2\text{evitado}}}{150 \text{ kg}} \approx \frac{1.834{,}8}{150} \approx 12{,}2 \text{ árvores}.$$

---

# 5. ESTRUTURA DE FRAMES E NOMENCLATURA DE LAYERS NO FIGMA

Para que o aluno monte o arquivo `.fig` com máxima facilidade, sem hesitações de layout e em conformidade estrita com os padrões profissionais da indústria, define-se a seguinte estrutura canônica de páginas e camadas:

## 5.1. Organização das Páginas do Arquivo `.fig`

```
📁 APEX V - Performa Solar IA (Arquivo Figma)
├── 📄 00. Cover & Documentação (Identificação Acadêmica, Aluno, Unyleya e Performa Energy)
├── 📄 01. Design System & Tokens (Cores Hex, Tipografia Inter, Grid 8pt, Efeitos de Sombra)
├── 📄 02. Componentes & UI Kit (Buttons, Dropzone, Cards, Modais, Inputs, Bounding Boxes, Chat)
├── 📄 03. Telas Desktop (1440x900px) — Os 5 Fluxos Principais
├── 📄 04. Telas Mobile (390x844px) — Versões Responsivas dos 5 Fluxos
└── 📄 05. Protótipo Interativo & Microinterações (Conexões Prototype e Animações)
```

---

## 5.2. Padrão de Nomenclatura Semântica de Camadas

A nomenclatura de frames e camadas deve adotar o padrão semântico hierárquico (Kebab-case / Pascal-case):

```
Desktop/01-Landing-Onboarding
├── Header/Global-Nav
│   ├── Logo/Performa-Energy-Color
│   ├── Nav/Links-Group (Simulador, ODS, Privacidade)
│   └── Button/Nav-CTA ("Entrar")
├── Hero/Section-Main
│   ├── Badge/ODS-Alignment (ODS 7, 9 e 13)
│   ├── Typography/Hero-Title-H1 ("Economize até 20%...")
│   ├── Typography/Hero-Subtitle-Large
│   └── Actions/CTA-Group
│       ├── Button/Primary/Solar-Gold ("SIMULAR ECONOMIA AGORA")
│       └── Button/Secondary/Outline ("Como a IA Protege seus Dados")
└── Overlay/Modal-LGPD-Consent
    ├── Scrim/Backdrop-Blur-8px
    └── Container/Modal-Window
        ├── Header/Icon-Shield-Lock
        ├── Text/Modal-Title-H3 ("Termo de Privacidade & Tratamento")
        ├── Form/Checkboxes-Group (Finalidade, Minimização, Revogabilidade)
        └── Actions/Buttons-Group ("Cancelar", "Concordar e Avançar")

Desktop/02-Upload-OCR-Review
├── Header/Step-Indicator (Etapa 2 de 3: Leitura de Fatura)
├── Container/Dropzone-Upload-Active
│   ├── Icon/Cloud-Upload-48px
│   ├── Label/Dropzone-Title
│   └── Badge/LGPD-Encryption-Security
└── View/Split-Screen-HITL
    ├── Column-Left/Fatura-Viewer
    │   ├── Image/Fatura-CEMIG-Preview
    │   ├── Box/Bounding-Box-Consumo (Verde translúcido + Tag)
    │   └── Box/Bounding-Box-Tarifa
    └── Column-Right/Review-Form
        ├── Field/Input-Concessionaria (CEMIG)
        ├── Field/Input-Consumo-kWh (650 kWh • 99.4%)
        ├── Field/Input-Valor-Total (R$ 684,20)
        └── Button/Primary/Confirm-Proceed ("CONFIRMAR E CALCULAR")

Desktop/03-Simulator-Dashboard
├── Summary/Bar-Selected-Data
├── Metrics/Grid-Cards-3Cols
│   ├── Card/Metric-Monthly-Savings (R$ 102,60/mês)
│   ├── Card/Metric-Annual-Savings (R$ 1.231,20/ano)
│   └── Card/Metric-Solar-Credits (550 kWh/mês)
├── Visualization/Chart-Comparison-Current-vs-Solar
├── Interactive/Slider-Consumption-Adjust
└── Drawer/XAI-Explainable-AI
    ├── Header/Drawer-Title ("Memória Analítica de Cálculo")
    ├── Math/Formula-Breakdown-Step-by-Step
    └── Button/Close-Drawer

Desktop/04-Lia-Chatbot-Modal
├── Chat/Container-Window
│   ├── Header/Avatar-Lia-Online
│   ├── Chat/Scroll-Area
│   │   ├── Bubble/Lia-Greeting
│   │   ├── Bubble/User-Question
│   │   ├── Bubble/Lia-Regulatory-Answer
│   │   └── Tag/Legal-Citation (ANEEL RN 1.000/21)
│   ├── Chips/Quick-Suggestions-Row
│   └── Input/Message-Bar-With-Send-Button

Desktop/05-LGPD-Ethics-Center
├── Section/ESG-Metrics-Display (CO2 evitado e Árvores)
├── Section/Data-Subject-Rights-Art18
│   ├── Text/Session-ID-Token
│   └── Actions/Rights-Buttons
│       ├── Button/Download-Data-JSON
│       └── Button/Delete-Data-Permanent
└── Section/Non-Discrimination-Seal
```

---

## 5.3. Guia Prático de Montagem no Figma Desktop / Web

Para o discente executar a criação das telas sem qualquer dificuldade técnica:
1. **Passo 1 — Configuração Inicial**: Abrir o Figma (Web ou Desktop), criar novo arquivo de design e renomear para `APEX V - Performa Solar IA - Protótipo Final`.
2. **Passo 2 — Criação dos Estilos Globais**:
   - Vá ao painel direito (*Local Styles*).
   - Crie as cores do Design System: `Solar-Gold` (`#F59E0B`), `Clean-Green` (`#10B981`), `Slate-900` (`#0F172A`), `Slate-50` (`#F8FAFC`), etc.
   - Crie os estilos de texto da família `Inter`: `H1/Display` (36px Bold), `H2/Section` (28px Semi-Bold), `Body/Medium` (14px Regular), `Value/Big` (32px Bold).
3. **Passo 3 — Montagem dos Componentes Mestres**: Na página `02. Componentes & UI Kit`, crie os botões com Auto Layout (`Shift + A`), crie as variantes de estado (`Default`, `Hover`, `Pressed`) e monte os cards de métricas.
4. **Passo 4 — Construção dos 5 Frames Desktop**: Crie 5 frames na resolução 1440x900px, aplique o grid de 12 colunas (margem 80px, gutter 24px) e posicione os componentes seguindo os wireframes textuais da Seção 4.
5. **Passo 5 — Configuração das Conexões no Modo Prototype**:
   - Conecte o botão `"SIMULAR ECONOMIA AGORA"` da Landing Page ao frame `02-Upload-OCR-Review` utilizando o modal intermediário como *Open Overlay*.
   - Conecte o botão `"CONFIRMAR E CALCULAR"` ao frame `03-Simulator-Dashboard`.
   - Conecte o link `"Ver Memória de Cálculo"` para abrir o frame `Drawer/XAI` com transição *Slide In Right*.
   - Conecte o ícone da Lia para abrir o chat flutuante.
6. **Passo 6 — Teste de Apresentação**: Pressione o botão `Play` (ícone triangular no topo direito) para validar todas as rotas e animações no modo de exibição.

---

# 6. DIRETRIZES DE INTEGRAÇÃO ACADÊMICA: MÓDULOS 3 E 4 DA APEX V

A presente especificação foi arquitetada para viabilizar o cumprimento perfeito de todas as exigências acadêmicas do cronograma da disciplina APEX V (Faculdade Unyleya):

## 6.1. Módulo 3: Certificação iTalents e Inserção nos Slides 14 e 15 do PPTX

- **Exigência do Módulo 3 (até 10 pontos)**:
  1. Conclusão do curso institucional de Figma na plataforma **iTalents** (parceira da Unyleya) e emissão do certificado em nome do discente.
  2. Envio do arquivo PPTX com a Etapa 3 preenchida (Slides 12 até 19).
- **Diretriz para os Slides 14 e 15 do Template PPTX**:
  - *No Slide 14*: Inserir capturas de tela (*screenshots*) em alta resolução da **Landing Page (Fluxo 1)** e da **Tela de OCR com Split View e Bounding Boxes (Fluxo 2)**. Inserir em caixa de texto destacada o link público de compartilhamento gerado no Figma (`Share prototype` com permissão *"Anyone with the link can view"*).
  - *No Slide 15*: Inserir capturas de tela do **Dashboard de Economia com o Drawer XAI aberto (Fluxo 3)**, do **Assistente Virtual Lia (Fluxo 4)** e do **Painel ESG/LGPD (Fluxo 5)**, acompanhadas das instruções de navegação para a banca avaliadora.

---

## 6.2. Módulo 4 (Item 1 — até 20 pontos): Critérios de Avaliação do Protótipo Figma

Para garantir a pontuação máxima de 20 pontos no Item 1 do Módulo 4, o protótipo deve atender aos seguintes critérios de inspeção da banca:
1. **Navegabilidade Real e Ausência de Telas Quebradas**: Todos os 5 fluxos devem permitir caminho de ida e volta (*happy path* completo).
2. **Design System Audível**: Uso consistente de variáveis cromáticas acessíveis (WCAG AAA), tipografia escalonada e componentes reutilizáveis.
3. **Explicabilidade da IA (XAI)**: Presença evidente da gaveta de transparência matemática e das bounding boxes de leitura da fatura.
4. **Alinhamento com o Tema Gerador**: O protótipo demonstra com perfeição o papel da IA no letramento cidadão, desmistificando o setor de energia solar e protegendo dados pessoais (LGPD).

---

## 6.3. Módulo 4 (Item 2 — até 50 pontos): Protocolo da Apresentação Presencial e Checklist das 3 Fotos

O Item 2 do Módulo 4 corresponde à metade da nota total da disciplina (50 pontos). A comprovação exige a realização de um workshop presencial na sede da **Performa Energy** e a submissão irrefutável do painel fotográfico no Slide 16 do template PPTX:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                          TRIPÉ DE EVIDÊNCIAS FOTOGRÁFICAS (50 PONTOS - MÓDULO 4)                 │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│  [ FOTO 1: AMBIENTE CORPORATIVO & COMUNIDADE REUNIDA ]                                           │
│  • Enquadramento: Plano Geral Aberto (Wide Shot) mostrando a sala de reunião da Performa Energy. │
│  • Elementos em Cena: O estudante de pé, colaboradores acomodados assistindo à apresentação,     │
│    tela da Smart TV/projetor exibindo o slide institucional com logo Unyleya e Performa Energy. │
│  • O que comprova: Que a atividade ocorreu presencialmente no local físico institucional.        │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│  [ FOTO 2: MEDIAÇÃO PEDAGÓGICA & DEMONSTRAÇÃO DO PROTÓTIPO FIGMA ]                               │
│  • Enquadramento: Plano Médio (Medium Shot) focado no apresentador e nos colaboradores.          │
│  • Elementos em Cena: Tela do notebook ou monitor exibindo nitidamente o protótipo do Figma     │
│    (ex.: tela do Split View com OCR ou Dashboard de Créditos), estudante apontando para a        │
│    interface e colaboradores interagindo ativamente com o sistema.                              │
│  • O que comprova: A transposição do conhecimento tecnológico através do produto digital.       │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│  [ FOTO 3: COLETA PARTICIPATIVA DA AVALIAÇÃO DA COMUNIDADE ]                                     │
│  • Enquadramento: Plano Médio-Aproximado / Detalhe contextualizado da mesa de conferência.      │
│  • Elementos em Cena: Colaboradores da Performa Energy com caneta em punho preenchendo a ficha   │
│    impressa de avaliação (escala Likert) ou utilizando o formulário digital nos celulares.      │
│  • O que comprova: A avaliação formal da comunidade atendida e a devolutiva social da extensão.  │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

# 7. REFERÊNCIAS NORMATIVAS E BIBLIOGRÁFICAS (ABNT NBR 6023)

1. AGÊNCIA NACIONAL DE ENERGIA ELÉTRICA (Brasil). **Resolução Normativa ANEEL nº 1.000, de 7 de dezembro de 2021**. Estabelece as Regras de Prestação do Serviço Público de Distribuição de Energia Elétrica. *Diário Oficial da União*: seção 1, Brasília, DF, ano 159, n. 238, p. 102-145, 20 dez. 2021.
2. BRASIL. Ministério da Ciência, Tecnologia e Inovações. **Estratégia Brasileira de Inteligência Artificial (EBIA)**. Brasília, DF: MCTI, 2021. 76 p.
3. BRASIL. Ministério da Educação. Conselho Nacional de Educação. Câmara de Educação Superior. **Resolução nº 7, de 18 de dezembro de 2018**. Estabelece as Diretrizes para a Extensão na Educação Superior Brasileira e regimenta as disposições do PNE 2014-2024. *Diário Oficial da União*: seção 1, Brasília, DF, n. 243, p. 49-50, 19 dez. 2018.
4. BRASIL. Presidência da República. **Lei nº 13.709, de 14 de agosto de 2018**. Lei Geral de Proteção de Dados Pessoais (LGPD). *Diário Oficial da União*: seção 1, Brasília, DF, ano 155, n. 157, p. 59-64, 15 ago. 2018.
5. BRASIL. Presidência da República. **Lei nº 14.300, de 6 de janeiro de 2022**. Institui o marco legal da microgeração e minigeração distribuída, o Sistema de Compensação de Energia Elétrica (SCEE) e o Programa de Energia Renovável Social (PERS). *Diário Oficial da União*: seção 1, Brasília, DF, ano 159, n. 5, p. 1-6, 7 jan. 2022.
6. FLORIDI, Luciano. **The ethics of artificial intelligence**: principles, challenges, and opportunities. Oxford: Oxford University Press, 2023. 272 p.
7. KNOWLES, Malcolm S.; HOLTON III, Elwood F.; SWANSON, Richard A. **Aprendizagem de resultados**: uma abordagem prática para aumentar a efetividade da educação corporativa. Rio de Janeiro: Elsevier, 2009. 336 p.
8. NIELSEN, Jakob. **Usability engineering**. Boston: Academic Press, 1994. 362 p.
9. O'NEIL, Cathy. **Armas de destruição matemática**: como o big data aumenta a desigualdade e ameaça a democracia. Tradução de Rafael Abraham. Santo André: Editora Rua do Sabão, 2020. 336 p.
10. ORGANIZAÇÃO DAS NAÇÕES UNIDAS. **Transformando nosso mundo: a Agenda 2030 para o Desenvolvimento Sustentável**. Nova York: ONU, 2015.
11. RUSSELL, Stuart; NORVIG, Peter. **Inteligência artificial**: uma abordagem moderna. 4. ed. Rio de Janeiro: GEN LTC, 2022. 1152 p.
12. UNESCO. **Recomendação sobre a ética da inteligência artificial**. Paris: UNESCO, 2022. 44 p.
13. W3C. **Web Content Accessibility Guidelines (WCAG) 2.1**: W3C Recommendation. World Wide Web Consortium, 2018. Disponível em: https://www.w3.org/TR/WCAG21/.
14. ZUBOFF, Shoshana. **A era do capitalismo de vigilância**: a luta por um futuro humano na nova fronteira do poder. Rio de Janeiro: Intrínseca, 2020. 800 p.

---
*Fim do Documento de Especificação Técnica — Performa Solar IA / APEX V*
