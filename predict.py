# -*- coding: utf-8 -*-

import re

from bs4 import BeautifulSoup
import requests
import pandas as pd
import collections


def bays(model, A, B=None):
    pB = (model == B).sum().sum()
    pAB = (((df == A) | (df == B)).sum(axis=1) > 1).sum()
    return pAB / pB


def predict(df, brand_df, wear, k=3):
    prob = []

    for brand in brand_df.index:
        prob.append(bays(df, brand, wear))

    best_k = sorted(range(len(prob)), key=lambda i: prob[i], reverse=True)[:k]
    return list(map(lambda k: brand_df.index[k], best_k))
