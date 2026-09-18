## Linear Regression

The following python file experiments with linear regression, using Stochastic gradient descent 
on a tiny dataset. It uses numpy to simplify the work.

It uses the Mean Squared Error function as Loss.

```
W <- W - learning_rate * (P - y[i]) * X[i]
b <- b - learning_rate * (P - y[i])
``` 

were the update equations used.
