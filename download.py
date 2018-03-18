#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Downloader for unsup tutorial

@author: zeyi
"""
import os
import requests

from tqdm import tqdm

DATA_DIR = 'data'

def download_file(url, destination):
    """Wrapper for downloading file with progress bar"""
    r = requests.get(url, stream=True)
    
    # Get file size
    total_size = int(r.headers.get('content-length', 0))
    block_size = 1024
    wrote = 0
    with open(destination, 'wb') as f:
        for data in tqdm(r.iter_content(block_size), 
                         total=block_size//block_size,
                         unit='KB',
                         unit_divisor=1024,
                         unit_scale=True):
            wrote += len(data)
            f.write(data)
    if total_size > 0 and wrote != total_size:
        raise(ValueError)
    return
    
def retrieve_BlueCoat(path=DATA_DIR):
    """Downloads BlueCoat Proxy Data, and prepares data for analysis"""
        
    full_path = os.path.join(path, 'bluecoat')
    if not os.path.exists(full_path):
        os.makedirs(full_path, exist_ok=True)
    
    #Check if data already exists
    zip_file = os.path.join(full_path, 'bluecoat_proxy_big.zip')
    if not os.path.isfile(zip_file):
        print('Downloading bluecoat data')
        url = 'http://log-sharing.dreamhosters.com/bluecoat_proxy_big.zip'
        download_file(url, zip_file)
    
    #Unpack zip file
    
    return

def retrieve_SotM30(path=DATA_DIR):
    """SoTM30 download"""
    full_path = os.path.join(path, 'SotM30')
    if not os.path.exists(full_path):
        os.makedirs(full_path, exist_ok=True)
    
    #Check if data already exists
    zip_file = os.path.join(full_path, 'SotM30-anton.log.gz')
    if not os.path.isfile(zip_file):
        print('Downloading SoTM30 data')
        url = 'http://log-sharing.dreamhosters.com/SotM30-anton.log.gz'
        download_file(url, zip_file)
    
    #Unpack file
    
    return

def retrieve_IDS(path=DATA_DIR):
    raise(NotImplemented)
    
if __name__ == "__main__":
    retrieve_BlueCoat()