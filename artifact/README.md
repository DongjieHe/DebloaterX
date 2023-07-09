# A Container-Usage-Pattern-based Context Debloating Approach for Object-Sensitive Pointer Analysis (Artifact)

## Outline

* Requirements
* Getting Started
    * Run Docker Image
    * Directory Structure
    * Test Driving Script
    * Test Tables/Figures Generation Script
* Step-by-Step guides
    * Step 1: run `driver.sh`
    * Step 2: run `debloaterX.py` to generate tables and figures
    * Step 3: validate paper claims

## Requirements

We will provide a ready-to-use docker image for artefact evaluation. Our tool, `DebloaterX`, has been open-sourced at [https://github.com/DongjieHe/DebloaterX.git](https://github.com/DongjieHe/DebloaterX.git).

For reviewers (users) who want to review (use) our tool on their local machines, we briefly introduce the requirements or dependencies of `DebloaterX` below.

The artifact built on the latest version of Ubuntu relies on the following softwares: `Python3`, `xetex`, and `Python3-pip`. These softwares can be installed by following commands:

```
# apt-get install python3 -y
# apt-get install python3-pip -y
# apt-get install texlive-xetex -y
```

Since `DebloaterX` is implemented in [`Qilin`](https://github.com/QilinPTA/Qilin), it also shares the same prerequisites of `Qilin`, e.g., a newer JDK (Java 16+) and the `Gradle` build automation tool. These dependencies will be automatically resolved by `Qilin`'s building scripts. 

The Python scripts in this artefact have used a few third-party packages: `matplotlib`,
`numpy`, `scipy`, and `brokenaxes`. We have prepared them in `requirements.txt` so that users can use the following commands to install them all by one command:

```
# pip3 install -r requirements.txt
```

Finally, we have conducted all experiments on a Linux server with 16 CPUs, 512 GB memory, and a time budget of 12 hours per program. Different settings will result in different analysis times and scalability. 

We wish the reviewers could obtain enough resources to evaluate our artefact. In case reviewers could not get enough computing resources, they can still validate the claims of our paper by evaluating some small benchmarks such as `antlr`, `fop`, `hsqldb`, `avrora`, and `pmd`. 

## Getting Started (in about 10 mins)

### Run Docker Image

* install Docker on your machine: https://docs.docker.com/engine/install/
* download the docker image and this README.md file from `Zenodo`
* load docker image:
```
# docker load < debloaterx_artifact.tar.gz
```
* run the docker image:
```
# docker run -it debloaterx:latest
```
If everything is correct, you should be in the `/debloaterx/` directory.
One can use the following command to create a connection directory from your host machine with the one in the container.
```
# docker run --mount type=bind,source=/local/path/to/result,target=/debloaterx/result -it debloaterx:latest
```

### Directory Structure
In this artefact, there are two top-level directories: `qilin` and `artifact`. 

+ `qilin/` includes the source code of `Qilin` and our tool `DebloaterX`. The users can use the command `./run.sh` to build the source code directly. The core implementation of `DebloaterX` is located in `qilin/qilin.pta/src/qilin/pta/toolkits/debloaterx`. We have provided brief comments on our implementation to explain the objectives of each file.
+ `artifact/` includes all files that are necessary for evaluating our artefact.
    * `benchmarks/` contains all benchmarks used in our evaluation, including JREs and benchmarks from `DaCapo 2006`, `DaCapo bach`, and also third-party applications. 
    * `Qilin-0.9.2-SNAPSHOT.jar` is the only executable file used in the evaluation. It can be compiled from the source code using `./run.sh` under `qilin/` directory (the compilation result will be in `qilin/artifact/`).
    * `sample/` includes one run of experimental data used in our paper. Lazy reviewers can use these provided data to reproduce all evaluation results used in our paper ^^.
    * `*.py` and `*.sh` are scripts used for evaluation.


### Test Driven Scripts

The benchmarks in the paper are coming from three sources: `DaCapo 2006`, `third-party` applications and `DaCapo bach`. We use `run.py` to run benchmarks in `DaCapo 2006` and `third-party` and `runbach.py` to run benchmarks in `DaCapo bach`. Both usages of the two scripts can be described by the grammar below:

```
cmd := script argumentList
script := run.py | runbach.py
argumentList := argument argumentList
argument := -print | -out={OUTPUT-PATH} | benchmark | pta | -cd | -cda={CONCH|DEBLOATERX}
benchmark := antlr | bloat | eclipse | fop | hsqldb | checkstyle | JPC | avrora | pmd | sunflow | tradebeans | xalan
pta := insens | 2o | Z-2o | 3o | Z-3o
```

`-cda=...` only works when `-cd` is specified. One can specify multiple benchmarks and multiple pointer analysis by using `benchmark` and `pta` multiple times.

When `script := run.py`, the benchmarks could be any subset of `{antlr, bloat, eclipse, fop, hsqldb, checkstyle, JPC}`. When `script := runbach.py`, the benchmarks could be any subset of `{avrora, pmd, sunflow, tradebeans, xalan}`. Note, both `run.py` and `runbach.py` invoke `qilin.py` which is a driving script of `Qilin-0.9.2-SNAPSHOT.jar`. 

For more details, please open the scripts and read the code ^-^.

Below, we use `fop` as a test benchmark to check whether `Conch`-, `Zipper`-, `DebloaterX`- guided- $k$-obj, standard $k$-obj and `Spark` (context-insensitive Andersen analysis for Java) can run successfully.

+ Test `Spark` (should be finished in 10 seconds)
```
# python3 run.py fop insens -print
```
+ Test standard `2obj` (should be finished in 1 min)
```
# python3 run.py fop 2o -print 
```
+ Test Conch-guided 2obj, i.e., `C-2obj` in the paper (should be finished in 1 min)
```
# python3 run.py fop 2o -cd -cda=CONCH -print
```
`-cda=CONCH` can be omitted since CONCH is currently the default context-debloating approach in `Qilin`.
+ Test DebloaterX-guided 2obj, i.e., `X-2obj` in the paper (should be finished in 1 min)
```
# python3 run.py fop 2o -cd -cda=DEBLOATERX -print
```
+ Test Zipper-guided 2obj, i.e., `Z-2obj` in the paper (should be finished in 1 min)
```
# python3 run.py fop Z-2o -print 
```

### Test Tables/Figures Generation Script (in 1 min)

`debloaterX.py` is the script for generating figures and tables in our paper. We use the experimental results (running on our server and provided in the `sample/` directory) to test this script:
```
# python3 debloaterX.py  -sample
```
Remember to use the command below if you have encountered any requirements issues:
```
# pip3 install -r requirements.txt
```

The command should generate the following files: `maintable.tex`, `diffObjRatioBar.pdf`, `containerPatternBar.pdf`, `reductionratiobars.pdf`, `precisionlosstwo.pdf`, `speeduptwo.pdf`, and `pretimeTable.tex`. The $\TeX$ files can be compiled into PDF files by using the following commands:
```
# xelatex maintable.tex
# xelatex pretimeTable.tex
```

The table below maps the generated files with their names used in the paper:
| File Name in Artifact  | File Name in Paper |
| ---------------------- | ------------------ |
| maintable.pdf          | Table 2            |
| diffObjRatioBar.pdf    | Figure 13-a        |
| containerPatternBar.pdf | Figure 13-b       |
| reductionratiobars.pdf  | Figure 14         |
| precisionlosstwo.pdf   | Figure 15          |
| speeduptwo.pdf         | Figure 16          |
| pretimeTable.pdf       | Table 3            |

Reviewers can ignore the data dumped on the terminal. 

## Step-by-Step guides
It is ready to evaluate our artefact. The evaluation contains three steps:

+ **Step 1**: use `driver.sh` (the driven script for running different benchmarks with different pointer analyses by invoking `run.py` and `runbach.py`) to obtain execution results of each pointer analysis on each benchmark. This step will take most of the review time. 
+ **Step 2**: use `debloaterX.py` to generate tables and figures by using the output of `driver.sh` (under `output/` and `output-bach/` directories by default).
+ **Step 3**: use the generated figures and tables to validate the paper claims.

### Step 1: run `driver.sh` (in about 2 days)

In `driver.sh`, `app0` and `app1` include all benchmarks that are evaluated in the paper. 
Note that different machines with different CPUs and Memory may result in different analysis times and scalability. However, the conclusion that `DebloaterX`-guided $k$-obj is significantly faster than both `Conch`- and `Zipper`-guided $k$-obj while achieving nearly the same precision as the standard $k$-obj can be guaranteed.

Let us start by running the following command:
```
# ./driver.sh
```
or 
```
# nohup ./driver.sh & 
```
to run in the background mode.

For reviewers who do not have enough computing resources, they can change variables `app0` and `app1` in `driver.sh` to exclude some large benchmarks such as `bloat`, `eclipse`, `checkstyle`, `tradebeans`, and `xalan`.

The experimental results are saved in `output/run1/` and `output-bach/run1/` by default. Reviewers can change this value by modifying the variable `run` in `driver.sh`.

To avoid accidental loss of analyzed data, we encourage reviewers to associate the output data directory (i.e., `output/` and `output-bach/` in the container) with the host directory by using the binding technique (i.e., `--mount type=bind,source=...,targe=...` ) introduced above.
### Step 2: run `debloaterX.py` to generate tables and figures (in less than 5 seconds)

just run the following commands:

```
# python3 debloaterX.py
# xelatex maintable.tex
# xelatex pretimeTable.tex
```

The files and their corresponding names used in the paper have already been given in the table above. 

If the reviewers have changed the value of `app0` or `app1` in Step 1, please remember to change the value of variables `bench06`, `thirdApps`, and `bench09` in `debloaterX.py` accordingly before running the commands above.

### Step 3: validate paper claims (in 2 mins)

The paper makes the following claims:

* `DebloaterX` enables $k$-obj to run significantly faster with only a negligible loss of precision (evidenced by `maintable.pdf`, `precisionlosstwo.pdf`, and `speeduptwo.pdf`).
* `DebloaterX` outperforms `Zipper` significantly in both precision and efficiency (`maintable.pdf`, `precisionlosstwo.pdf`, and `speeduptwo.pdf`). 
* `DebloaterX` outperforms `Conch` in efficiency substantially while achieving nearly the same precision (`maintable.pdf`, `precisionlosstwo.pdf`, and `speeduptwo.pdf`).
* The efficiency achieved is mainly due to that only a small portion of objects are selected to be context-dependent (evidenced by `diffObjRatioBar.pdf` and `containerPatternBar.pdf`), which results in a large reduction in OAG edges, calling contexts per method, and points-to relations (evidenced by `reductionratiobars.pdf`). 
* `DebloaterX` is an efficient pre-analysis tool, with similar overheads to `Zipper` and `Conch` (evidenced by `pretimeTable.pdf`).


That's all. Have fun.