import pickle
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.applications.xception import Xception

    

class GenerateDescription():
    def __init__(self) -> None:

        self.max_length = 39

        self.model = load_model(r"Saved_model/model_1")

        with open("tokenizer.pkl","rb") as tk:
            self.tokenizer = pickle.load(tk)


    def _load_test(self,img_path):
        
        model = Xception( include_top=False,pooling="max")

        print(f"[info] Loading image from {img_path}")



        image = Image.open(img_path)
        image = image.resize((299,299))

        print(image.size)
  
        image = np.expand_dims(image, axis=0)
        

        image = image/127.5
        image = image - 1.0
            
        feature = model.predict(image)

            
        return feature


    def _word_for_id(self,integer):
        for word, index in self.tokenizer.word_index.items():
            if index == integer:
                return word
        return None


    def _generate_desc(self, photo) -> str:

        in_text = 'start'

        for _ in range(self.max_length):
            sequence = self.tokenizer.texts_to_sequences([in_text])[0]
            sequence = pad_sequences([sequence], maxlen=self.max_length)
            pred = self.model.predict([photo,sequence], verbose=0)
            pred = np.argmax(pred)
            word = self._word_for_id(pred)
            if word is None:
                break
            in_text += ' ' + word
            if word == 'end':
                break

        return in_text


    def generate(self,img):

        

        photo = self._load_test(img)
     
        description = self._generate_desc(photo)

        return description



if __name__ == "__main__":
    g = GenerateDescription()

    caption = g.generate(r"Sparks.png")

    print(caption)
