# Facial-Demographics-TinyML
The project involves extensive analysis and feature extraction of facial data. Both ML and DL models were applied and later on the analysis was extended to a video stream. In the last stage of the project, the best model was shifted to TinyML format and deployed on Raspberry Pi camera to develop an real world analysis application. 

UTK dataset is used for training purposes. The link to the data set is : https://susanqq.github.io/UTKFace/ 
```
Labels
The labels of each face image is embedded in the file name, formated like `[age]_[gender]_[race]_[date&time].jpg`

`[age]` is an integer from 0 to 116, indicating the age
`[gender]` is either 0 (male) or 1 (female)
`[race]` is an integer from 0 to 4, denoting White, Black, Asian, Indian, and Others (like Hispanic, Latino, Middle Eastern).
`[date&time]` is in the format of yyyymmddHHMMSSFFF, showing the date and time an image was collected to UTKFace
```