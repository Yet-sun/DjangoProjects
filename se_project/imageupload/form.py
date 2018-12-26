from django import forms


class UploadImageForm(forms.Form):
    """图像上传表单"""
    # text = forms.CharField(max_length=100)
    image = forms.ImageField(
        # label='请上传一张图片:',
    )


# class UserForm(forms.Form):
    # username = forms.CharField(max_length=50, min_length=3,
    #                            error_messages={'required': '用户名不能为空', 'min_length': '最少不能少于3个字符',
    #                                            'max_length': '最多不能超过50个字符'})
    # password = forms.CharField(max_length=50, min_length=3,
    #                            error_messages={'required': '密码不能为空', 'min_length': '最少不能少于3个字符',
    #                                            'max_length': '最多不能超过50个字符'})
    # name = forms.CharField(max_length=30, min_length=3,
    #                        error_messages={'required': '姓名不能为空', 'min_length': '最少不能少于3个字符',
    #                                        'max_length': '最多不能超过30个字符'})
    # # id = forms.AutoField(primary_key=True)
    # age = forms.IntegerField(error_messages={'required': '年龄不能为空'})
    # sex = forms.CharField(max_length=10, min_length=1, error_messages={'required': '性别不能为空', 'min_length': '最少不能少于1个字符',
    #                                                                    'max_length': '最多不能超过10个字符'})
