library(tidyverse)
library(readr)
#install.packages("pROC")
library(pROC)
setwd('/Users/Mackdig25/hockey')
PbP2016Data <- read_csv('2016NHLPbP.csv')
PbP2017Data <- read_csv('2017NHLPbP.csv')
TestData <- read_csv('2018NHLPbP.csv')

# train data
Train_PbP_Data <- bind_rows(PbP2016Data,PbP2017Data)
dim(Train_PbP_Data)

# Get Columns
str(Train_PbP_Data, max.level = 1)

# Unique events
unique(Train_PbP_Data$event)

# List of Fenwick Events
fenwick_events <- c('Shot','Missed Shot','Goal')

# Remove the shoutout attempts
Train_PbP_Data<-Train_PbP_Data[Train_PbP_Data$period<5,]
dim(Train_PbP_Data)

# Remove Goalie saves
Train_PbP_Data<-subset(Train_PbP_Data, !(event == "Shot" & playerType == "Goalie"))
dim(Train_PbP_Data)
# Remove Goalie GA
Train_PbP_Data<-subset(Train_PbP_Data, !(event == "Goal" & playerType == "Goalie"))
dim(Train_PbP_Data)
# Remove Assits
Train_PbP_Data<-subset(Train_PbP_Data, !(event == "Goal" & playerType == "Assist"))
dim(Train_PbP_Data)
#Remove faceoff losses
Train_PbP_Data<-subset(Train_PbP_Data, !(event == "Faceoff" & playerType == "Loser"))
dim(Train_PbP_Data)
#Remove Hittee
Train_PbP_Data<-subset(Train_PbP_Data, !(event == "Hit" & playerType == "Hittee"))
dim(Train_PbP_Data)
#Remove Shot Block
Train_PbP_Data<-subset(Train_PbP_Data, !(event == "Blocked Shot" & playerType == "Shooter"))
dim(Train_PbP_Data)
#Remove Penalty Against
Train_PbP_Data<-subset(Train_PbP_Data, !(event == "Penalty" & playerType == "DrewBy"))
dim(Train_PbP_Data)

# Determine if the pbp event is a home
is_home <-function (dataframe){
  dataframe$is_home<-ifelse(dataframe$team_id_for==dataframe$home_team_id,1,0)
  return (dataframe)
}
# Determine if its a goal event or not,
is_goal<-function(dataframe){
  dataframe$is_goal <- ifelse(dataframe$event == "Goal" & dataframe$playerType == "Scorer",
                              1,0)
  return (dataframe)
}

# Add is home column
Train_PbP_Data<-is_home(Train_PbP_Data)
# Add is this a goal
Train_PbP_Data<-is_goal(Train_PbP_Data)

# create a time difference between each event 
# this will be used to determine if the event is a rebound
# For this we add na values for diff if the plays are seperated by period
# Group by period, order by index, is previous row a diff period, populate the difference
Train_PbP_Data<-Train_PbP_Data %>% group_by(game_id) %>%
    arrange(X1,.by_group=TRUE) %>%
           mutate(
             time_diff=ifelse(period != lag(period),
                    NA, 
                         periodTimeRemaining-lag(periodTimeRemaining)))

# drop any resulting NAs                                    
Train_PbP_Data$time_diff[is.na(Train_PbP_Data$time_diff)]<-0
Train_PbP_Data$is_home[is.na(Train_PbP_Data$is_home)]<-0

# determine if an event is a rebound
Train_PbP_Data$is_rebound <- ifelse(Train_PbP_Data$time_diff > -3 &
                                      Train_PbP_Data$event %in% fenwick_events &
                                      Train_PbP_Data$team_id_for==
    lag(Train_PbP_Data$team_id_for),
  1,0)

Train_PbP_Data$is_rebound[is.na(Train_PbP_Data$is_rebound)]<-0

# Determine if the event is off the rush
# This might need to be why we keep the rest of the play by play data
# To determine if a different play happened 25 coordinates away. 
# If we do in fact use the fenwick data, we will need to 
# Drop the receiver of the hit, faceoff, and other plays
# Filter is rebound by fenwick opportunities.
# But it looks like this is only counting fenwick events, 
# but the previous event is important
Train_PbP_Data$is_rush <- ifelse(Train_PbP_Data$time_diff > -4 &
  lag(abs(Train_PbP_Data$x)) < 25 &
  Train_PbP_Data$event %in% fenwick_events,
  1,0)

Train_PbP_Data$is_rebound[is.na(Train_PbP_Data$time_diff)] <- 0

Train_PbP_Data$is_rush[is.na(Train_PbP_Data$is_rush)] <- 0

# We only want fenwick events
Train_Fenwick_Data <- filter(Train_PbP_Data ,event %in% fenwick_events)
# Unique shot types
unique(Train_Fenwick_Data$secondaryType)
# Unique X Coors
unique(Train_Fenwick_Data$x)
# Unique Y Coors
unique(Train_Fenwick_Data$y)
# Unique Strength States
## Need to create this, currently not in the data
#unique(Train_Fenwick_Data$game_strength_state)

