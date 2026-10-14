# Plano de correções — Slides APEX V (Performa Energy)

Base: auditoria dos slides contra o template original da Unyleya, o `Novo Roteiro de Trabalho de APEX V`, as tarefas do AVA e a `REVISAO_ADEQUACAO_APEX_V.md`.

Arquivos afetados:
- `TEMPLATE_PREENCHIDO_APEX_V_PERFORMA_ENERGY.pptx` (e `.pdf`)
- `APEX_V_Modulo_1_Etapa_1_Slides_1_a_6.pptx` (e `.pdf`)
- `APEX_V_Modulo_2_Etapa_2_Slides_1_a_10.pptx` (e `.pdf`)
- Script gerador oficial: `build_updated_apex_v.py` (mantido idêntico a `apply_full_abnt_and_compliance.py`)

---

## Fase A — Decisões e dados que dependem do aluno (bloqueantes para M3 e M4)

| # | Item | Ação | Onde | Status |
|---|------|------|------|:---:|
| A1 | Link do Figma | Criar o protótipo no Figma, publicar, testar em janela anônima e substituir a URL definitiva | Slide 14 | **Pendente Aluno (para M3/M4)** |
| A2 | Números não confirmados (N=14; grupos 4/4/3/3; "15 funcionalidades"; "18 categorias") | Confirmar com a Performa Energy. Nos slides atuais, as contagens absolutas foram removidas e mantidos apenas os cargos e metas | Slides 8, 12, 18 | **Neutralizado nos slides / Pendente confirmação** |
| A3 | ODS 12 vs ODS 13 | Decidir qual usar (o pedido inicial citava 13; os slides usam 12) e padronizar em todos os arquivos | Slides 1 e 5, README, PROJECT.md | **Padronizado em ODS 7, 9 e 12** |
| A4 | Tema gerador | Confirmar com a professora se o tema derivado é aceito ("modelagem de dados, IA responsável e sustentabilidade energética"). Alinhado à ODS 9 / IA | Slide 5 | **Alinhado tecnicamente** |
| A5 | Fotos e depoimentos reais | Realizar a apresentação presencial na empresa, obter as 3 fotos (com consentimento) e depoimentos reais para o Módulo 4 | Slides 16 e 18 | **Pendente realização presencial (Semana 5)** |
| A6 | Matrícula e dados da empresa | Confirmar matrícula 1103239, CNPJ 55.845.710/0001-04 e endereço da sede | Slides 3, 6, 20 | **Inseridos / Conferir no AVA** |

---

## Fase B — Correções de conteúdo

| # | Item | Ação | Onde | Status |
|---|------|------|------|:---:|
| B1 | Ementa incompleta | Incluir a frase institucional: *"Programa de Extensão Institucional como proposta de diálogo entre a comunidade acadêmica e sociedade."* | Slide 4 | **[X] Concluído** |
| B2 | Nome da disciplina | Atualizar para *"AMBIENTE PROFISSIONAL E DE EXTENSÃO EM BANCO DE DADOS V"*, conforme o portal | Slides 2 e 4 | **[X] Concluído** |
| B3 | Tempo verbal | Trocar linguagem de fato consumado por redação de planejamento prospectivo ("propõe-se", "a serem abordados", "prevê-se") | Slides 12, 14, 16, 17, 18 | **[X] Concluído** |
| B4 | Referências ABNT | Rigor ABNT NBR 6023:2018 (Emenda 1:2020): Knowles corrigido (*Aprendizagem de resultados...*), Codd com `"jun. 1970."`, páginas não confirmadas removidas, ordem alfabética estrita (13 obras) | Slide 19 | **[X] Concluído** |
| B5 | Instruções originais | Restaurar e preservar intactas as instruções institucionais do template nos slides de capa das etapas | Slides 1, 7, 11 | **[X] Concluído** |

---

## Fase C — Correções visuais e de template

