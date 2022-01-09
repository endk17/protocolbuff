#!/usr/bin/env bash

protoc -I=proto --python_out=python/simple proto/simple.proto
protoc -I=proto --python_out=python/addressbook proto/addressbook.proto