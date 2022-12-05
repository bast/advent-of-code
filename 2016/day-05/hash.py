import hashlib


def password1(door_id):
    result = ""
    i = 0
    while True:
        s = f"{door_id}{i}"
        digest = hashlib.md5(s.encode("utf-8")).hexdigest()
        if digest.startswith("00000"):
            result += digest[5]
            if len(result) == 8:
                return result
        i += 1


def password2(door_id):
    result = {}
    i = 0
    while True:
        s = f"{door_id}{i}"
        digest = hashlib.md5(s.encode("utf-8")).hexdigest()
        if digest.startswith("00000"):
            if digest[5].isnumeric():
                n = int(digest[5])
                if n < 8:
                    if not n in result:
                        result[n] = digest[6]
                        if len(result.items()) == 8:
                            return "".join([result[i] for i in range(8)])
        i += 1


print("part 1:", password1("ffykfhsq"))
print("part 2:", password2("ffykfhsq"))
