# SOC_midterm


##Project overview
The project relies on a hybrid convolutional network architecture YOLOv5.

## Dataset

to train the model, the MO17 dataset was used, consisting of grounddtruth instances, continuos videos as frames.

##Methodology
Training occured in 3 variants of the model, yolov5s, yolov5m and yolov5m with layers freezed. 
The tutorial google colab notebook was used, modified to path to processed dataset uploaded to drive.

##Data Preprocessing Pipeline
The data set gtound truth values are not normalised for the YOLO models. a python script had to be implemented accomodate.
write a .yaml file to allot sequences for training
out of the 7 sequences, 5 were used to train, one to validate and one to test.


## Model Training
using the tutorial colab notebook, change the path to our drive and after minor tweaks, 
the processed dataset was fed into the models. 
each training run has 25 epochs with 66 batches of 16 files each.

## Experimental Results
The results were as expected, small model being the least accurate but fastest, the medium being the slowest adn most accurate,
the freezed medium was noticably faster yet surprisingly accurate.

## Real-World Validation
some real life pictures were tested on, [accurate results](./results) were observed. 

## Issues Encountered

error 403 on miunting the drive, solved on running on different browser.

###training files being ruled corrupt 
MOT17 bounding boxes occasionally extended beyond image borders.
Effect:
Validation images were discarded, producing unfair comparisons.
Solution:
Bounding boxes were clipped to image dimensions before normalization through custom [script](./scripts).

## Future Work
Training on video and image tracking using opencv algorithms like DeepSORT.
Detecting anomalies from footage using image tracking algorithms 













