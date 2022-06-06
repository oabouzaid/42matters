# wordcount Container

This container contains a simple word count using `pyspark`.

## Getting Started

Please find below the instructions to run to be able to run the code within the container. 

### Prerequisities


In order to run this container you'll need docker installed.

* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

### Usage

Build the docker image which consists of copying the python code, the librart `requirements.txt` file, and downloading the input data using `curl` command.

```shell
docker build -t wordcount <DESIRED_LOCATION>
```

Execute the word count python code within the container, and outputs the result into `src/output/part-00000` file inside the docker image.
This will also display the top 50 words in terms of occurence.

```shell
docker container run wordcount
```

If you want to view the whole count output, you can fetch the file from the docker image into a desired location in your local machine using the command below.

```shell
docker cp <CONTAINER ID>:/src/output/part-00000 <DESIRED_LOCATION>
```

**Note:** The `CONTAINER ID` can be fetched using the command, where the `IMAGE` = `helloworld`:

```shell
docker ps -as
```
