# 類神經網路作業2

:::info
資工三乙 406262462 羅韋杰
:::

### Report


| TrainAccuracies  | NeuronNum 5     | NeuronNum 10    | NeuronNum 15   | 
| ---------------- | --------------- | --------------- | -------------- |
| LearningRate 1.0 |     99.16%      |      99.16%     |     99.17%     |
| LearningRate 0.5 |     98.33%      |      98.33%     |     99.16 %    | 
| LearningRate 0.1 |     98.33%      |      98.33%     |     98.33%     |



| TestAccuracies   | NeuronNum 5     | NeuronNum 10    | NeuronNum 15   | 
| ---------------- | --------------- | --------------- | -------------- | 
| LearningRate 1.0 |     98.13%      |      96.66%     |     97.13%     | 
| LearningRate 0.5 |     96.66%      |      96.77%     |     98.96%     |
| LearningRate 0.1 |     96.66%      |      96.66%     |     96.66%     |




### 實驗心得

* 隨著NeuronNumber數量的增加，所需要的epoch數量也會增加，成正比關係
* 隨著LearningRate的下降，所需要的epoch數量也會上升，成反比關係
* 運行時間在LearningRate上有明顯的正相關
* 這次好難QQ