FROM ubuntu:latest
LABEL authors="roony"

ENTRYPOINT ["top", "-b"]