# See how many secondary type NAs are there
head(Train_Fenwick_Data[Train_Fenwick_Data$secondaryType == 'NA',], n = 15)
# Remove those 15 values
Train_Fenwick_Data <- filter(Train_Fenwick_Data, !is.na(secondaryType))
head(Train_Fenwick_Data[Train_Fenwick_Data$secondaryType == 'NA',])

# Turn the secondary type into a category
Train_Fenwick_Data$secondaryType<- as.factor(Train_Fenwick_Data$secondaryType)

#Find Range of X
range(Train_Fenwick_Data$x)
# Find the range of y
range(Train_Fenwick_Data$y)
#Drop NAs
Train_Fenwick_Data <- filter(Train_Fenwick_Data, x != 'NA' & y != 'NA') 

#Find Range of X
range(Train_Fenwick_Data$x)
# Find the range of y
range(Train_Fenwick_Data$y)

# Create a new column for each shots angle form goal
## An NHL rink is 200 feet wide by 85 feet across 
## Every vertical up or down is equal to one foot and each x integer is equal to .995 feet. 
## The goal line is 11 feet from the end boards so that is equal to 11.05 in units.
## The coordinate of the center of the goal is (87.95,0).
## Given a shots location determine the angle using the coordinate system. 
## The angle we are to find Theta is equal to Sin(Theta) = Opposite/Hypoteneuse.
## We know the opposite side is equal the y coordinate. 
## The hypoteneuse is the length of using the pythagorean theorem. 
## Answer is in radians in order to get it to degrees we will multiply it by 180 and divide by pi

Train_Fenwick_Data$y <- ifelse(Train_Fenwick_Data$x < 0,
                                      -1 * Train_Fenwick_Data$y, Train_Fenwick_Data$y)

Train_Fenwick_Data$x <- abs(Train_Fenwick_Data$x)


Train_Fenwick_Data$shot_angle <- (asin
                                  (abs
                                    (Train_Fenwick_Data$y)
                                    /sqrt(
                                      (87.95 - 
                                         abs(Train_Fenwick_Data$x))^2
                                      + Train_Fenwick_Data$y^2))*180)/ 3.14

## Shots below the net should result in an angle larger than 90 degrees
## Add 90 degress if the x coor of the shot is greater than x coor of the goal line
Train_Fenwick_Data$shot_angle <- ifelse(abs(Train_Fenwick_Data$x) > 88, 90 + 
                                          (180-(90 + Train_Fenwick_Data$shot_angle)), 
                                        Train_Fenwick_Data$shot_angle)
# New column for distance from goal
## construct the distance from the goal; pythagorean theorem
Train_Fenwick_Data$distance <- sqrt(
  (87.95 - abs(Train_Fenwick_Data$x))^2 + Train_Fenwick_Data$y^2)

# Build Model

xGmodel <- glm(is_goal ~ poly(distance, 3, raw = TRUE) + 
                 poly(shot_angle, 3, raw = TRUE) + secondaryType +
                 is_rebound + is_rush,
               data = Train_Fenwick_Data, 
               family = binomial(link = 'logit'))

save(xGmodel, file = "xGmodelver2.rda")

summary(xGmodel)
coef(xGmodel)


# chi square distribution of the difference in the Null and Residual deviances

1 - pchisq(99068-90332, 163201-163187)


# Testing the model
# Remove the shoutout attempts
TestData<-TestData[TestData$period<5,]
dim(TestData)

# Remove Goalie saves
TestData<-subset(TestData, !(event == "Shot" & playerType == "Goalie"))
dim(TestData)
# Remove Goalie GA
TestData<-subset(TestData, !(event == "Goal" & playerType == "Goalie"))
dim(TestData)
# Remove Assits
TestData<-subset(TestData, !(event == "Goal" & playerType == "Assist"))
dim(TestData)
#Remove faceoff losses
TestData<-subset(TestData, !(event == "Faceoff" & playerType == "Loser"))
dim(TestData)
#Remove Hittee
TestData<-subset(TestData, !(event == "Hit" & playerType == "Hittee"))
dim(TestData)
#Remove Shot Block
TestData<-subset(TestData, !(event == "Blocked Shot" & playerType == "Shooter"))
dim(TestData)
#Remove Penalty Against
TestData<-subset(TestData, !(event == "Penalty" & playerType == "DrewBy"))
dim(TestData)

# Add is home column
TestData<-is_home(TestData)
# Add is this a goal
TestData<-is_goal(TestData)

# create a time difference between each event 
TestData<-TestData %>% group_by(game_id) %>%
  arrange(X1,.by_group=TRUE) %>%
  mutate(
    time_diff=ifelse(period != lag(period),
                     NA, 
                     periodTimeRemaining-lag(periodTimeRemaining)))

# drop any resulting NAs                                    
TestData$time_diff[is.na(TestData$time_diff)]<-0
TestData$is_home[is.na(TestData$is_home)]<-0

# determine if an event is a rebound
TestData$is_rebound <- ifelse(TestData$time_diff > -3 &
                                TestData$event %in% fenwick_events &
                                TestData$team_id_for==
                                      lag(TestData$team_id_for),
                                    1,0)

