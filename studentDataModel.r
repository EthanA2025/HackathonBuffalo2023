library(lcmm)

df <- read.csv("student_data.csv")
df$student_id <- as.factor(df$student_id)
gmm_model <- lcmm(gpa ~ time, random = ~ time, subject = 'student_id', 
                  mixture = ~ time, ng = 2, data = df, link = "threshold", 
                  link.mixture = list(link="logit"), idiag = TRUE)

#print the summary of the model
summary(gmm_model)