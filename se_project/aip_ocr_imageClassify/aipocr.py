from aip import AipOcr

APP_ID = '15033710'
API_KEY = 'DlD5SvVTyfzEbdNpOWZ6qQgG'
SECRET_KEY = 'j5hVIOaxWQq2g5bj6NWSXY4BaCP18TAO'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def image_text_recognize(filepath):
    image = get_file_content(filepath)
    """ 调用通用文字识别, 图片参数为本地图片 """
    message = client.basicGeneral(image);
    print(message)
    return message


# """ 如果有可选参数 """
# options = {}
# options["language_type"] = "CHN_ENG"
# options["detect_direction"] = "true"
# options["detect_language"] = "true"
# options["probability"] = "true"
#
# """ 带参数调用通用文字识别, 图片参数为本地图片 """
# client.basicGeneral(image, options)
#
# url = "http//www.x.com/sample.jpg"
def image_text_recognize_url(url):
    """ 调用通用文字识别, 图片参数为远程url图片 """
    message = client.basicGeneralUrl(url);
    print(message)
    return message
#
# """ 如果有可选参数 """
# options = {}
# options["language_type"] = "CHN_ENG"
# options["detect_direction"] = "true"
# options["detect_language"] = "true"
# options["probability"] = "true"
#
# """ 带参数调用通用文字识别, 图片参数为远程url图片 """
# client.basicGeneralUrl(url, options)
