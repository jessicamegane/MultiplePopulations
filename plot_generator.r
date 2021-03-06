"""
Rscript to generate a file with the fitness average and std of the runs
and a plot to see the evolution during the generations.
"""

library(ggplot2)

l = list.dirs("save/B/dataset2/", recursive = FALSE)
# print(l)
for (folder in l) {
    jpeg(paste(folder,"plot.jpg",sep="/"))
    D = read.csv(paste(folder,"best.txt", sep="/"), header=TRUE)
    ag <- aggregate(. ~ D$generation, D, function(x) c(Mean = mean(x), SD = sd(x)))
    write.table(ag$fitness, paste(folder,"best_data.txt", sep="/"),col.names = F)
    P1 = read.table(paste(folder,"best_data.txt", sep="/"), header = TRUE)
    
    # COMMENT THIS IF IS NOT METHOD 2
    D2 = read.csv(paste(folder,"best2.txt", sep="/"), header=TRUE)
    ag <- aggregate(. ~ D2$generation, D2, function(x) c(Mean = mean(x), SD = sd(x)))
    write.table(ag$fitness, paste(folder,"best2_data.txt", sep="/"),col.names = F)
    P2 = read.table(paste(folder,"best2_data.txt", sep="/"), header = TRUE)


    print(ggplot() + 
    # COMMENT THIS IF IS NOT METHOD 2
    geom_line(aes(x = P2[,1], y = P2[,2], color="P2")) + 
    geom_ribbon(P2, mapping = aes(x=P2[,1], ymax = P2[,2] + P2[,3], ymin= P2[,2] - P2[,3]), fill="skyblue2", alpha=0.3) + 
    # COMMENT UNTIL HERE
    geom_line(aes(x = P1[,1], y = P1[,2], color = "P1")) + 
    geom_ribbon(P1, mapping = aes(x=P1[,1], ymax = P1[,2] + P1[,3], ymin= P1[,2] - P1[,3]), fill="sienna2", alpha=0.3) + 
    scale_color_manual("", values = c("sienna2", "skyblue2")) +
    theme_minimal() +
    theme(legend.position="top") +
    scale_x_continuous(breaks = seq(0, 99, 10)) +
    ylim(700,950) +
    labs(x = "Generations", y = "Fitness"))
}