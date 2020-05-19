import json

import requests


def request_googleapi(title, author, isbn):
    """
    googleの書籍検索APIに問い合わせを行なう関数。
    title, author, isbnのうち、問い合わせに使用しない情報に対しては空文字列を引数に渡すこと
    title, author か isbn どちらかは必須項目

    params:
        title String: 書籍名
        author String: 著者
        isbn String: ISBNコード（10桁でも13桁でもOK）
    return:
        Dict: レスポンスから、必要情報のみをパースした辞書。
              書籍が見つからなかった場合も辞書が返るので、
              呼び出し元で`is_found`のboolのチェックが必要。
    """

    if isbn != "":
        res = requests.get(
            "https://www.googleapis.com/books/v1/volumes?q=isbn:%s" % (isbn)
        )
        return parse_info(json.loads(res.content))

    elif author != "" and title != "":
        res = requests.get(
            "https://www.googleapis.com/books/v1/volumes?q=inauthor:%s+intitle:%s"
            % (author, title)
        )
        return parse_info(json.loads(res.content))

    else:
        return parse_info({})


def parse_info(original_data):
    """
    google書籍検索APIのレスポンスから、必要情報のみをパースする関数

    params:
        original_data Dict: レスポンスを辞書に変換したもの。
                            空の辞書も受け付ける。
    return:
        base_info Dict: 結果の辞書
    """

    base_info = {
        "is_found": False,
        "title": "",
        "subtitle": "",
        "authors": [],
        "published_date": "",
        "description": "",
        "isbn13": "",
        "image_url": "",
    }

    if original_data == {} or original_data["totalItems"] == 0:
        return base_info


    if "title" in original_data["items"][0]["volumeInfo"]:
        base_info["title"] = original_data["items"][0]["volumeInfo"]["title"]
    if "subtitle" in original_data["items"][0]["volumeInfo"]:
        base_info["subtitle"] = original_data["items"][0]["volumeInfo"]["subtitle"]
    if "authors" in original_data["items"][0]["volumeInfo"]:
        base_info["authors"] = original_data["items"][0]["volumeInfo"]["authors"]
    if "publishedDate" in original_data["items"][0]["volumeInfo"]:
        base_info["published_date"] = original_data["items"][0]["volumeInfo"][
            "publishedDate"
        ]
    if "description" in original_data["items"][0]["volumeInfo"]:
        base_info["description"] = original_data["items"][0]["volumeInfo"]["description"]
    if "identifier" in original_data["items"][0]["volumeInfo"]["industryIdentifiers"][1]:
        base_info["isbn13"] = original_data["items"][0]["volumeInfo"][
            "industryIdentifiers"
        ][1]["identifier"]
    if "imageLinks" in original_data["items"][0]["volumeInfo"]:
        base_info["image_url"] = original_data["items"][0]["volumeInfo"]["imageLinks"][
            "thumbnail"
        ]

    base_info["is_found"] = True

    return base_info
