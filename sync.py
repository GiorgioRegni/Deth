#!/usr/bin/python

""" This code periodically starts an ethereum node, sync with the chain and\
uses docker to increlentally push the updated chain to Docker Hub in \
ihunda/deth """

import docker
import sys
import os

client = docker.from_env()

def main():
    """Main entry point for the script."""
    pass

def update_deth_container_image():
    """Run the latest deth and sync up to the latest block, then
    publish the new image to docker hub""" 
    container = client.containers.run("ihunda/geth", detach=True)
    while (True):
        """ Check blockchain sync status """
        res = container.exec_run("/geth --exec eth.syncing attach");
        print res
        os.sleep(1)
        
if __name__ == '__main__':
    sys.exit(main())
