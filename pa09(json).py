import json

strTest='''
    [
        {
            "name":"bob",
            "gender":"male",
            "birthday":"1992-10-18"
        },
        {
            "name":"Selina",
            "gender":"female",
            "birthday":"1995-10-18"
        }
    ]
    '''
print(type(strTest))
data=json.loads(strTest)
print(type(data))
with open("01.json","w") as file:
    file.write(json.dumps(data,indent=2))
    #file.write(json.dumps(data,indent=2,ensure_ascii=False)) 含中文的话用该语句