TestData$is_rebound[is.na(TestData$is_rebound)]<-0

# Determine if the event is off the rush
TestData$is_rush <- ifelse(TestData$time_diff > -4 &
                                   lag(abs(TestData$x)) < 25 &
                             TestData$event %in% fenwick_events,
                                 1,0)

TestData$is_rebound[is.na(TestData$time_diff)] <- 0

TestData$is_rush[is.na(TestData$is_rush)] <- 0

# We only want fenwick events
Test_Fenwick_Data <- filter(TestData ,event %in% fenwick_events)
# Unique shot types
unique(Test_Fenwick_Data$secondaryType)
# Unique X Coors
unique(Test_Fenwick_Data$x)
# Unique Y Coors
unique(Test_Fenwick_Data$y)
# Unique Strength States
## Need to create this, currently not in the data
#unique(Test_Fenwick_Data$game_strength_state)

# See how many secondary type NAs are there
head(Test_Fenwick_Data[Test_Fenwick_Data$secondaryType == 'NA',], n = 15)
# Remove those 15 values
Test_Fenwick_Data <- filter(Test_Fenwick_Data, !is.na(secondaryType))
head(Test_Fenwick_Data[Test_Fenwick_Data$secondaryType == 'NA',])

# Turn the secondary type into a category
Test_Fenwick_Data$secondaryType<- as.factor(Test_Fenwick_Data$secondaryType)

#Find Range of X
range(Test_Fenwick_Data$x)
# Find the range of y
range(Test_Fenwick_Data$y)
#Drop NAs
Test_Fenwick_Data <- filter(Test_Fenwick_Data, x != 'NA' & y != 'NA') 

#Find Range of X
range(Test_Fenwick_Data$x)
# Find the range of y
range(Test_Fenwick_Data$y)

# Create a new column for each shots angle form goal

Test_Fenwick_Data$y <- ifelse(Test_Fenwick_Data$x < 0,
                               -1 * Test_Fenwick_Data$y, Test_Fenwick_Data$y)

Test_Fenwick_Data$x <- abs(Test_Fenwick_Data$x)


Test_Fenwick_Data$shot_angle <- (asin
                                  (abs
                                    (Test_Fenwick_Data$y)
                                    /sqrt(
                                      (87.95 - 
                                         abs(Test_Fenwick_Data$x))^2
                                      + Test_Fenwick_Data$y^2))*180)/ 3.14

## Shots below the net should result in an angle larger than 90 degrees
Test_Fenwick_Data$shot_angle <- ifelse(abs(Test_Fenwick_Data$x) > 88, 90 + 
                                          (180-(90 + Test_Fenwick_Data$shot_angle)), 
                                        Test_Fenwick_Data$shot_angle)
# New column for distance from goal
Test_Fenwick_Data$distance <- sqrt(
  (87.95 - abs(Test_Fenwick_Data$x))^2 + Test_Fenwick_Data$y^2)

## Testing Model
Test_Fenwick_Data$xG <- predict(xGmodel, Test_Fenwick_Data, type = "response")

avg_xG_by_coord <- Test_Fenwick_Data %>% group_by(x, y) %>%
  summarise(xg = mean(xG))

ggplot(avg_xG_by_coord, aes(x, y, fill = xg)) + geom_raster() +
  scale_fill_gradient(low = 'blue', high = 'red')+
  geom_vline(xintercept = 0, color = 'red') +
  geom_vline(xintercept = 25, color = 'blue') +
  geom_vline(xintercept = 88, color = 'red') +
  xlab('X Coordinates') + ylab('Y Coordinates') +
  labs(title = 'Average xG Value by Coordinate')

# test the predictions of our model is to plot it’s ROC curve 
# calculate the area underneath the curve
g <- roc(is_goal ~ xG, data = Test_Fenwick_Data)
plot(g)

#Find the area underneath the curve
auc(g)


#code to group xg and goals by player
## Go back ad add the player names for more information
xg_player <- Test_Fenwick_Data %>%
  group_by(player_id, team_id_for) %>%
  summarise( xG = sum(xG), Goals = sum(is_goal), Difference = sum(xG) - sum(is_goal))
head(xg_player)

arrange(xg_player, desc(xG))

ggplot(aes(x = xG, y = Goals), data = xg_player) +
  geom_point() + 
  geom_smooth(method = 'lm') +
  labs(title = 'Expected Goals vs Goals by Player')

# Linear model
play_xg <- lm(Goals ~ xG, data = xg_player)
summary(play_xg)

# By team 
## Join the team name in to add more context
xg_team <- Test_Fenwick_Data %>%
  group_by(team_id_for) %>%
  summarise( xG = sum(xG), Goals = sum(is_goal), Difference = sum(xG) - sum(is_goal))

arrange(xg_team, desc(xG))


team_xg <- lm(Goals ~ xG, data = xg_team)
summary(team_xg)


ggplot(aes(x = xG, y = Goals), data = xg_team) +
  geom_point() + 
  geom_smooth(method = 'lm') +
  labs(title = 'Expected Goals vs Goals by Team')