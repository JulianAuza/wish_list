import django
from apps.wishlist.models import User

# Courses.objects.create(course_name = 'Super fun', desc ='YAS') ssssssss
User.objects.create(name = 'Kim Hyuna' ,email= 'wondergirls@jyp.com', password = '12345678' , user_name = '4minute')
# users = User.objects.all()
# for user in users:
#     print user.user_name, user.email_address,user.password