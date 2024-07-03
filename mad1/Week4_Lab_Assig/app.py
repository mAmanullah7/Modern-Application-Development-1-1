from flask import Flask , render_template , request
from numpy import average
import pandas as pd
import matplotlib.pyplot as plt

app=Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():
    if request.method=="POST":
        data=pd.read_csv('data.csv')

        if request.form.get("ID")!=''and request.form.get('id_value')!='':
            ID=request.form.get("ID")
            id=int(request.form.get('id_value')) 

            if ID=='student_id' and id in data['Student id'].tolist():
                
            
                lisst=data[data['Student id']==id]
                course_id=lisst[' Course id'].tolist()
                marks=lisst[' Marks'].tolist()
                total=sum(marks)
                return render_template('student.html',course_id=course_id,marks=marks,total=total,id=id)
                
                
            elif ID =='course_id' and id in data[' Course id'].tolist():
                
                lisst=data[data[' Course id']==int(request.form.get('id_value'))]
                maxs=max((lisst[' Marks']).tolist())
                avgs=average(lisst[' Marks'].tolist())
                plt.hist(lisst[' Marks'])
                plt.savefig('./static/histogram.png')
                plt.close()
                return render_template('course.html', maxs=maxs,avgs=avgs)
            
            else:

                return render_template('error.html')
        else:

            return render_template('error.html')
            
            
    

        
    elif request.method=="GET":
        return render_template('index.html')
if __name__=="__main__":
    app.run()