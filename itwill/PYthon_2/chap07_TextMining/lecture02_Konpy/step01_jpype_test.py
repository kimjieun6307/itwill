# -*- coding: utf-8 -*-
"""
JAVA 가상머신 사용을 위한 패키지 설치와 테스트
"""

import jpype

path = jpype.getDefaultJVMPath()
print(path)
# C:\Program Files\Java\jre1.8.0_151\bin\server\jvm.dll
# => 정상적으로 설치 되었음. 정상적으로 동작함.

