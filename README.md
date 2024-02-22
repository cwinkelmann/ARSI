# ARSI exam for Radar Remote Sensing - Interferometry

## To run this you need Docker. Otherwise the installation of the dependencies is a bit tricky.



docker stop pygmtsar

docker rm pygmtsar

docker run --gpus all -v /home/christian/hnee/playground/gmtsar/notebooks:/home/jovyan/notebooks -it -dp 8888:8888 -dp 8787:8787 --restart always --name pygmtsar docker.io/pechnikov/pygmtsar 


docker run --gpus all -it -dp 8888:8888 --name docker.io/pechnikov/pygmtsar
