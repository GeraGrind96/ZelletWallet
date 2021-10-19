#!/bin/bash
cd /home/pi/Moneda_princ
sudo gunicorn -w 12 --threads 8  -b 0.0.0.0:8000 app:app


