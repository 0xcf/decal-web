docker run --rm --volume=$PWD:/srv/jekyll:Z  \
    --volume=$PWD/vendor/bundle:/usr/local/bundle:Z \
    jekyll/jekyll:latest jekyll build

docker run --rm --volume=$PWD:/srv/jekyll:Z  \
    --volume=$PWD/vendor/bundle:/usr/local/bundle:Z \
    --publish 127.0.0.1:4000:4000 jekyll/jekyll:latest jekyll serve