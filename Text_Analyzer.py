import re
from textblob import TextBlob

# Had to create another Screenplay class, as the original requires the text to be in a file and open it
# A flaw at the early stage of the design


class TextAnalyzer(object):
    def __init__(self, screenplay):
        self.file = open(screenplay)
        self.text = self.file.read()
        self.file.close()
        self.markers = ['INT.', 'EXT.', 'FADE', 'CREDITS', 'DISSOLVES', 'BACKGROUND', 'THE END', 'CUT', 'FLASHBACK',
                        'EXTERIOR', 'DISSOLVE', 'CLOSEUP']

    def get_title(self):
        lines = self.text.split('\n')
        title = lines[0]
        return title

    def get_characters(self):
        characters = {}
        text = self.text
        text = remove_parenthesis(text)
        for i in range(len(text)):
            if text[i].isupper():
                if any(s in text[i] for s in self.markers):
                    continue
                if text[i] in characters:
                    characters[text[i]] += 1
                else:
                    characters[text[i]] = 1
        return characters

    def get_scenery(self):
        scenery = {}
        scenery_markers = ['INT.', 'EXT.']
        for line in self.screenplay:
            if any(s in line for s in scenery_markers):
                if line in scenery:
                    scenery[line] += 1
                else:
                    scenery[line] = 1
        return scenery

    def divide_by_scenes(self):
        scenes = self.text.split('INT' or 'EXT')
        return scenes

    # def clean_name(self):

    def get_sentiment(self):
        sentiments = []
        scenes = self.divide_by_scenes()



        for i in range(len(scenes)):
            blob = TextBlob(scenes[i])
            emotion = blob.sentiment.polarity
            sentiments.append(emotion)
        return sentiments

    def print(self):
        print(self.text)


# doesn't remove parenthesis that start in one line and finish in another
def remove_parenthesis(string):
    string = string.split('\n')
    for i in range(len(string)):
        string[i] = re.sub(r" ?\([^)]+\)", "", string[i])
    return string


if __name__ == "__main__":
    annie_hall = Screenplay("Annie_Hall.txt")
    print(annie_hall.get_title())

    pulp_fiction = Screenplay("Pulp_Fiction_Clean.txt")
    print(pulp_fiction.get_title())