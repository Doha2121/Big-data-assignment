#!/bin/bash

mkdir -p /mnt/d/bd-a1/service-result/

docker cp bd-a1-container:/home/doc-bd-a1/res_dpre.csv /mnt/d/bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-1.txt /mnt/d/bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-2.txt /mnt/d/bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-3.txt /mnt/d/bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/vis.png /mnt/d/bd-a1/service-result/
docker cp bd-a1-container:/home/doc-bd-a1/k.txt /mnt/d/bd-a1/service-result/

docker stop bd-a1-container

echo "All results copied. Container stopped."
