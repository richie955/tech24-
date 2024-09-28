from django.shortcuts import render,HttpResponse
from .utils import finalOutput, MatrixOut, fillPrev


# Create your views here.
def home(request):
    return render(request,"index.html")

def handle(request):
    if request.method=="POST":
        input=request.POST.get("inputBox1")
        code=request.POST.get("inputBox2")
        x=request.POST.get("action")
        output=finalOutput(input, code, x)
        matrix = MatrixOut(code)
        # print(input,code)
        # output=input+ code
        return render(request,'signup.html',{'output_data': output,
                                             'output_data_1' : matrix[0],
                                             'output_data_2' : matrix[1],
                                             'output_data_3' : matrix[2],
                                             'output_data_4' : matrix[3],
                                             'output_data_5' : matrix[4],
                                             'output_data_6' : matrix[5],
                                             'output_data_7' : matrix[6],
                                             'output_data_8' : matrix[7],
                                             'output_data_9' : matrix[8],
                                             'output_data_10' :matrix[9], 
                                             'output_data_11' : matrix[10],
                                             'output_data_12' : matrix[11],
                                             'output_data_13' : matrix[12],
                                             'output_data_14' : matrix[13],
                                             'output_data_15' : matrix[14],
                                             'output_data_16' : matrix[15],
                                             'output_data_17' : matrix[16],
                                             'output_data_18' : matrix[17],
                                             'output_data_19' : matrix[18],
                                             'output_data_20' : matrix[19],
                                             'output_data_21' : matrix[20],
                                             'output_data_22' : matrix[21],
                                             'output_data_23' : matrix[22],
                                             'output_data_24' : matrix[23],
                                             'output_data_25' : matrix[24],
                                             'default1' : fillPrev(input, code)[0],
                                             'default2' : fillPrev(input, code)[1],
                                             }) 
    # output data is to be mentioned
    
    return render(request,"signup.html")


