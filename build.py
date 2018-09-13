#!/usr/bin/env python
import os
import subprocess

try:
    # pipenv lock 으로 requirements.txt 생성
    subprocess.call('pipenv lock --requirements > requirements.txt', shell=True)
    # docker build
    subprocess.call('docker build -t eb-docker:base -f Dockerfile.base .', shell=True)

finally:
    # requirements 삭제
    os.remove('requirements.txt')
