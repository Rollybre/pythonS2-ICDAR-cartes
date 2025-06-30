#!/bin/bash
source ~/anaconda3/etc/profile.d/conda.sh
conda activate maptext-eval

echo "Résultats Évaluation DET data-sample :" > resultats.txt
python eval.py --gt data_eval/metadatagoodsample.json --pred data_eval/resultatsample.json --task det >> resultats.txt

echo -e "\nRésultats Évaluation DETREC data-sample :" >> resultats.txt
python eval.py --gt data_eval/metadatagoodsample.json --pred data_eval/resultatsample.json --task detrec >> resultats.txt

echo -e "\nRésultats Évaluation DET 500 samples :" >> resultats.txt
python eval.py --gt data_eval/metadatagood500.json --pred data_eval/resultat500.json --task det >> resultats.txt

echo -e "\nRésultats Évaluation DETREC 500 samples :" >> resultats.txt
python eval.py --gt data_eval/metadatagood500.json --pred data_eval/resultat500.json --task detrec >> resultats.txt
