#!/bin/bash
CURRENT_PATH="$(pwd)"
REAL_PATH="$CURRENT_PATH/src"
 
echo "Tu es actuellement dans : $CURRENT_PATH"
echo "Chemin absolu de flaskApi.py : $REAL_PATH"
python $REAL_PATH/flaskAPI.py
