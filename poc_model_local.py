from fastai.vision.all import load_learner, PILImage
from dataclasses import dataclass
import time
from pathlib import Path


@dataclass
class ModelOutput:
    predicted_class: str
    probs: dict
    predicted_class_prob: float
    time_to_predict: float = 0.0


# Load the pre-trained model
LERNER = load_learner('poc_model.pkl')
DATA_FOLDER_PATH = Path('test_data')


def predict_image(image_path_infer: Path) -> ModelOutput:
    img = PILImage.create(image_path_infer)

    start_time = time.time()
    prediction, _, probabilities = LERNER.predict(img)
    end_time = time.time()

    predicted_class_prob = probabilities[LERNER.dls.vocab.o2i[prediction]].item()
    return ModelOutput(prediction, probabilities, predicted_class_prob, round(end_time - start_time, 2))


# Example usage
for file_path in DATA_FOLDER_PATH.iterdir():
    if not file_path.is_file():
        raise FileNotFoundError(f"File '{file_path}' not found")

    print(f"Analyzing file '{file_path}'")
    result = predict_image(file_path)
    print(f"Predicted class '{result.predicted_class}' with probability: '{result.predicted_class_prob}'")
    print(f'Probabilities: {result.probs}')
    print(f'Time to predict: {result.time_to_predict}s')
    print('---')
