# calculate-pi
Calculate Pi using Leibniz formula: pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...

This repository sources the Docker image `ottokruse/calculate-pi`.

Just a silly program to keep your CPU busy ;)

Usage:

`docker run --rm ottokruse/calculate-pi 1000` # pass the nr of fractals to consider, e.g. 2 would give 1 - 1/3 + 1/5
