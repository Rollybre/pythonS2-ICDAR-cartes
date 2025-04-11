# pythonS2-ICDAR-cartes

## Membres du groupe
- Pia 
- Emilie 
- Charlie
- Alexandre
- Pierre-Alexandre
- Philippe
- Gaëtan

## Descriptions des tâches

**Tâche 1 : Détection de mots**
L'objectif principal de cette tâche est la **détection des mots individuels** présents sur les images de cartes historiques. Les participants doivent fournir des **polygones de délimitation précis** autour de chaque mot détecté. Le contenu textuel des mots n'est pas pris en compte pour cette tâche, et l'organisation des mots en groupes est ignorée. La **Panoptic Detection Quality (PDQ) au niveau du mot** est la métrique d'évaluation principale.

**Tâche 2 : Détection de phrases (lien de mots)**
Cette tâche exige non seulement la **détection des mots** avec leurs polygones, mais également leur **regroupement en phrases constitutives**. Les mots appartenant à la même phrase doivent être regroupés en une liste (groupe). L'**ordre des mots au sein d'un groupe n'est pas évalué** dans cette tâche. Comme pour la tâche 1, le contenu textuel des mots est ignoré. La **PDQ au niveau du groupe (phrase)** est la métrique d'évaluation principale, calculée sur l'union des polygones des mots de chaque groupe.

**Tâche 3 : Détection et reconnaissance de mots**
Dans cette tâche, les participants doivent fournir à la fois les **polygones de délimitation des mots et leurs transcriptions textuelles correspondantes**. Le champ "**text**" doit être rempli pour chaque mot. Le regroupement des mots en phrases n'est pas requis et toute organisation au niveau du groupe sera ignorée. La **Panoptic Word Quality (PWQ)**, qui requiert une transcription correcte en plus d'une bonne localisation, est la métrique d'évaluation principale. La **Panoptic Character Quality (PCQ)**, qui évalue la précision de la reconnaissance au niveau du caractère, est également utilisée.

**Tâche 4 : Détection et reconnaissance de phrases**
Cette tâche est la plus complète et requiert la **détection des mots, leur regroupement en phrases (dans l'ordre de lecture) et la reconnaissance du texte de chaque phrase**. Les soumissions doivent inclure les polygones, les transcriptions ("text") et le regroupement des mots en listes **ordonnées**. La **PCQ au niveau du groupe (phrase)** est la métrique d'évaluation principale, où le texte de référence et la prédiction sont la concaténation des mots dans l'ordre de la liste. La PWQ au niveau du groupe est également rapportée.

### Sur quelle(s) tâche(s) travaillons nous ? 

## Les méthodes mises en place l'année passée
### Tâche 1
#### MaskDINO
Mask DINO est une extension de DINO qui unifie la détection d'objets et la segmentation d'images (instance, panoptique et sémantique) en ajoutant une branche de prédiction de masque. Il utilise les plongements de requêtes de DINO pour prédire des masques binaires à partir d'une carte de plongement de pixels haute résolution

Avantages :

- Unification des tâches de détection et de segmentation
- Performances de pointe en segmentation instance, panoptique et sémantique parmi les modèles de moins d'un milliard de paramètres
- Simple, efficace et extensible, bénéficiant de données de détection et de segmentation à grande échelle
- Coopération entre la détection et la segmentation, où chaque tâche s'améliore mutuellement

Inconvénients :

- Performance de segmentation panoptique (Mask AP) inférieure aux modèles spécialisés en segmentation d'instance
- Performance de détection à grande échelle non optimale en raison des limitations de mémoire GPU
- Besoins en mémoire GPU accrus (8 GPU (???) pour l'entraînement)
- Coopération limitée entre les différentes tâches de segmentation dans la segmentation panoptique sur COCO


## Méthode qu'on veut mettre en place

