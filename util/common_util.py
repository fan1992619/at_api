#coding:utf-8
class CommontUtil:
    def is_contain(self,str_one,str_two):
        flag=None
        if str_one in str_two:
            flag=True
        else:
            flag=False
        return flag
    #判断两个dict相不相等
    def is_equal_dict(self, dict_one, dict_two):
        '''
        判断两个字典是否相等
        '''
        if isinstance(dict_one, str):
            dict_one = json.loads(dict_one)
        if isinstance(dict_two, str):
            dict_two = json.loads(dict_two)
        return cmp(dict_one, dict_two)
if __name__ == '__main__':
    com=CommontUtil()
    dict_one={
        'code':0
    }
    dict_two={
        'code':0
    }
    print com.is_equal_dict(dict_one,dict_two)