# vox2schemtic
Magica Voxelのデータファイル(.vox)をminecraftのschematicファイル(.schematic)に変換します。

# 使い方

前提条件としてバージョン3.9以上のpythonをインストールしてください


## 事前準備
```
pip install PyYAML
pip install py-vox-io
pip install Python-NBT
```

## 変換
```
# 変換(test.voxをconfig.yamlの変換ルールに従いtest.schematicに変換)
python .\convert.py -c config.yaml -o test.schematic .\test.vox
```

## 変換表の書き方
以下のように"blockのid: magicavoxelのパレット番号のリスト"の対応を羅列していってください
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