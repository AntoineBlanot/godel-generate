#!/bin/bash

N=10
OUT_FILE="data/dummy.txt"
DEVICE="cuda"           # cpu
MODEL_NAME="microsoft/GODEL-v1_1-base-seq2seq"      # microsoft/GODEL-v1_1-large-seq2seq
KNOWLEDGE="Your favorite sport is tennis."          # input the knowledge here
DIALOG="If you had to pick one, what would your favorite sport be?"     # input the dialog here

python generate.py --n $N --model_name "$MODEL_NAME" --device "$DEVICE" --out "$OUT_FILE" \
    --knowledge "$KNOWLEDGE" --dialog "$DIALOG"