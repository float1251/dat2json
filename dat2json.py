from io import StringIO
import json


def dat2dic(dat):
    """
    dat形式の文字列をlistにして返す.
    [
        {
            "name": string,
            "mail": string,
            "datetime": datetime,
            "comment": string,
            "title": string     // index:0のものにだけある
        },
        ...
    ]
    @params: dat dat形式のstring
    @return list
    """
    d = StringIO(dat)
    val = []
    for line in d:
        ret = {}
        ret["name"], ret["mail"], ret["datatime"], ret["comment"], ret["title"] = line.split("<>")
        # 日付等の末尾のスペースを削除
        # 改行コードを削除する
        # 改行コードだけのときはtitleが不要なので削除する
        if ret["title"] != "\n":
            ret["title"] = ret["title"][:-1]
        else:
            del ret["title"]
        val.append(ret)
    return val


def dat2json(dat):
    "datをjsonにして返す"
    return json.dumps(dat2dic(dat))
