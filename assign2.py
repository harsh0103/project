from operator import le
import pandas as pd
info={'Gender':['Male','Female','Male','Female','Female'],'Position':['Head','Asst.Prof','head','Asst.prof','Asst prof']}
df=pd.DataFrame(info)
print(df)
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
gender_encoded= le.fit_transform(df['Gender'])
encoded_position=le.fit_transform(df['Position'])
df['Encoded_Gender']=gender_encoded
df['Encoded_Position']=encoded_position
print(df)