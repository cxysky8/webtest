#利用tesserocr识别简单图形验证码
import tesserocr
from PIL import Image

imageTarget=Image.open(r"F:\code\pa\02\CheckCode.jpg")
#验证码转灰度、二值化操作
imageTarget=imageTarget.convert("L")
threshold=127
table=[]
for i in range(256):
    if i<threshold:
        table.append(0)
    else:
        table.append(1)
imageTarget=imageTarget.point(table,"1")
#转换结束，正常清晰的验证码不需以上代码
result=tesserocr.image_to_text(imageTarget)
print(result)