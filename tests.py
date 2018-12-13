from textblob import TextBlob
import Screenplay as sp

pulp_fiction = sp.Screenplay('Pulp_Fiction_Clean.txt')
# pulp_fiction.print()

text = pulp_fiction.screenplay.read()
print(text)

scenes = text.split('INT' or 'EXT')
print(scenes)

sentinments = []

for i in range(len(scenes)):
    blob = TextBlob(scenes[i])
    emotion = blob.sentiment.polarity
    sentinments.append(emotion)
print(sentinments)