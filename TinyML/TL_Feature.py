# Code to extract features form transfer learning to train just the top layers
def create_features(dataset, pre_model, input_size):
 
    x_scratch = []
 
    # loop over the images
    for imagePath in dataset:
 

        image = load_img(imagePath, target_size=input_size)
        image = img_to_array(image)
 
        # preprocess the image by (1) expanding the dimensions and
        # (2) subtracting the mean RGB pixel intensity from the
        # ImageNet dataset
        image = np.expand_dims(image, axis=0)
        image = imagenet_utils.preprocess_input(image)
 
        # add the image to the batch
        x_scratch.append(image)
 
    x = np.vstack(x_scratch)
    features = pre_model.predict(x, batch_size=32)
    features_flatten = features.reshape((features.shape[0], 7 * 7 * 512))
    return x, features, features_flatten