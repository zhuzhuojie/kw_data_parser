"""
 Filters and sorts can only be configured by openpyxl but will need to be applied in applications like Excel. This is because they actually rearranges or format cells or rows in the range.


 This will add the relevant instructions to the file but will neither actually filter nor sort.

 결론 : 실제 파일에는 필터와 정렬되지 않는다.
"""

from openpyxl import Workbook

wb = Workbook()
ws = wb.active

data = [
    ["Fruit", "Quantity"],
    ["Kiwi", 3],
    ["Grape", 15],
    ["Apple", 3],
    ["Peach", 3],
    ["Pomegranate", 3],
    ["Pear", 3],
    ["Tangerine", 3],
    ["Blueberry", 3],
    ["Mango", 3],
    ["Watermelon", 3],
    ["Blackberry", 3],
    ["Orange", 3],
    ["Raspberry", 3],
    ["Banana", 3]
]

for r in data:
    ws.append(r)

ws.auto_filter.ref = "A1:B15"
ws.auto_filter.add_filter_column(1, ["Kiwi", "Apple", "Grape"])
ws.auto_filter.add_sort_condition("B2:B15")

wb.save("filtered.xlsx")