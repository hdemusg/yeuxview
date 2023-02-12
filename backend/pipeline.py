from google.cloud import storage
from PIL import Image
import io
from fastai.vision.all import *
import pandas
from flask import jsonify

def fetch(filename, bucket, blobname): 
    blob = bucket.get_blob(blobname).download_as_string()
    bytes = io.BytesIO(blob)
    im = Image.open(bytes)
    return im

def classify(image_l, image_r):
    '''
    print("/predict request")
    req_json = request.get_json()
    json_instances = req_json["instances"]
    X_list = [np.array(j["image"], dtype="uint8") for j in json_instances]
    X_transformed = torch.cat([transform(x).unsqueeze(dim=0) for x in X_list]).to(device)
    preds = model(X_transformed)
    preds_classes = [classes[i_max] for i_max in preds.argmax(1).tolist()]
    print(preds_classes)
    return jsonify({
    "predictions": preds_classes
    })
    '''
    learn_test = load_learner('export.pkl')
    im_l = learn_test.predict(tensor(image_l))
    im_r = learn_test.predict(tensor(image_r))
    data = (im_l, im_r)

    '''
    ((['cataract'], TensorBase([False,  True, False, False, False, False, False, False]), TensorBase([1.3244e-01, 1.0000e+00, 3.3794e-01, 1.0679e-02, 6.9232e-02,
            2.7801e-02, 1.6186e-04, 2.4527e-01])), (['normal'], TensorBase([False, False, False, False, False, False,  True, False]), TensorBase([0.1876, 0.1003, 0.1331, 0.2466, 0.1485, 0.1195, 0.7667, 0.1394])))
    '''
    print(type(data))
    print(data)
    res = jsonify({'image1': {'diagnosis': data[0][0][0], 'preds': data[0][1].tolist(), 'probs': data[0][2].tolist()}, 'image2': {'diagnosis': data[1][0][0], 'preds': data[1][1].tolist(), 'probs': data[1][2].tolist()}})
    return res

def pat(x):
    return x.paths