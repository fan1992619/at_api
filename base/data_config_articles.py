class global_var:
	#case_id
	Title = '0'
	url = '1'
	content='2'
	img_url='3'
	img_content='4'
#获取title
def get_title():
	return global_var.Title
#获取url
def get_url():
	return global_var.url
#获取文章内容
def get_content():
	return global_var.content
#获取图片的url
def get_img_url():
	return global_var.img_url
def get_img_content():
	return global_var.img_content
