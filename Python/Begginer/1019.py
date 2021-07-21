# -*- coding: utf-8 -*-

duration = int(input()) #seconds

hours = duration // 3600
minutes = (duration % 3600) // 60 
seconds = ((duration % 3600) % 60)

print(f"{hours}:{minutes}:{seconds}")

