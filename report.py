#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pandasのインポート
import pandas as pd

# ALL_animes.csvを読み込む
df = pd.read_csv('ALL_animes.csv')

# 検索するアニメのタイトルを変数に格納
anime = "攻殻機動隊"

# 変数animeと部分一致するタイトルをkoukau_dfに格納
partial_match_anime_df = df[df['title'].str.contains(anime)]

# koukaku_df変数から、タイトル、開始年月日、終了年月日の表示
print(partial_match_anime_df.loc[:, ['title', 'started_year', 
'started_month', 
'started_day', 'ended_year','ended_month', 'ended_day']])
