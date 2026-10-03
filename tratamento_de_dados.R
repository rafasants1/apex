dados <- data.frame(
  nomes = c("AdriAn","Aloi1sio","Camila","Cristiano4","Denise","Douglas",
            "EdnA","Fabio","Flavio","Frederico","Gabriel1","GlaUra4"),
  idade = c(19, 22, 25, 31, 28, 21, 35, 24, 19, 42, 27, 33),
  horas_estudo = c(2, 5, 8, 3, 6, 10, 1, 7, 4, 2, 9, 5),
  nota = c(55, 70, 88, 61, 79, 94, 48, 85, 67, 52, 91, 74),
  curso = c("A", "B", "A", "C", "B", "A",
            "C", "B", "C", "A", "B", "C")
)

dados$tempo_estudo <- ifelse(dados$horas_estudo >= 6, "Muito", "Pouco")

dados$desempenho <- ifelse(dados$nota >= 70, "Bom", "Regular")

dados$faixa_idade <- cut(
  dados$idade,
  breaks = c(0, 25, 36, Inf),
  labels = c("Jovem", "Adulto", "Mais de 35"),
  right = FALSE
)

dados$curso <- factor(
  dados$curso,
  levels = c("A", "B", "C"),
  labels = c("Estatistica", "Economia", "Computacao")
)

dados$curso <- relevel(dados$curso, ref = "Economia")

data(faithful)

head(faithful)
str(faithful)
summary(faithful)

faithful$eruptions.cat <- ifelse(faithful$eruptions > 3, "longas", "curtas")

recode_grupos <- c("longas" = "Grupo 1", "curtas" = "Grupo 2")
faithful$eruptions.cat <- recode_grupos[faithful$eruptions.cat]
