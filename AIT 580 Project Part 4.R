# Load necessary libraries

library(dplyr)
library(ggplot2)

# Read the dataset
data <- read.csv("E:/Downloads/George Mason/Employee_Payroll.csv")

head(data)

ggplot(data, aes(x=Job_Title))+
  geom_bar() +
  labs(x = "Job Titles", y = "Count", title = "Count of Job Titles")

ggplot(data, aes(x=Base_Pay))+
  geom_histogram() +
  labs(x = "Base Pay", y = "Frequency", title = "Distribution of Base Pay")

ggplot(data, aes(x=Bureau))+
  geom_bar() +
  labs(x = "Bureau", y = "Count", title = "Frequency of Bureaus")

ggplot(data, aes(x=Fiscal_Year))+
  geom_bar() +
  labs(x = "Fiscal Year", y = "Count", title = "Frequency of Fiscal Years")

ggplot(data, aes(x = Fiscal_Year, y = Base_Pay)) +
  geom_boxplot() +
  labs(title = 'Base Pay vs Fiscal Year',
       x = 'Fiscal Year',
       y = 'Base Pay') +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

top_bureaus <- data %>%
  group_by(Bureau) %>%
  summarize(mean_base_pay = mean(`Base_Pay`, na.rm = TRUE)) %>%
  top_n(10, wt = mean_base_pay) %>%
  pull(Bureau)

# Filter data for top bureaus
data_top_bureaus <- data %>%
  filter(Bureau %in% top_bureaus)

# Create a boxplot
ggplot(data_top_bureaus, aes(x = `Base_Pay`, y = factor(Bureau))) +
  geom_boxplot() +
  labs(title = 'Base Pay vs. Bureau',
       x = 'Base Pay',
       y = 'Bureau') +
  theme_minimal()
  