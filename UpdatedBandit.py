import matplotlib.pyplot as plt
import seaborn as sns
import random
import numpy as np

class ContextualBandit():

    def __init__(self, n_widgets, n_variations_per_widget):

        self.image_list = []
        self.text_list = []
        self.button_list = []
        self.widgets = n_widgets
        self.n_variations = n_variations_per_widget
        #self.contexts = contexts
        self.mu = 0
        self.variance = 1
        self.k = n_widgets ** n_variations_per_widget
        self.climbing_steps = n_variations_per_widget
        self.weights = np.random.normal(self.mu, self.variance, self.k)
        self.optimal_arm = {"Image" : 0, "Text" : 0, "Button" : 0}

    def random_arm(self):
        
        images_copy = self.image_list.copy()
        texts_copy = self.text_list.copy()
        buttons_copy = self.button_list.copy()
        
        random.shuffle(images_copy)
        random.shuffle(texts_copy)
        random.shuffle(buttons_copy)
        
        img = images_copy[0]
        text = texts_copy[0]
        button = buttons_copy[0]
        
        random_arm = {}
        random_arm["Image"] = img
        random_arm["Text"] = text
        random_arm["Button"] = button
        
        return "Random Layout: ", random_arm

    def random_widget(self):
        
        images_copy = self.image_list.copy()
        texts_copy = self.text_list.copy()
        buttons_copy = self.button_list.copy()
        
        random.shuffle(images_copy)
        random.shuffle(texts_copy)
        random.shuffle(buttons_copy)
        
        img = images_copy[0]
        text = texts_copy[0]
        button = buttons_copy[0]
        
        random_arm = {}
        random_arm["Image"] = img
        random_arm["Text"] = text
        random_arm["Button"] = button
        random_widget = list(random_arm.keys())[random.randint(0, self.widgets - 1)]
        #random_widget = list(random_arm.keys())[random.sample(widget_list, k=1)]
        return 'Random Widget: ', random_widget


    def highestVariationScore(self):

        
        images_copy = self.image_list.copy()
        texts_copy = self.text_list.copy()
        buttons_copy = self.button_list.copy()
        
        random.shuffle(images_copy)
        random.shuffle(texts_copy)
        random.shuffle(buttons_copy)
        
        img = images_copy[0]
        text = texts_copy[0]
        button = buttons_copy[0]
        
        random_arm = {}
        
        random_arm["Image"] = img
        random_arm["Text"] = text
        random_arm["Button"] = button
        random_widget = list(random_arm.keys())[random.randint(0, self.widgets - 1)]  
        image_score = 1
        text_score = 1
        button_score = 1

        fixed_arm = {}

        

        if (random_widget == "Image"):


            for i in range(len(self.image_list) + 1):

                maximum = self.weights[1]
                if (self.weights[i] > maximum):
                    maximum = self.weights[i+1]
            print("The Highest Image Variation Score = {}".format(maximum))
                    #print("Image Variation Score: {} = {}".format(images[i], weights[i] + image_score))
            fixed_arm["Image"] = maximum
            fixed_arm["Text"] = text
            fixed_arm["Button"] = button
            #print(fixed_arm)
            self.optimal_arm["Image"] = maximum

        if (random_widget == "Text"):

            for i in range(len(self.text_list) + 4):
                i = i + 4
                maximum = self.weights[4]
                if (self.weights[i] > maximum):

                    maximum = self.weights[i]
            print("The Highest Text Variation Score = {}".format(maximum))
                    #print("Text Variation Score: {} = {}".format(texts[i], weights[i+3] + text_score))
            fixed_arm["Image"] = img
            fixed_arm["Text"] = maximum
            fixed_arm["Button"] = button
            self.optimal_arm["Text"] = maximum
            #print(fixed_arm)

        if (random_widget == "Button"):

            for i in range(len(self.button_list) + 7):
                i = i + 7
                maximum = self.weights[7]
                if (self.weights[i] > maximum):

                    maximum = self.weights[i]
            print("The Highest Button Variation Score = {}".format(maximum))

            #fixed_arm["Image"] = img
            #fixed_arm["Text"] = text
            fixed_arm["Button"] = maximum
            self.optimal_arm["Button"] = maximum

        
        return self.optimal_arm


if __name__ == "__main__":

    bandit = ContextualBandit(3, 3)

    bandit.image_list = ["image1", "image2", "image3"]
    bandit.text_list = ["text1", "text2", "text3"]
    bandit.button_list = ["button1", "button2", "button3"]

    print(bandit.highestVariationScore())
