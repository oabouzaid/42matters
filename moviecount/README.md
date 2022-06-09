# wordcount Container

This container contains a simple movie view count prediction using `sklearn` and `pandas`

## Getting Started

Please find below the instructions to run to be able to run the code within the container. 

### Prerequisities


In order to run this container you'll need docker installed.

* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

### Usage

1. After cloning the `42matters` repo, `cd` to `moviecount` folder.


2. Build the docker image which consists of copying the python code, the requirements `requirements.txt` file.

```shell
docker build -t moviecount .
```

3. Change the directory to `src`, using 

```shell
cd src/
```

4. Run the container with a volume data and copies the output `prediction.csv` locally in the current directory:

```shell
docker run -v ${PWD}:/src moviecount
```

## Discussion

### Chosen approach:

Using the few number of views we have, we train a random forest regressor (regressor X = [`Year`, `Rating`, `Rating Count`])

The choice of the random forest over a simple linear regression comes from the fact that linear regression goes beyond the range of view count that it has been trained on, and thus generating negative values for the prediction view count.

The python script shows an example of very simple Random Forest regressor, without any hyperparameters. Of course, for a more realistic use-case, these have to be tuned and selected carefully.

The challenge of this problem is that the number of labele example is very scarce (6 movies out of 250). 

### Alternative approach:

We could also use k-means clustering with k = 6, and assign the same number of views to all movies belonging to the same cluster. This value could be the number of views given in the problem statement, but this would be a very naive approach. We could also use the movie name and do some NLP to check whether a movie belongs to a series of movies, and take that into account for the predictions.