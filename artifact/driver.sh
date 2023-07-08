#!/bin/bash
run="run1"
app0="antlr bloat eclipse fop hsqldb checkstyle JPC"
python3 run.py insens ${app0} -out=output/$run/
python3 run.py 2o -cd -cda=DEBLOATERX ${app0} -out=output/$run/
# python3 run.py 2o -cd -cda=COLLECTION ${app0} -out=output/$run/
python3 run.py 2o -cd ${app0} -out=output/$run/
python3 run.py 2o ${app0} -out=output/$run/
python3 run.py 3o -cd -cda=DEBLOATERX ${app0} -out=output/$run/
# python3 run.py 3o -cd -cda=COLLECTION ${app0} -out=output/$run/
python3 run.py 3o -cd ${app0} -out=output/$run/
python3 run.py 3o ${app0} -out=output/$run/
python3 run.py Z-2o E-2o ${app0} -out=output/$run/
python3 run.py Z-3o E-3o ${app0} -out=output/$run/

app1="avrora pmd sunflow tradebeans xalan"
python3 runbach.py insens ${app1} -out=output-bach/$run/
python3 runbach.py 2o -cd -cda=DEBLOATERX ${app1} -out=output-bach/$run/
# python3 runbach.py 2o -cd -cda=COLLECTION ${app1} -out=output-bach/$run/
python3 runbach.py 2o -cd ${app1} -out=output-bach/$run/
python3 runbach.py 2o ${app1} -out=output-bach/$run/
python3 runbach.py 3o -cd -cda=DEBLOATERX ${app1} -out=output-bach/$run/
# python3 runbach.py 3o -cd -cda=COLLECTION ${app1} -out=output-bach/$run/
python3 runbach.py 3o -cd ${app1} -out=output-bach/$run/
python3 runbach.py 3o ${app1} -out=output-bach/$run/
python3 runbach.py Z-2o E-2o ${app1} -out=output-bach/$run/
python3 runbach.py Z-3o E-3o ${app1} -out=output-bach/$run/
