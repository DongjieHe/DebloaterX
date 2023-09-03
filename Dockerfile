# compile artifact
# FROM amd64/gradle AS buildEnv
# RUN apt-get install python3 -y
# ADD . /build/
# WORKDIR /build/
# RUN ./gradlew clean fatJar

# build image
FROM hdjay2013/jupx:v16
ENV workdir /debloaterx
WORKDIR $workdir
ENV user root
USER $user
RUN pip3 install brokenaxes
RUN pip3 install scipy
# artifact
COPY artifact/benchmarks/applications/checkstyle $workdir/artifact/benchmarks/applications/checkstyle
COPY artifact/benchmarks/applications/findbugs $workdir/artifact/benchmarks/applications/findbugs
COPY artifact/benchmarks/applications/JPC $workdir/artifact/benchmarks/applications/JPC
COPY artifact/benchmarks/dacapo2006/ $workdir/artifact/benchmarks/dacapo2006/
COPY artifact/benchmarks/dacapo-bach/ $workdir/artifact/benchmarks/dacapo-bach/
COPY artifact/benchmarks/JREs/jre1.6.0_45/ $workdir/artifact/benchmarks/JREs/jre1.6.0_45/
COPY artifact/benchmarks/JREs/jre1.8.0_121_debug/ $workdir/artifact/benchmarks/JREs/jre1.8.0_121_debug/

COPY artifact/sample/ $workdir/artifact/sample/
COPY artifact/util/ $workdir/artifact/util/
COPY artifact/run.py $workdir/artifact/
COPY artifact/qilin.py $workdir/artifact/
COPY artifact/driver.sh $workdir/artifact/
COPY artifact/debloaterX.py $workdir/artifact/
COPY artifact/runbach.py $workdir/artifact/
COPY artifact/__init__.py $workdir/artifact/
COPY artifact/Qilin-0.9.2-SNAPSHOT.jar $workdir/artifact/
# source
COPY libs $workdir/qilin/libs
COPY gradle/ $workdir/qilin/gradle/
COPY qilin.core $workdir/qilin/qilin.core
COPY qilin.microben $workdir/qilin/qilin.microben
COPY qilin.pta $workdir/qilin/qilin.pta
COPY qilin.util $workdir/qilin/qilin.util
COPY build.gradle $workdir/qilin/
COPY gradlew $workdir/qilin/
COPY gradlew.bat $workdir/qilin/
COPY LICENSE $workdir/qilin/
COPY README.md $workdir/qilin/
COPY run.sh $workdir/qilin/
COPY settings.gradle $workdir/qilin/

CMD /bin/bash

