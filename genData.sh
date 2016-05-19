#! /bin/bash

cd $1
tesseract -psm 8 code.font.exp0.tif code.font.exp0 box.train
unicharset_extractor code.font.exp0.box
echo font 0 0 0 0 0 > font_properties
shapeclustering -F font_properties -U unicharset  *.tr
mftraining -F font_properties -U unicharset -O banker.unicharset *.tr
cntraining *.tr

mv unicharset $2.unicharset
mv shapetable $2.shapetable
mv inttemp $2.inttemp
mv pffmtable $2.pffmtable
mv normproto $2.normproto
# 提高成功率
cp ../../eng/eng.unicharambigs .
cp ../../eng/eng.punc-dawg .
cp ../../eng/eng.word-dawg .
cp ../../eng/eng.number-dawg .
cp ../../eng/eng.freq-dawg .
# 生成语言文件
combine_tessdata $2.
