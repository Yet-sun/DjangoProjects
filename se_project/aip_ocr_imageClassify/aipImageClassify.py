from aip import AipImageClassify

APP_ID = '15048481'
API_KEY = 'u2DM6qVpSWfrWd8VarqCAynL'
SECRET_KEY = 'IKni8DCB5Z2CBjPaQMXfONyGRKC8LyBj'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def imageClassify(fielpath):
    image = get_file_content(fielpath)

    """ 调用通用物体识别 """
    message = client.advancedGeneral(image);
    print(message)
    return message

def imageClassify_url(url):
    """ 调用通用图像识别, 图片参数为远程url图片 """
    message = client.advancedGeneralUrl(url);
    print(message)
    return message

# """ 如果有可选参数 """
# options = {}
# options["baike_num"] = 5
#
# """ 带参数调用通用物体识别 """
# client.advancedGeneral(image, options)
