## 数据表
### 课程表 
| ID        | 课程标题(title)   | 课程图片(course_img)  | 难度等级(level(choice)) |
| --------   | -----:  | :----:  | ---- |
| 1     | Python全栈 |   img1 | 1 |
| 2     | Python周末 |  img2  | 2 |
| 3     | Linux运维  |  img3  | 3 |
### 课程详细 - 水平分表
| ID | why |  推荐课程 |
| ---- | ----: | ---- |
| 1 | 原因1 | 课程1,课程2 | 
| 2 | 原因2 | 课程2,课程3 | 
| 3 | 原因3 | 课程1,课程2 | 

### 章节 
| id | 所属课程(course) | 章节(num) | 章节名称(name) |
| ---- | ---- | ---- | ----| 
| 1 | 1 | 1 | 章节1 |
| 2 | 1 | 2 | 章节2 |
| 3 | 2 | 1 | 章节3 |

### 用户表
| id | 用户名 | 密码 |
|---| --- | ---|
| 1 | zhang | 000000 | 

### 用户token表
| id | 用户 | token |
|---| --- | ---|
| 1 | 1 | ssankjsndkaksdjandkd | 

## 迁移数据库
```python
 python manage.py makemigrations
 python manage.py migrate
```
## 创建超级管理员
```python
python manage.py createsuperuser
# username:root
# password:root@123
```
## api接口
```html
获取所有课程信息：http://127.0.0.1:8000/api/v1/course/
获取指定课程详细信息：http://127.0.0.1:8000/api/v1/course/2
用户登录: 'http://127.0.0.1:8000/api/v1/auth/',
微学位: 'http://127.0.0.1:8000/api/v1/micro/'
```
- 课程系列
> 查询所有的课程  
    &emsp; * http://127.0.0.1:8000/api/v1/course/  
    &emsp; * level变中文
         
> 查询课程详细   
    &emsp; * http://127.0.0.1:8000/api/v1/course/1/  
    &emsp; * 路由 as_view 是否添加参数，取决于视图继承的类  
    &emsp; * 序列化  
    &emsp; &emsp; - ModelSerializer  
    &emsp; &emsp; - depth: 递归查询，包括跨表字段，不推荐  
    &emsp; &emsp; - source: 查询one2one/fk/choice字段  
    &emsp; &emsp; - 自定义method：查询m2m字段
    
> 用户登录验证  
    &emsp; * http://127.0.0.1:8000/api/v1/auth/    
    &emsp; * 跨域简单和复杂请求    
    &emsp; * token  
    &emsp; &emsp; - update_or_create    
    
> 微职位  
    &emsp; * http://127.0.0.1:8000/api/v1/micro/  
    &emsp; * 认证组件  

- 深科技相关
	> 文章列表  
	
    > 文章详细  
     
    > 文章评论
       
	> 点赞 
	 
	> 收藏   


