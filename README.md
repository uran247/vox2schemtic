# vox2schemtic
Magica Voxelのデータファイル(.vox)をminecraftのschematicファイル(.schematic)に変換します。

# 使い方

前提条件としてバージョン3.9以上のpythonをインストールしてください


## インストール方法
```
git clone https://github.com/uran247/vox2schemtic.git
pip install PyYAML
pip install py-vox-io
pip install Python-NBT
```

## 変換
test.voxをconfig.yamlの変換ルールに従いtest.schematicに変換
```
python .\convert.py -c config.yaml -o test.schematic .\test.vox
```

## 変換表の書き方
以下のように「マインクラフトのblockid: magicavoxelのパレット番号のリスト」の対応を羅列していってください
```yaml:config.yaml
palletes:
  "minecraft:black_wool": [1, 9, 10]
  "minecraft:black_concrete": [5, 61]
  "minecraft:light_gray_wool": [33, 34, 35]
  "minecraft:green_wool": [41, 42, 43, 45]
  "minecraft:brown_wool": [49, 50, 51, 53]
  "minecraft:snow_block": [57]
  "minecraft:yellow_concrete": [65]
  "minecraft:blue_wool": [73]
  "minecraft:black_stained_glass": [249]
```

# よくある質問
- voxファイルを読み込めない
  - ライブラリのバグによりmagicavoxel0.99で保存されたデータは読み込めません、エクスポート機能を使いvoxで出力したデータは読み込めますのでそちらを使ってください
- 出力したschematicファイルを読み込めない
  - worldedit用のデータフォーマットで出力しているのでworldeditを使って読み込んでください
- modブロックも使える？
  - 試していませんがデータフォーマット上はmodブロックの扱いに違いはないので読み込めるかと思います
- 上付き半ブロックを使いたい
  - 変換表でブロックidを右記のような書き方にしてください"minecraft:sndesite_slab[type=top]"