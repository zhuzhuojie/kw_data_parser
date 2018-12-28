# openpyxl을 이용한 엑셀처리

openpuxl은 파이썬에서 xlsx, xlsm, xltx, xltm 파일들을 읽고 쓰는 라이브러리입니다. openpyxl은 현재도 지속적으로 업데이트 되고있는 라이브러리입니다.

## 샘플코드

```python
from openpyxl import Workbook
wb = Workbook()

# grab the active worksheet
ws = wb.active

# Data can be assigned directly to cells
ws['A1'] = 42

# Rows can also be appended
ws.append([1, 2, 3])

# Python types will automatically be converted
import datetime
ws['A2'] = datetime.datetime.now()

# Save the file
wb.save("sample.xlsx")
```

# 설치

* openpyxl 설치

```bash
$ pip install openpyxl 
```

pip를 이용하여 openpyxl을 설치합니다.

* dependency 라이브러리 설치

```bash
$ pip3 install pillow  
```

이미지 삽입시 필요한 pillow 이미지 관련 라이브러리를 설치합니다.


## 목차

1. [save, load](https://github.com/pjt3591oo/python-openpyxl-sample/tree/master/save_and_load)
2. [simple usage](https://github.com/pjt3591oo/python-openpyxl-sample/tree/master/simple_usage) 
3. [style](https://github.com/pjt3591oo/python-openpyxl-sample/tree/master/style)
4. [filter, sort](https://github.com/pjt3591oo/python-openpyxl-sample/tree/master/filter_and_sort)
5. [table](https://github.com/pjt3591oo/python-openpyxl-sample/tree/master/table)
6. [chart](https://github.com/pjt3591oo/python-openpyxl-sample/tree/master/charts) 
7. [comment](https://github.com/pjt3591oo/python-openpyxl-sample/tree/master/comments)