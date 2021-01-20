#!/usr/bin/env python
# -*- coding:utf-8 -*-
# FileName: PlaceDemo.py
# Developer: Peter. w (peterwolf.wang@gmail.com)


#Sample Text "PengHu.txt" Source:
#https://bosstwo420.pixnet.net/blog/post/220559147-%E3%80%8E%E6%BE%8E%E6%B9%96%E8%87%AA%E7%94%B1%E8%A1%8C%E3%80%8F%E6%BE%8E%E6%B9%96%E6%99%AF%E9%BB%9E%E6%8E%A8%E8%96%A6%EF%BD%9E%E5%BF%85%E5%90%83%E7%BE%8E%E9%A3%9F%EF%BD%9E%E5%A4%A7

try:
    # Installed via pip install
    try:
        from .ArticutAPI import Articut
    except:
        from ArticutAPI import Articut
except:
    # Installed via git clone
    import sys
    sys.path.append("../..")
    from ArticutAPI import Articut

import json
from pprint import pprint

if __name__ == "__main__":

    try:
        #使用自己的斷詞額度。
        with open("../../account.info", "r") as f:
            userDICT = json.loads(f.read())
        username = userDICT["email"]
        apikey = userDICT["apikey"]
        atc = Articut(username=userDICT["email"], apikey=userDICT["apikey"])
    except:
        #使用免費的斷詞額度。
        #實體化 Articut()
        atc = Articut()

    #載入 Demo 用的文字
    with open("./PengHu.txt", encoding="utf-8") as f:
        contentLIST = [l.replace("\n", "") for l in f.readlines()]

    #呼叫 parse() ，把 "openDataPlaceAccessBOOL" 參數設為 True，並把回傳的結果交給 getOpenDataPlaceLIST() 處理。
    resultLIST = []
    for c in contentLIST:
        print("Processing:{}/{} >> {}".format(contentLIST.index(c)+1, len(contentLIST), c))
        resultDICT = atc.parse(c, openDataPlaceAccessBOOL=True)
        placeLIST = atc.getOpenDataPlaceLIST(resultDICT)
        placeLIST.sort()
        if placeLIST!=None:
            resultLIST.extend(placeLIST)
        else:
            pass

    #在畫面上顯示結果，並將結果存入 PlaceDetectionResultLIST.json 檔中。
    print("DetectionResult:\n")
    pprint(resultLIST)
    with open("./PlaceDetectionResultLIST.json", "w", encoding="utf-8") as f:
        json.dump(resultLIST, f, ensure_ascii=False)
