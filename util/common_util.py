#coding:utf-8
class CommontUtil:
    def is_contain(self,str_one,str_two):
        flag=None
        if str_one in str_two:
            flag=True
        else:
            flag=False
        return flag
if __name__ == '__main__':
    com=CommontUtil()
    str_one="123"
    str_two="1234"
    print com.is_contain(str_one,str_two)