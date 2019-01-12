# Title     : DecisionTreeClassifier
# Objective : to Evalue the model
# Created by: Arwa
# Created on: 12/4/2018

# loading from R
xx<-data(iris)

# loading from PC
myData<-read.csv("/Users/reem/Desktop/iris.csv")

# loading from URL
library(curl)
urlfile<-'https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'
test <-read.csv(curl(urlfile))
