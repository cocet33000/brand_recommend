# -*- coding: utf-8 -*-

import re

import numpy as np
from bs4 import BeautifulSoup
import requests
import pandas as pd
import collections

# URLからbs4オブジェクトを生成
def openURL(URL: int):
    res = requests.get(URL)
    if res.status_code != requests.codes.ok:
        print('Error')
        return(False)
    return BeautifulSoup(res.text)


# bs4オブジェクトから着用ブランドのリストを取得
def getBrandList(snaps):
    BrandList = []
    for snap in snaps:
        BrandList.append(list(set(map(lambda x: x.text, snap.find_all(
            'a', attrs={'href': re.compile('^/snaps/brand')})))))
    return BrandList


# bs4オブジェクトから名前を取得
def getNameList(snaps):
    NameList = []
    for snap in snaps:
        NameList.append(snap.find('a')['title'])
    return NameList


def getuniqueList(df):
    uniqueList = []

    for columns in df.columns.values:
        uniqueList.extend(df[columns])

    return collections.Counter(uniqueList)
