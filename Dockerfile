From ihunda/geth

EXPOSE 8545
EXPOSE 30303

WORKDIR /data

# This volume is where sensitive Ethereum will be stored
VOLUME /data/keystore

ENTRYPOINT ["/geth", "--datadir", "/data"]
