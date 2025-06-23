import json
import os
from pathlib import Path
#from tqdm import tqdm

def split_coco_by_folders(coco_path, train_folder, val_folder, output_folder):
    with open(coco_path, 'r') as f:
        coco = json.load(f)

    images = coco['images']
    annotations = coco['annotations']
    categories = coco['categories']
    info = coco.get('info', {})
    licenses = coco.get('licenses', [])

    # Obtenir les noms de fichiers présents dans chaque dossier
    train_files = {f.name for f in Path(train_folder).glob('*') if f.suffix in ['.jpg', '.png']}
    val_files = {f.name for f in Path(val_folder).glob('*') if f.suffix in ['.jpg', '.png']}

    print("Fichiers trouvés dans le dossier train :", sorted(train_files)[:5])
    print("Fichiers trouvés dans le dossier val :", sorted(val_files)[:5])
    print("Exemples de file_name dans COCO :", [img["file_name"] for img in coco["images"][:5]])

    def create_subset(image_filenames, subset_name):
        image_id_map = {}
        new_images = []
        new_annotations = []

        for img in images:
            if img['file_name'] in image_filenames:
                new_id = len(new_images) + 1
                image_id_map[img['id']] = new_id
                img_copy = img.copy()
                img_copy['id'] = new_id
                new_images.append(img_copy)

        for ann in annotations:
            old_image_id = ann['image_id']
            if old_image_id in image_id_map:
                ann_copy = ann.copy()
                ann_copy['image_id'] = image_id_map[old_image_id]
                ann_copy['id'] = len(new_annotations) + 1
                new_annotations.append(ann_copy)

        coco_subset = {
            'info': info,
            'licenses': licenses,
            'images': new_images,
            'annotations': new_annotations,
            'categories': categories
        }

        output_path = Path(output_folder) / f'instances_{subset_name}.json'
        output_path.parent.mkdir(parents=True, exist_ok=True)  # ✅ crée le dossier si nécessaire

        with open(output_path, 'w') as f:
            json.dump(coco_subset, f, indent=2)
        print(f"[✓] Fichier COCO '{subset_name}' écrit à : {output_path}")

    # Création des fichiers
    create_subset(train_files, 'train')
    create_subset(val_files, 'val')

if __name__ == "__main__":

    split_coco_by_folders(
        coco_path='output_coco.json',          # ton fichier COCO complet
        train_folder='/Users/rolly/Documents/10-19_Université_et_scolarité/python_s2/projet/data/split/train/images',      # dossier avec images d'entraînement
        val_folder='/Users/rolly/Documents/10-19_Université_et_scolarité/python_s2/projet/data/split/val/images/',          # dossier avec images de validation
        output_folder='Users/rolly/Documents/10-19_Université_et_scolarité/python_s2/projet/data/split/annotations/'           # dossier de sortie pour les .json
    )