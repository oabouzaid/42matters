## Discussion

### Chosen approach:

Using the few number of views we have, we train a random forest regressor (regressor X = [`Year`, `Rating`, `Rating Count`])

The choice of the random forest over a simple linear regression comes from the fact that linear regression goes beyond the range of view count that it has been trained on, and thus generating negative values for the prediction view count.

The python script shows an example of very simple Random Forest regressor, without any hyperparameters. Of course, for a more realistic use-case, these have to be tuned and selected carefully.

The challenge of this problem is that the number of labele example is very scarce (6 movies out of 250). 

### Alternative approach:

We could also use k-means clustering with k = 6, and assign the same number of views to all movies belonging to the same cluster. This value could be the number of views given in the problem statement, but this would be a very naive approach. We could also use the movie name and do some NLP to check whether a movie belongs to a series of movies, and take that into account for the predictions.