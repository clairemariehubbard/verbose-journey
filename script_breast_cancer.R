# importamos los datos
data <- read.csv('breastcancer.csv')

# dibujamos un grafico sencillo
hist(data$radius_mean)

# guardamos grafico como png
dev.copy(png, "grafico.png")
dev.off()