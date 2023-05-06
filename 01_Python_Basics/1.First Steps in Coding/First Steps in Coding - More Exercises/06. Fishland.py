price_skumriq = float(input())
price_caca = float(input())
kg_palamud = float(input())
kg_safrid = float(input())
kg_midi = int(input())
price_palamud = price_skumriq + (price_skumriq * 0.6)
price_safrid = price_caca + price_caca * 0.8
price_midi = 7.5
price = kg_palamud * price_palamud + kg_safrid * price_safrid + kg_midi * price_midi
print(f"{price:.2f}")