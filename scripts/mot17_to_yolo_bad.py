import cv2
import matplotlib.pyplot as plt
import os

def draw_yolo_labels(image_path, label_path, save_path=None):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h_img, w_img = img.shape[:2]

    if os.path.exists(label_path):
        with open(label_path) as f:
            for line in f:
                cls, xc, yc, w, h = map(float, line.split())
                # un-normalize: turn the 0-1 values back into pixel coordinates
                x1 = int((xc - w/2) * w_img)
                y1 = int((yc - h/2) * h_img)
                x2 = int((xc + w/2) * w_img)
                y2 = int((yc + h/2) * h_img)
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)

    plt.figure(figsize=(10, 6))
    plt.imshow(img)
    plt.axis('off')
    if save_path:
        plt.savefig(save_path, bbox_inches='tight', dpi=150)
    plt.show()

# pick any frame that has people in it — check a few frame numbers
draw_yolo_labels(
    '/content/drive/MyDrive/MOT17_processed/val/images/000250.jpg',
    '/content/drive/MyDrive/MOT17_processed/val/labels/000250.txt',
    save_path='/content/drive/MyDrive/MOT17_processed/sample_gt_frame1250.png'
)
