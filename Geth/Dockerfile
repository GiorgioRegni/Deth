# Base Geth container for Deth https://github.com/GiorgioRegni/Deth
FROM golang:1.7

# Instal Geth
RUN \
  apt-get update && apt-get upgrade -q -y && \
  apt-get install -y --no-install-recommends make gcc libc-dev ca-certificates && \
  git clone --depth 1 https://github.com/ethereum/go-ethereum && \
  (cd go-ethereum && make geth) && \
  cp go-ethereum/build/bin/geth /geth

# Clean up for a slimmer image
RUN \
  apt-get remove -y golang git make gcc libc-dev && \ 
  apt-get clean && \
  rm -rf go-ethereum

EXPOSE 8545
EXPOSE 30303

RUN mkdir -p /data/keystore /data/geth



