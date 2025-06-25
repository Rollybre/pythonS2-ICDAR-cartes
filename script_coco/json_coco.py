import json
import os
from pathlib import Path

def polygon_to_bbox(polygon):
    x_coords = [point[0] for point in polygon]
    y_coords = [point[1] for point in polygon]
    x_min, y_min = min(x_coords), min(y_coords)
    width, height = max(x_coords) - x_min, max(y_coords) - y_min
    return [x_min, y_min, width, height]

def main():
    input_path = 'ign25synth_train.json'  # ton fichier d'entrée
    output_path = 'output_coco.json'

    with open(input_path, 'r') as f:
        data = json.load(f)

    coco = {
        "info": {
            "description": "Dataset converted from custom format",
            "version": "1.0",
            "year": 2025,
        },
        "licenses": [],
        "images": [],
        "annotations": [],
        "categories": [{"id": 1, "name": "text", "supercategory": "none"}]
    }

    annotation_id = 1
    for image_id, item in enumerate(data, 1):
        image_filename = Path(item["image"]).name

        # On ne peut pas récupérer width/height sans les images => valeurs fictives
        coco["images"].append({
            "id": image_id,
            "file_name": image_filename,
            "width": 2000,   # à adapter
            "height": 2000   # à adapter
        })

        for group in item["groups"]:
            for obj in group:
                vertices = obj["vertices"]
                segmentation = [coord for point in vertices for coord in point]
                bbox = polygon_to_bbox(vertices)

                coco["annotations"].append({
                    "id": annotation_id,
                    "image_id": image_id,
                    "category_id": 1,
                    "segmentation": [segmentation],
                    "bbox": bbox,
                    "area": bbox[2] * bbox[3],
                    "iscrowd": 0
                })

                annotation_id += 1

    with open(output_path, 'w') as f:
        json.dump(coco, f, indent=2)

    print(f"Conversion terminée : {output_path}")

if __name__ == '__main__':
    main()