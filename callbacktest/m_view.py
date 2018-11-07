#coding=utf-8
import sys
print sys.path
sys.path.append("..")
print sys.path
from f_login import login_user, login_required
import m_model

# login_user("1", "jackliu")

print login_required()

# import sys
# print sys.path
