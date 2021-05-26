# class_to_hiphop
A hip hop playlist recommender based on the trackId of a classical-music piece from Spotify.

sample request:
http://35.198.186.156/api/recommend?track_id=2kyEgPaAW8wdpvevPnkf0Z&popularity_threshold=0.3&playlist_len=50

track_id = <'your_classical_piece_track_id'>
popularity_threshold = [0,1]
playlist length = [1,50]

## Secrets
.env and google service account is not included in source code
in .env:
```
GOOGLE_APPLICATION_CREDENTIALS=<path_to_google_service_account.json>
```

## Docker
build image and tag as hiphipclass-app
```
docker build -t hiphopclass-app .
```
run docker and expose port 5000
```
docker run -p 5000:5000 hiphopclass-app:latest
```

## Hosting docker image on Goocle Container Registry (GCR)
tag image for pushing to GCR:
```
docker tag hiphopclass-app eu.gcr.io/mich-2021/hiphopclass-app
```
push to GCR
```
docker push eu.gcr.io/mich-2021/hiphopclass-app
```

or to build, tag and push docker image all at once run
```
./build_and_push.sh
```

View docker images here: https://console.cloud.google.com/gcr/images/mich-2021/EU/hiphopclass-app?project=mich-2021&gcrImageListsize=30


