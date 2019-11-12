#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 11/12/2019 2:49 PM
# @Author  : Gene.Zhao
# @Site    : 
# @File    : table2json.py
# @Email   : genezhao@wisers.com
import json

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup


# rowspan是出现行合并的table，目前简单支持行合并


def table2json(content):
    """
    将html中的table转成json
    :param content:html字符串
    :return: table2json
    """
    soup = BeautifulSoup(content, "html.parser")
    rows = soup.find_all("tr")
    headers = {}
    thead = soup.find("thead")
    if thead:
        thead = thead.find_all("th")
        for cell_index in range(len(thead)):
            headers[cell_index] = thead[cell_index].text.strip().lower()
    data = []
    rowspan_index = []
    for row_index, row in enumerate(rows):
        cells = row.find_all("td")
        if thead:
            items = {}
            for cell in headers:
                items[headers[cell]] = cells[cell].text
        else:
            items = []
            for cell_index, cell in enumerate(cells):
                rowspan = cell.attrs.get('rowspan')
                if rowspan and rowspan.isdigit():
                    # 记录 出现rowspan的位置下标和值
                    rowspan_index.append((cell.text.strip(), cell_index))
                items.append(cell.text.strip())
        data.append(items)
    # 有rowspan,并且data有tbody
    if len(data) >= 2 and rowspan_index:
        head = data[0]  # 表格的thead
        index = 1  # 记录tbody数据在data里面的标
        for d in data[1:]:
            if len(d) < len(head):
                for i in rowspan_index:
                    # tbody数据插入rowspan
                    d.insert(i[1], i[0])
                    data[index] = d
            index += 1
    return json.dumps(data)
