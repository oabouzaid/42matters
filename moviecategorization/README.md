# Movie categorization


## Discussion

### Chosen approach: NLP with multi-label classification 

First of all, we will need to reduce the cardinality of the movie categories. Thousands of categories will make the problem very complex. An idea would be to use some NLP word clustering technique based on semantics. For example we could use word2vec/Glove for word embedding and computing the cosine similarity between the movie categories, and do some clustering in a way that map the similar ones into a single category.

Now that we have a significantly small amount of categories (call it k << N, N being the initial category cardinality), we will need some ground truth as a reference to validate movie categories assignment. This ground truth could be by cross checking other major movie websites such as IMdB, rottentomatoes, Netflix, etc. In this way, we try to manually tag a subset of selected movies (of different types) to cover the k categories.

Now, out of the movies we tagged (each movie could have one more tags, k tags maximum since there are now k categories) we can apply a ML model that learns from the following:
- Title and description: on which we can that use stemming/lemmatization using NLTK then using word2vec to vectorize the words.
- Do some image processing on the posters to help map to the movie categories. There is an excellent Stanford paper (http://cs230.stanford.edu/projects_winter_2020/reports/32643471.pdf) that presents the use of multiple CNNs (ResNet, DenseNets etc.) in order to map the posters (images) into categories. We could extend this by also providing the Title and Description that we preprocess in the previous point.   


We train the model using folds for cross validation to prevent overfitting.

As we have k movie categories, the output will be a k-dimensional binary vector, with the predicted categories set to 1.

Once happy with the result, we can now generalise our prediction and tag the rest of the (untagged) movies!

**Pros:** The cardinality reduction allow to significantly simplify the problem, without necessarily losing a lot of intrinsic information.

**Cons:** Requires initial manual labelling of the movies since this is a supervised learning approach


### Alternative approach:

We could instead opt for some clustering (for example k-means), however the number of cluster will (and should) significantly lower that the thousands of given movie categories, since euclidian distance suffers from the curse of dimentionality). Also the categories will be hard to interpret and would require some manual work to label the clusters of movies. However, the algorithm is simple and does not require any data labelling or tagging beforehand.  