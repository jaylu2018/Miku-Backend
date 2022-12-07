data_list = [
    {
        "id": 1,
        "children": [
            {
                "id": 2,
                "children": [
                    {
                        "id": 3,
                        "children": [],
                        "create_time": "2022-12-08T00:42:11.938693+08:00",
                        "update_time": "2022-12-08T00:42:11.938744+08:00",
                        "name": "gddfgfdgg",
                        "owner": None,
                        "phone": None,
                        "email": None,
                        "desc": "",
                        "status": True,
                        "parent": 2
                    }
                ],
                "create_time": "2022-12-08T00:37:05.012922+08:00",
                "update_time": "2022-12-08T00:37:05.012963+08:00",
                "name": "53453453",
                "owner": None,
                "phone": None,
                "email": None,
                "desc": "",
                "status": True,
                "parent": 1
            }
        ],
        "create_time": "2022-12-08T00:36:52.312796+08:00",
        "update_time": "2022-12-08T00:36:52.312863+08:00",
        "name": "测试",
        "owner": None,
        "phone": None,
        "email": None,
        "desc": "为2312312",
        "status": True,
        "parent": None
    }
]


def delete_bad_key(badKey, dictionary):
    for key in list(dictionary.keys()):
        if key == badKey and dictionary[key] == []:
            del dictionary[key]
        elif type(dictionary[key]) == dict:
            delete_bad_key(badKey, dictionary[key])
        elif type(dictionary[key]) == list:
            for item in dictionary[key]:
                delete_bad_key(badKey, item)
    return dictionary


if __name__ == '__main__':
    data = [delete_bad_key('children', data) for data in data_list]
    for i in data:
        print(i)
