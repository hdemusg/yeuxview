from google.cloud import storage
from PIL import Image
import io

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
    pass