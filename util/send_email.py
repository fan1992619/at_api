#coding:utf-8
#定义一个发送邮件的类（工具），因为要发邮件要有收件人，主题，内容等，所有要创建相关参数(self,user_list,sub,content)
#发送邮件的包
#构建邮件的格式
#构建一个服务器
import smtplib
from email.mime.text import MIMEText
class SendEmail:
    global send_user
    global email_host
    global password
    send_user="fan1992619@163.com"
    email_host="smtp.163.com"
    password="61904925fy"
    def send_mail(self,user_list,sub,content):
        #发件人
        user="fanyun"+"<"+send_user+">"
        #构建发送邮件格式内容：content 格式：_subtype='plain'因为用的是中文：_charset='utf-8'
        message=MIMEText(content,_subtype='plain',_charset='utf-8')
        #主题
        message['Subject']=sub
        #来自于谁
        message['From']=user
        #发送给谁
        message['To']=";".join(user_list)
        #创建服务
        server=smtplib.SMTP()
        #因为没有链接的服务器，所以制造一个全局变量
        server.connect(email_host)
        server.login(send_user,password)
        #来自于哪一个：user发送给谁：user_list 内容：message.as_string()
        server.sendmail(user,user_list,message.as_string())
        server.close()


    #创建一个主函数，告诉通过了多少，失败了多少
    def send_main(self,pass_list,fail_list):
        #因为要计算百分比，所以要用浮点类型float
        pass_num=float(len(pass_list))
        fail_num=float(len(fail_list))
        count_num=pass_num+fail_num
        #计算百分比的格式
        #%.2f:去小数点后两位 %%：取一个百分号“%” %(pass_num/count_num*100)要计算的表达式
        pass_result="%.2f%%" %(pass_num/count_num*100)
        fail_result = "%.2f%%" % (fail_num / count_num * 100)
        user_list = ['498904925@qq.com']
        sub = "接口自动化测试报告"
        content = "此次一共运行的接口个数为%s个，通过的个数为%s个，失败的个数为%s个，通过率为%s，失败率为%s" %(count_num,pass_num,fail_num,pass_result,fail_result)
        self.send_mail(user_list, sub, content)
if __name__ == '__main__':
    sen=SendEmail()
    sen.send_main([1,2,3,4],[1,2,3,4,5,6])
#因为是list类型

