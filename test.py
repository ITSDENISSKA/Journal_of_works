from requests import get, post, delete

# РАБОЧИЕ
print(get("http://127.0.0.1:5003/api/v2/users").json())
print(get("http://127.0.0.1:5003/api/v2/user/1").json())
print(post("http://127.0.0.1:5003/api/v2/users", json={'surname': "Бушенев",
                                                       'name': "Сава",
                                                       'age': 2,
                                                       'position': "раб",
                                                       "speciality": "хлопковые поля",
                                                       "address": "ленина 72",
                                                       "email": "суперпро11123111@1гмэил.ру",
                                                       "password": "суперпро"}).json())
print(delete("http://127.0.0.1:5003/api/v2/user/4").json())

# ОШИБКИ ВЫДАЮТ
print(get("http://127.0.0.1:5003/api/v2/user/111").json())
print(delete("http://127.0.0.1:5003/api/v2/user/411").json())
