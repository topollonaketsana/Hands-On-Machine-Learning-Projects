### Project 3

*In this chapter, we will start by looking at the Linear Regression model, one of the
simplest models there is. We will discuss two very different ways to train it:*

1. Using a direct “closed-form” equation that directly computes the model parame‐
ters that best fit the model to the training set (i.e., the model parameters that
minimize the cost function over the training set).


In Chapter 1, we looked at a simple regression model of life satisfaction: 
life_satisfaction $= θ_0 + θ_1$ × GDP_per_capita.

#### Linear Regression model prediction

$\hat y = θ_0 + θ_1x_1 + θ_2x_2 + ⋯ + θ_nx_n$

Where,

• ŷ is the predicted value   
• n is the number of features.  
• x_i is the ith feature value.    
• θ_j is the j_th model parameter (including the bias term $θ_0$ and  the feature weights
$θ_1, θ_2, ⋯, θ_n$).

The Linear Regression model prediction in vector form, 

$y = h_θ (x) = θ · x$


To find the performance measure of a regression model is the Root Mean Square Error (RMSE),


$MSE (X, h_θ) = \frac{1}{m} ∑ i (θ^T x^i − y^i)^2$



#### The Normal Equation
To find the value of θ that minimizes the cost function, there is a closed-form solution
—in other words, a mathematical equation that gives the result directly. This is called
the Normal Equation


$θ = (X^T X)^−1 .X^T y$

