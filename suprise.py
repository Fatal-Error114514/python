import base64
encode_text = '''4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qGA4qCk4qCA4qCE4qKA4qCA4qCA4qCA4qCA4qCA4qCA4
            qCA4qCACuKggOKggOKggOKggOKggOKggOKggOKhoOKip+KjvuKjt+Kjv+Kjv+KjteKjv+KjhOKggOKggO
            KggOKggOKggOKggArioIDioIDioIDioIDioIDioIDiorDiorHiob/ioJ/ioJvioJvioInioJnior/io7/
            ioIDioIDioIDioIDioIDioIAK4qCA4qCA4qCA4qCA4qCA4qCA4qK44qO/4qGH4qOk4qOk4qGA4qKg4qGE
            4qO44qK/4qCA4qCA4qCA4qCA4qCA4qCACuKggOKggOKggOKggOKggOKggOKiqOKhvOKhh+KgiOKgieKjo
            eKggOKgieKiiOKjnuKggOKggOKggOKggOKggOKggArioIDioIDioIDioIDioIDioIDioIjioLHioqLioY
            TioIDio6zio6TioIDio77ioIvioIDioIDioIDioIDioIDioIAK4qCA4qCA4qCA4qCA4qCA4qCA4qCA4qK
            A4qGO4qGH4qCA4qCI4qO/4qK74qGL4qCA4qCA4qCA4qCA4qCA4qCA4qCACuKggOKggOKggOKggOKjgOKj
            pOKjtuKjv+Kjp+Kig+KggOKgoOKjtuKjv+Kiu+KjtuKjpOKjpOKjgOKggOKggOKggAriooDio6Tio7bio
            7/io7/io7/io7/io7/io7/ioaTioLHiooDio7nioIvioIjio7/io7/io7/io7/io7/io6bioIAK4qO+4q
            O/4qO/4qO/4qO/4qG/4qKb4qO/4qO/4qOn4qOU4qOC4qOE4qCg4qO04qO/4qO/4qO/4qO/4qO/4qO/4qG
            HCuKhv+Kjv+Kjv+Kjv+Kjv+Kjs+Kgq+KgiOKjmeKju+Khp+KglOKiuuKjm+Kjv+Kjv+Kjv+Kjv+Kjv+Kj
            v+Kjv+Khhwrio7/io7/io7/io7/io7/ioITioIDiooDio6jio7/ioa/ioK3ioq3io7bio7/io7/io7/io
            7/io7/io7/io7/ioYc='''

encode_word = '''TmV2ZXIgZ29ubmEgZ2l2ZSB5b3UgdXAKTmV2ZXIgZ29ubmEgbGV0IHlvdSBkb3duCk5ldmVyIGdvbm5hIHJ1
            biBhcm91bmQgYW5kIGRlc2VydCB5b3UKTmV2ZXIgZ29ubmEgbWFrZSB5b3UgY3J5Ck5ldmVyIGdvbm5hIHNheSBnb
            29kYnllCk5ldmVyIGdvbm5hIHRlbGwgYSBsaWUgYW5kIGh1cnQgeW91'''

encode_text = encode_text.replace('\n', '')
encode_word = encode_word.replace('\n', '')

decoded_string = base64.b64decode(encode_text).decode('utf-8')
decoded_word = base64.b64decode(encode_word).decode('utf-8')

print(decoded_string)
print(decoded_word)