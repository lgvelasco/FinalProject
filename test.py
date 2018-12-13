from textblob import TextBlob

import Screenplay as sp

annie_hall = sp.Screenplay("Annie_Hall.txt")

scenery_markers = ['INT.', 'EXT.']

text = annie_hall.screenplay.read()

scenes = text.split('INT' or 'EXT')
print(scenes)
print(annie_hall.divide_by_scenes())
sentinments = []

for i in range(len(scenes)):
    blob = TextBlob(scenes[i])
    emotion = blob.sentiment.polarity
    sentinments.append(emotion)
print(sentinments)


