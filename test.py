#coding=utf-8
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
import sys
sys.path.insert(0, base_dir)
# sys.path[0]=r"C:\Users\jackliu\Desktop"
# print sys.path
from callbacktest.f_login import login_user, login_required
from callbacktest.m_model import user

# login_user("jackliu")

print login_required()


