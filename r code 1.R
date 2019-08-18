library("ggplot2")
my_data<-read.csv(file="feature-table.csv",header = TRUE,sep = ",")
head(my_data)
str(my_data)
rnames<-my_data[,1]
mat_data<-as.matrix(my_data[,-1])
rownames(mat_data)<-rnames
head(mat_data)




names(my_data)[1]<-"feature_id"
head(my_data[1])
heatmap(mat_data)

mine.heatmap <- ggplot(data = mat_data, mapping = aes(x = ,
                                                       y = Class,
                                                       fill = Abundance)) +
  geom_tile() +
  xlab(label = "Sample")


data_subset<-my_data[1:5,2:101]
as.matrix(data_subset)

heatmap(as.matrix(data_subset[,-1]))

event<-c("X2","X13","X15","X19","X26","X39","X57","X65","X72","X82","X87","X88","X96","X109")
event1<-c("X1","X2","X13")

event_data<-mat_data[,which(colnames(mat_data)%in% event)]
head(event_data)

no_event<-mat_data[,-which(colnames(mat_data)%in% event)]

as.matrix(mat_data[1:5,which(colnames(mat_data)%in% event1)])


length(event)
###### filter OUT by abundance 

for (i in 1:100) {
  
  
}
# To loop each column
for (i in 1:ncol(df))
{
  dosomething(df[,i])
}
# To loop each row
for (i in 1:nrow(df))
{
  dosomething(df[i,])
}
