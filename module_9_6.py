def all_variants(text):
    str_len = 1
    str_pos = 0
    while str_len <= len(text):
        if str_pos + str_len <= len(text):
            yield text[str_pos:str_pos + str_len]
        else:
            str_len += 1
            str_pos = 0
            continue
        str_pos += 1


a = all_variants("abc")
for i in a:
    print(i)
