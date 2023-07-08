# A Container-Usage-Pattern-based Context Debloating Approach for Object-Sensitive Pointer Analysis (Artifact)

## Outline

* Requirements
* Getting Started
    * Run Docker Image
    * Directory Structure
    * Test Driven Script
    * Test Tables/Figures Generation Script
* Step-by-Step guides
    * Step 1: run `driver.sh`
    * Step 2: run `debloaterX.py` to generate tables and figures
    * Step 3: validate paper claims

## Requirements

We will provide a ready-to-use docker image for artifact evaluation. Our tool, `DebloaterX`, has been open-sourced at [https://github.com/DongjieHe/DebloaterX.git](https://github.com/DongjieHe/DebloaterX.git).

For reviewers (users) who want to review (use) our tool on their local machines, we briefly introduce the requirements or dependencies of `DebloaterX` below.

The artifact built on the latest version of Ubuntu relies on the following softwares: Python3, xetex, and Python3-pip. These softwares can be installed by following commands:

```
# apt-get install python3 -y
# apt-get install python3-pip -y
# apt-get install texlive-xetex -y
```

Since `DebloaterX` is implemented in [`Qilin`](https://github.com/QilinPTA/Qilin), it also shares the same prerequisites of `Qilin`, e.g., a newer JDK (Java 16+) and the `Gradle` build automation tool. These dependencies will be automatically resolved by `Qilin`'s building scripts. 

The python scripts in this artifact have used a few third-party packages: `matplotlib`,
`numpy`, and `brokenaxes`. We have prepared them in `requirements.txt` so that users can use the following commands to install them all by one command:

```
# pip3 install -r requirements.txt
```

Finally, we have conducted all our experiments on a Linux server with 16 CPUs, 512 GB memory, and a time budget of 12 hours per program. Different settings will result in different analysis time and scalability. 

We wish the reviewers could obtain enough resources to evaluate our artefact. In case that reviewers could not get enough computing resources, they can still validate the claims of our paper by evaluating some small benchmarks such as `antlr`, `fop`, `hsqldb`, `avrora`, and `pmd`. 

## Getting Started (in about 5 mins)

### Run Docker Image

* install Docker on your machine: https://docs.docker.com/engine/install/
* download the docker image and this README.md file from `Zenodo`
* load docker image:
```
# docker load < debloaterx_artifact.tar.gz
```
* run the docker image:
```
# docker run -it hdjay2013/debloaterx:latest
```
If everything is correct, you should be in the `/debloaterx/` directory.
One can use the following command to create a connection directory from you host machine with the one in container.
```
# docker run --mount type=bind,source=/local/path/to/result,target=/debloaterx/result -it hdjay2013/debloaterx:latest
```

Remember to use the command below if you have encountered any requirements issues:
```
# pip3 install -r requirements.txt
```

### Directory Structure
In this artifact, there are two top-level directories: `qilin` and `artifact`. 

+ `qilin/` includes the souce code of `Qilin` and our tool `DebloaterX`. The users can use command `./run.sh` to build the souce code directly. The core implementation of `DebloaterX` is located in `qilin/qilin.pta/src/qilin/pta/toolkits/debloaterx`. We have provided brief comments in our implementation to explain the objectives of each file.
+ `artifact/` includes all files that are necessary for evaluating our artefact.
    * `benchmarks/` contains all benchmarks used in our evaluation, including JREs and benchmarks from `DaCapo 2006`, `DaCapo bach`, and also third-party applications. 
    * `Qilin-0.9.2-SNAPSHOT.jar` is the only executable files used in the evaluation. It can be compiled from the source code by using `./run.sh` under `qilin/` directory (the compilation result will be in `qilin/artifact/`).
    * `sample/` includes one run of experimental data used in our paper. Lazy reviewers can use these provided data to reproduce all evaluation results used in our paper ^^.
    * `*.py` and `*.sh` are scripts used for evaluation.


### Test Driven Scripts


