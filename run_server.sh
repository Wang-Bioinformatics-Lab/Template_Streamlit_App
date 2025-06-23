#!/bin/bash

source activate py39 #change this to your own env, see the dockerfile
streamlit run app_homepage.py --server.port 5000 --server.address 0.0.0.0