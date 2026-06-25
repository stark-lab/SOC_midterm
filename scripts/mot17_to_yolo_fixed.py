import os
import configparser
import shutil


def read_seqinfo(seqinfo_path):
    config = configparser.ConfigParser()
    config.read(seqinfo_path)
    width = int(config['Sequence']['imWidth'])
    height = int(config['Sequence']['imHeight'])
    return width, height


def convert_sequence(sequence_folder, output_images_folder, output_labels_folder):
    seqinfo_path = os.path.join(sequence_folder, 'seqinfo.ini')
    img_width, img_height = read_seqinfo(seqinfo_path)

    gt_path = os.path.join(sequence_folder, 'gt', 'gt.txt')
    img_dir = os.path.join(sequence_folder, 'img1')

    boxes_by_frame = {}
    with open(gt_path, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            frame_id = int(parts[0])
            x = float(parts[2])
            y = float(parts[3])
            w = float(parts[4])
            h = float(parts[5])
            is_valid = int(parts[6])
            class_id = int(parts[7])

            if is_valid != 1 or class_id != 1:
                continue

            # NEW: clamp the box so it never extends past the image edges
            x = max(0, x)
            y = max(0, y)
            w = min(w, img_width - x)
            h = min(h, img_height - y)

            boxes_by_frame.setdefault(frame_id, []).append((x, y, w, h))

    os.makedirs(output_images_folder, exist_ok=True)
    os.makedirs(output_labels_folder, exist_ok=True)

    image_files = sorted(os.listdir(img_dir))
    for image_name in image_files:
        frame_id = int(os.path.splitext(image_name)[0])

        shutil.copy(os.path.join(img_dir, image_name),
                    os.path.join(output_images_folder, image_name))

        label_name = os.path.splitext(image_name)[0] + '.txt'
        label_path = os.path.join(output_labels_folder, label_name)

        lines_to_write = []
        for (x, y, w, h) in boxes_by_frame.get(frame_id, []):
            x_center = (x + w / 2) / img_width
            y_center = (y + h / 2) / img_height
            w_norm = w / img_width
            h_norm = h / img_height
            lines_to_write.append(f"0 {x_center:.6f} {y_center:.6f} {w_norm:.6f} {h_norm:.6f}")

        with open(label_path, 'w') as f:
            f.write('\n'.join(lines_to_write))

    print(f"Done: {sequence_folder} -> {len(image_files)} images processed")
