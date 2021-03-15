Contextual Bandit for Real-Time Optimization


I am building a contextual multi-armed bandit to optimize the layout which consists of a collection of content pieces, such as images, text, etc.. through displaying variations of those content pieces to observe the maximum reward and best performing layout. 
To do so, I am looking at using Bayesian Updating of the Logistic Regression to update my Model from the Feedback generated by people who use the site. The goal here is to use the feedback from the people who use the site, such as their clicks or what they interact with, to update the algorithm. 
To do so, as seen in my code below, I am updating the means by minimizing the cost function with the Adaptive Movement Estimation Algorithm, or Adam optimization. 
Then, I update the Variances with the Laplace Approximation. 
For the Model, I am using the Thompson Sampling approach for a linear model that samples the weights, which follow an independent gaussian distribution. 
Then, my Thompson Sampling will choose the Arm with the Maximal Expected Reward, given the Context, such as what site the visitor came from and those sampled weights. In order to improve the time complexity and avoid the exhaustive, brute force approach that Thompson Sampling does. 
This is where my Greedy Hill Climbing Algorithm comes in to speed up the sampling before selecting the Maximum Reward. 
Given the Context Vector, Sampled Weights Vector and Number of Climbing Steps, My objective is to continue picking random content pieces, scoring each of its variants and selecting the variant with the Highest Reward for the Remainder of the Climbing Steps. 
For each Climbing Step, I am looking to select a random content piece to Optimize and Selecting the Variation of that content piece and ultimately the layouts that perform best and have the Highest Reward. 
My overall main idea is to decouple the training, the bayesian updating, and thompson sampling with a nested greedy hill climbing with random restarts to create a more resilient infrastructure. 
I am looking to schedule training with a CRON job every hour for the Bayesian Updating of the feedback from the people who visit the site.

Here is the Paper that I am directly looking to Implement: https://arxiv.org/pdf/1810.09558.pdf
