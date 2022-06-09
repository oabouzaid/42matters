# moviecount Container

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