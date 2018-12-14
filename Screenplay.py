import re
from textblob import TextBlob
import matplotlib.pyplot as plt


class Screenplay(object):
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

    def get_sentiment(self):
        sentiments = []
        scenes = self.divide_by_scenes()

        for i in range(len(scenes)):
            blob = TextBlob(scenes[i])
            emotion = blob.sentiment.polarity
            sentiments.append(emotion)
        return sentiments

    def plot_sentiment(self):
        x = []
        for i in range(len(self.divide_by_scenes())):
            x.append(i + 1)

        y = self.get_sentiment()
        fig, ax = plt.subplots()
        plt.plot(x, y)
        plt.title(self.get_title(), fontsize=32)
        plt.ylim((-0.75, 0.75))
        plt.ylabel("Sentiment Polarity")
        plt.xlabel("Scenes")
        # plt.text(.5, 1.03, "Average Sentiment - " + str(round(average(y), 4)), color="green")
        ttl = ax.title
        ttl.set_position([.5, 1.05])

        plt.show()

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
    print(annie_hall.get_characters())

    pulp_fiction = Screenplay("Pulp_Fiction_Clean.txt")
    print(pulp_fiction.get_title())
    print(pulp_fiction.get_characters())

    get_out = Screenplay('Get_Out_Clean.txt')
    print(get_out.get_title())
    print(get_out.get_characters())

    la_la = Screenplay('La_La_Land_Clean.txt')
    print(la_la.get_title())
    print(la_la.get_characters())
    la_la.plot_sentiment()

    req = Screenplay("Requiem_For_A_Dream.txt")
    print(req.get_title())
    print(req.get_characters())
    req.plot_sentiment()