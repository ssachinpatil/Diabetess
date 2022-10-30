import json,pickle
from sys import stderr
import numpy as np
try:
    import config
except:
    pass

class diabetes():
    def __init__(self,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
        self.Glucose=Glucose
        self.BloodPressure=BloodPressure
        self.SkinThickness=SkinThickness
        self.Insulin=Insulin
        self.BMI=BMI
        self.DiabetesPedigreeFunction=DiabetesPedigreeFunction
        self.Age=Age

    def load_model(self):
        try:
            with open (config.MODEL_FILE_PATH,"rb") as f:
                self.std_model=pickle.load(f)

            with open (config.JSON_FILE_PATH,"r") as m:
                self.json_data=json.load(m)
        except:

            with open ("model.pkl","rb") as f:
                self.std_model=pickle.load(f)

            with open ("json_data.json","r") as m:
                self.json_data=json.load(m)

    def prediction(self):
        self.load_model()

        array=np.zeros(len(self.json_data["columns"]))
        
        array[0]=self.Glucose
        array[1]=self.BloodPressure
        array[2]=self.SkinThickness
        array[3]=self.Insulin
        array[4]=self.BMI
        array[5]=self.DiabetesPedigreeFunction
        array[6]=self.Age

        print("array",array)
        predict=self.std_model.predict([array])
        print(predict[0])
        return predict
if __name__=="__main__":
    dia=diabetes(100,129,23,94,28.1,0.167,21)
    dia.prediction()

