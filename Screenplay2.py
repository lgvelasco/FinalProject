import re
from textblob import TextBlob
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
import operator

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

    # Uses Text Blob to get the sentiment polarity of a scene
    def get_sentiment(self):
        sentiments = []
        scenes = self.divide_by_scenes()

        for i in range(len(scenes)):
            blob = TextBlob(scenes[i])
            emotion = blob.sentiment.polarity
            sentiments.append(emotion)
        return sentiments

    # Created a graph showing the sentiment polarity of the scene, but plt is incompatible with the GUI so it is not
    # used
    # def plot_sentiment(self):
    #     x = []
    #     for i in range(len(self.divide_by_scenes())):
    #         x.append(i + 1)
    #
    #     y = self.get_sentiment()
    #     fig, ax = plt.subplots()
    #     plt.plot(x, y)
    #     plt.title(self.get_title(), fontsize=32)
    #     plt.ylim((-0.75, 0.75))
    #     plt.ylabel("Sentiment Polarity")
    #     plt.xlabel("Scenes")
    #     # plt.text(.5, 1.03, "Average Sentiment - " + str(round(average(y), 4)), color="green")
    #     ttl = ax.title
    #     ttl.set_position([.5, 1.05])
    #
    #     plt.show()

    def plot_sentiment(self):
        x = self.get_x_sentiment()
        y = self.get_sentiment()

        fig = Figure()
        a = fig.add_subplot(111)
        a.plot(x, y)

        a.set_title(self.get_title(), fontsize=32)
        a.set_ylabel("Sentiment Polarity", fontsize=16)
        a.set_xlabel("Scenes", fontsize=16)

        return fig

    # Get x values for the sentiment analysis
    def get_x_sentiment(self):
        x = []
        for i in range(len(self.divide_by_scenes())):
            x.append(i + 1)
        return x

    # Sort characters by key
    def sort_characters(self):
        d = self.get_characters()
        sorted_d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
        return sorted_d

    def top_5_characters(self):
        a = self.get_characters()
        b = sorted(a, key=a.get, reverse=True)
        b = b[:5]
        return b

    def top_5_characters_values(self):
        characters = self.get_characters()
        fives = self.top_5_characters()
        b = []
        for character in fives:
            a = characters.get(character)
            b.append(a)
        return b

    # Characters bar graph
    def plot_characters(self):
        x = self.top_5_characters()
        y = self.top_5_characters_values()

        fig = Figure()
        a = fig.add_subplot(111)
        a.bar(x, y)

        a.set_title(self.get_title(), fontsize=32)
        a.set_ylabel("Appearances", fontsize=16)
        a.set_xlabel("Characters", fontsize=16)

        # ax = plt.subplot(111)
        # ax.bar(x, y, width=0.5, color='b', align='center')
        # ax.bar(x, z, width=0.5, color='g', align='center')
        # ax.bar(x, k, width=0.5, color='r', align='center')
        # ax.xaxis_date()

        return fig

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
    print(annie_hall.sort_characters())
    print(annie_hall.top_5_characters())
    print(annie_hall.top_5_characters_values())