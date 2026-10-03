# Project: APEX V — Performa Energy (TI / Unyleya)

## Architecture
O projeto de extensão universitária APEX V estrutura-se na integração entre a formação cidadã do estudante de TI, a aplicação de Inteligência Artificial generativa e preditiva no setor de energia solar, e a entrega de valor real à comunidade corporativa da **Performa Energy** (gestora de créditos de energia solar).

### Mapeamento dos Módulos Acadêmicos (1 a 4) e Pontuação (100 pts)
- **Módulo 1 (até 10 pts)**: Etapa 1 do Template Padrão (Slides 2 a 6) — Identificação, ODS (7, 9 e 13) e Local de Implementação (Performa Energy).
- **Módulo 2 (até 10 pts)**: Etapa 2 do Template Padrão (Slides 8 a 10) — Participantes (cargos anônimos) e Desafio/Questão-Problema (leitura de faturas, LGPD, opacidade algorítmica e IA ética).
- **Módulo 3 (até 10 pts)**: Etapa 3 do Template Padrão (Slides 12 a 20) — Planejamento andragógico, material educativo digital, autoavaliação nas 5 dimensões, avaliação da comunidade e referências ABNT NBR 6023 + Certificação iTalents Figma.
- **Módulo 4 (até 70 pts)**:
  * Link da atividade de extensão / protótipo Figma + Certificado iTalents (até 20 pts).
  * Apresentação presencial na Performa Energy com registro estrito de 3 fotos obrigatórias (até 50 pts).

---

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | Preenchimento Etapa 1 (Slides 2-6) | Identificação, ODS 7, 9 e 13, Ementa oficial e Apresentação da Performa Energy | M1 | Survey (PDFs/Slides) |
| 2 | Preenchimento Etapa 2 (Slides 8-10) | Participantes (cargos corporativos), Diagnóstico de IA na Performa Energy, ADMs e Ética | M1 | Survey (PDFs/Slides) |
| 3 | Preenchimento Etapa 3 (Slides 12-20) | Plano pedagógico/andragógico, Material educativo, Autoavaliação (5 dimensões), Avaliação da comunidade e Referências ABNT | M1 | Survey (PDFs/Slides) |
| 4 | Geração do Arquivo PPTX Preenchido | Criação física do PPTX preenchido baseado no template oficial | M1 | Survey & Requisitos R1 |
| 5 | Documento Completo dos Slides (.md) | Registro integral e editável de todos os textos slide a slide para conferência | M1 | Survey & Requisitos R1 |
| 6 | Arquitetura de Informação & Fluxos Figma | Mapa de telas (L1-L3), taxonomia e 5 fluxos do protótipo Performa Solar IA | M2 | Survey & Requisitos R2 |
| 7 | Design System & Telas Detalhadas Figma | Tokens de cor WCAG AAA, tipografia, componentes UI e especificações de tela | M2 | Survey & Requisitos R2 |
| 8 | Roteiro de Apresentação Presencial (90 min) | Estrutura em 5 blocos para workshop corporativo na sede da Performa Energy | M3 | Survey & Requisitos R3 |
| 9 | Protocolo Rigoroso das 3 Fotos Obrigatórias | Checklist visual e especificações para as 3 fotos da avaliação de 50 pontos | M3 | Survey & Requisitos R3 |
| 10 | Instrumentos de Avaliação e Declaração | Questionário Likert de avaliação da comunidade e Termo/Declaração Institucional da empresa | M3 | Survey & Requisitos R3 |
| 11 | Validação E2E, Review, Challenge & Auditoria | Testes de conformidade das entregas, desafio empírico e auditoria forense sem hardcodes | M4 | Critérios Institucionais |

---

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Template PPTX Preenchido (R1) | Elaborar os textos dos 20 slides e gerar o arquivo PPTX preenchido e documento consolidado | Survey | PLANNED |
| M2 | Especificação do Protótipo Figma (R2) | Especificação técnica completa do Performa Solar IA (arquitetura, 5 fluxos, design system, telas) | Survey | PLANNED |
| M3 | Guia Presencial & Protocolo 3 Fotos (R3) | Roteiro presencial, checklist fotográfico de 50 pts, questionário e declaração empresarial | Survey | PLANNED |
| M4 | Verificação E2E, Review & Auditoria | Revisão acadêmica, desafio empírico e auditoria forense de integridade | M1, M2, M3 | PLANNED |

---

## Interface Contracts
### Survey ↔ Milestone Workers
- **Entrada para M1**: Matriz de slides de `teamwork_preview_explorer_survey_2/handoff.md` + placeholders de `pptx_full_dump.txt` + template original `TEMPLATE PADRÃO PARA DESENVOLVIMENTO DOS TRABALHOS DE EXTENSÃO _ POR ETAPAS-1 (1).pptx`.
- **Entrada para M2**: Especificação de arquitetura, fluxos e design system de `teamwork_preview_explorer_survey_3/handoff.md`.
- **Entrada para M3**: Roteiro de 5 blocos, protocolo fotográfico e instrumentos de avaliação de `teamwork_preview_explorer_survey_3/handoff.md`.
- **Entrada para M4**: Artefatos finais gerados por M1, M2 e M3 inspecionados por Reviewer, Challenger e Forensic Auditor.

---

## Code Layout
Os arquivos de entrega serão gerados exclusivamente na raiz do projeto (`c:\Users\rafas\Documents\performa\trabalho`):
- `c:\Users\rafas\Documents\performa\trabalho\TEMPLATE_PREENCHIDO_APEX_V_PERFORMA_ENERGY.pptx` (Arquivo PPTX pronto para submissão nos Módulos 1, 2 e 3)
- `c:\Users\rafas\Documents\performa\trabalho\DOCUMENTO_ENTREGA_SLIDES_APEX_V_PERFORMA_ENERGY.md` (Documento acadêmico com todos os slides formatados e prontos para inserção)
- `c:\Users\rafas\Documents\performa\trabalho\ESPECIFICACAO_PRODUTO_FIGMA_PERFORMA_SOLAR_IA.md` (Especificação completa do protótipo Figma para o Módulo 3 e 4)
- `c:\Users\rafas\Documents\performa\trabalho\GUIA_APRESENTACAO_PRESENCIAL_E_FOTOS_PERFORMA_ENERGY.md` (Guia presencial de 50 pontos, roteiro, protocolo das 3 fotos, questionário e declaração)
- `c:\Users\rafas\Documents\performa\trabalho\RELATORIO_CONSOLIDADO_FINAL_APEX_V.md` (Dossiê executivo e acadêmico completo do projeto)