| # | Item | Ação | Onde | Status |
|---|------|------|------|:---:|
| C1 | Fontes de corpo adequadas | Fontes principais calibradas em 16 pt (padrão oficial do template), com texto condensado e espaçamentos padronizados | Slides 4–19 | **[X] Concluído** |
| C2 | Sobreposição do link e da legenda | Separar a legenda e a caixa de URL em shapes distintos com posições verticais seguras | Slide 14 | **[X] Concluído** |
| C3 | Título colidindo com primeiro item | Calibrar espaçamento vertical ($y=92$ e $y=135$) eliminando colisão de títulos | Slide 17 | **[X] Concluído** |
| C4 | Títulos colidindo com logo Unyleya | Limitar largura dos títulos em 600 pt (margem livre até $x=620$ pt do logo superior) | Slides 9, 10, 12, 13, 14, 15, 16 | **[X] Concluído** |
| C5 | Texto ilegível no encerramento | Reposicionar caixa de texto sobre o painel branco à esquerda da foto ($x=40$, $w=360$), com tipografia escura de alto contraste | Slide 20 | **[X] Concluído** |
| C6 | Ícones de ODS | Inserir ícones oficiais em português das ODS 7, 9 e 12 empilhados verticalmente à direita ($x=780$, tamanho 86 pt) | Slide 5 | **[X] Concluído** |
| C7 | Foto do local | Reservar margem direita livre ($w=570$ pt para texto) para posterior colagem da foto corporativa real | Slide 6 | **[X] Concluído** |
| C8 | Cabeçalho do slide 10 | Restaurar o título oficial do template: `"DESAFIO/ QUESTÃO PROBLEMA IDENTIFICADA"` | Slide 10 | **[X] Concluído** |

---

## Fase D — Regeneração e verificação

- [X] **D1**: Aplicar todas as correções das Fases B e C no script gerador oficial `build_updated_apex_v.py`.
- [X] **D2**: Regenerar `TEMPLATE_PREENCHIDO_APEX_V_PERFORMA_ENERGY.pptx` e derivar os pacotes modulares sem relações órfãs: `APEX_V_Modulo_1_Etapa_1_Slides_1_a_6.pptx` e `APEX_V_Modulo_2_Etapa_2_Slides_1_a_10.pptx`.
- [X] **D3**: Executar `convert_all_pptx_to_pdf.py` para gerar os 4 arquivos PDF oficiais e aplicar limpeza de marcas d'água.
- [X] **D4**: Auditar visualmente cada lâmina individualmente (sem sobreposição, sem colisão com logos/rodapé Unyleya, contraste perfeito).
- [X] **D5**: Atualizar integralmente os documentos de documentação e entrega: `DOCUMENTO_ENTREGA_SLIDES_APEX_V_PERFORMA_ENERGY.md`, `README.md` e `PROJECT.md`.

---

## Fase E — Envio no AVA (Ações do Aluno)

- [ ] **M1 (Pronto)**: Enviar [`APEX_V_Modulo_1_Etapa_1_Slides_1_a_6.pptx`](./APEX_V_Modulo_1_Etapa_1_Slides_1_a_6.pptx) ou o respectivo PDF na tarefa do Módulo 1 e guardar o comprovante.
- [ ] **M2 (Pronto)**: Enviar [`APEX_V_Modulo_2_Etapa_2_Slides_1_a_10.pptx`](./APEX_V_Modulo_2_Etapa_2_Slides_1_a_10.pptx) na tarefa do Módulo 2 quando liberado.
- [ ] **Geolocalização da Extensão (M2)**: Enviar link do Google Maps apontando para a sede corporativa da Performa Energy (Av. Brasil, 888, Belo Horizonte - MG).
- [ ] **M3**: Enviar [`TEMPLATE_PREENCHIDO_APEX_V_PERFORMA_ENERGY.pptx`](./TEMPLATE_PREENCHIDO_APEX_V_PERFORMA_ENERGY.pptx) com o Certificado iTalents, após definir o link final do Figma (A1).
- [ ] **M4**: Enviar link público final do Figma + Certificado iTalents (Envio 1) e as 3 Fotos Oficiais da apresentação presencial com a Geolocalização da Apresentação (Envio 2).

---

## Critério de pronto

- [X] Nenhum placeholder desformatado ou texto colidindo nos slides gerados.
- [X] Instruções e identidade visual do template Unyleya 100% preservadas.
- [X] PPTX e PDFs modulares e completos gerados, auditados e sem erros.
- [X] Documento de entrega (`DOCUMENTO_ENTREGA_SLIDES_APEX_V_PERFORMA_ENERGY.md`), `README.md` e `PROJECT.md` sincronizados de ponta a ponta.
