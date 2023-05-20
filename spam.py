{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww28600\viewh14980\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Import dependancies\
import requests\
import time\
\
# Define payload content\
payload = \{\
    'content': \'91Your message here\'92\
\
\}\
\
# Authorize account\
header = \{\
    'authorization': \'91Your auth code here\'92\
\}\
\
# Send messages\
for i in range (100000):\
    time.sleep(Your delay here in seconds)\
    r = requests.post(\'91Your channel request url here\'92, data=payload, headers=header)\
    print("Sent message successfully!")}