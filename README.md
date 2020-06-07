# kanji_res
漢字のピンインと日本の音読みの対応法則を知ることで、中国語学習に役立てる。

### どういうものか

あるピンインを持つ漢字が、どういう日本語の音読みに対応しているかを把握する。

わかることの例を書く。

例えば、ianで終わるピンインの漢字はほとんど音読みのエンでおわる。

別の例では、j,q,xで始まるピンインの漢字は、日本語ではほとんどカ行かサ行で始まる。

### 考慮に入れる漢字

https://ja.wikibooks.org/wiki/%E4%B8%AD%E5%9B%BD%E8%AA%9E%E3%81%AE%E5%B8%B8%E7%94%A8%E6%BC%A2%E5%AD%97

このサイトにある、中国の小学生が学ぶ約2500の常用漢字を対象とする。

### できたファイル

cjiten.txt : それぞれの漢字のピンインを格納したファイル。

kanwa.txt : それぞれの漢字の音読みを格納したファイル。

pinin_table.txt : 声調つきピンインと声調なしピンインの対応テーブル。

### 使い方

リポジトリに含まれていた、cjiten.txt,kanwa.txt,pinin_table.txtを使うことにする。自分でファイルを作る場合は後で解説する。

input.txtに声調なしのピンインを並べる。

以下のスクリプトを実行すると、input.txtに対応する漢字の、声調つきピンインと、日本語の音読みをプリントする。

```
python3 9_make_list.py
```

結果の例は、RESULTディレクトリにある。RESULT/memo.txtに得られた知見が書いてある。

### 自分でデータファイルを作る

Selenium Web DriverというWebページを自動巡回するソフトウェアを使って、辞書サイトなどから自動でデータを取得する。

まず、このリポのcjiten.txt,kanwa.txt,zh_jyouyou.txt,pinin_table.txt,wiktionary_complete.txtを削除する。

```

python3 1_get_wiki_jyouyou.py > zh_jyouyou.txt

python3 -u 2_get_cn_jiten_pinin.py | tee cjiten.txt

python3 6_get_pinin_table.py > pinin_table.txt

python3 8_get_onyomi.py > kanwa.txt


```

3から5のget_wiktionaryで始まるスクリプトは今回は使用しなかったので飛ばした。

少しゴミ取りが必要。
