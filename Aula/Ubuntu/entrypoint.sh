#!/usr/bin/env bash

if [ -z "$1" ]; 
then
    echo "Container inciado sem parâmetro"
else
    echo "Container iniciado com parâmetro: $1" 
fi