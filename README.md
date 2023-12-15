# dev-python-cli-janusgraph-cassandra-single-node-without-ssl-client

## Description
POC for single node without ssl cassandra in python.

## Tech stack
- python
  - germlin
- cassandra
- janusgraph
  - apache tinker
  - apache gremlin

## Docker stack
- python:3.8-slim
- janusgraph/janusgraph
- cassandra:4.0

## To run
`sudo ./install.sh -u`

## To stop (optional)
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`

# Credit
- [Janus docker guide](https://docs.janusgraph.org/operations/container/)