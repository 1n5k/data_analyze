import pandas as pd

mv = pd.read_csv('ALL_animes.csv')

pd.options.display.max_rows = 20

print(mv.query('title.str.contains("ご注文")', engine="python"))
