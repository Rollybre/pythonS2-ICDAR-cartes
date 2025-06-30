#!/bin/bash
# Active conda
source ~/anaconda3/etc/profile.d/conda.sh
conda activate maptext-eval

# Évaluation DET data-sample
python eval.py --gt data_eval/metadatagoodsample.json --pred data_eval/resultatsample.json --task "det"

# Évaluation DETREC data-sample
python eval.py --gt data_eval/metadatagoodsample.json --pred data_eval/resultatsample.json --task "detrec"

# Évaluation DET data-sample
python eval.py --gt data_eval/metadatagood500.json --pred data_eval/resultat500.json --task "det"

# Évaluation DETREC data-sample
python eval.py --gt data_eval/metadatagood500.json --pred data_eval/resultat500.json --task "detrec"
