import statistics

ondas = [3.5, 6.9, 4, 4.6, 2, 3.3]

media = statistics.mean(ondas)

print(media)

media_menor = filter(lambda onda: onda > statistics.mean(ondas), ondas)

print(list(media_menor))
