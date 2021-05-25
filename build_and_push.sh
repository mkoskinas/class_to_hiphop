#!/bin/bash
docker build -t hiphopclass-app .
docker tag hiphopclass-app eu.gcr.io/mich-2021/hiphopclass-app
docker push eu.gcr.io/mich-2021/hiphopclass-app