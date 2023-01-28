import os

from imageai.Classification import ImageClassification

execution_path = os.path.abspath(os.path.dirname(__file__))

prediction = ImageClassification()
prediction.setModelTypeAsMobileNetV2()
prediction.setModelPath(os.path.join(execution_path, "mobilenet_v2-b0353104.pth"))
prediction.loadModel()

predictions, probabilities = prediction.classifyImage(
    os.path.join(execution_path, "house.jpg"), result_count=5
)
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction, " : ", eachProbability)

hyerim = 
PI = 3.14