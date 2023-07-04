#!/bin/bash
run="run1"
python3 run.py insens -all -out=output/$run/
python3 run.py 2o -cd -cda=DEBLOATERX -all -out=output/$run/
python3 run.py 2o -cd -cda=COLLECTION -all -out=output/$run/
python3 run.py 2o -cd -all -out=output/$run/
python3 run.py 2o -all -out=output/$run/
python3 run.py 3o -cd -cda=DEBLOATERX -all -out=output/$run/
python3 run.py 3o -cd -cda=COLLECTION -all -out=output/$run/
python3 run.py 3o -cd -all -out=output/$run/
python3 run.py 3o -all -out=output/$run/
python3 run.py Z-2o E-2o -all -out=output/$run/
python3 run.py Z-3o E-3o -all -out=output/$run/


python3 runbach.py insens -all -out=output-bach/$run/
python3 runbach.py 2o -cd -cda=DEBLOATERX -all -out=output-bach/$run/
python3 runbach.py 2o -cd -cda=COLLECTION -all -out=output-bach/$run/
python3 runbach.py 2o -cd -all -out=output-bach/$run/
python3 runbach.py 2o -all -out=output-bach/$run/
python3 runbach.py 3o -cd -cda=DEBLOATERX -all -out=output-bach/$run/
python3 runbach.py 3o -cd -cda=COLLECTION -all -out=output-bach/$run/
python3 runbach.py 3o -cd -all -out=output-bach/$run/
python3 runbach.py 3o -all -out=output-bach/$run/
python3 runbach.py Z-2o E-2o -all -out=output-bach/$run/
python3 runbach.py Z-3o E-3o -all -out=output-bach/$run/
