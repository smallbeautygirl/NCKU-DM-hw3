# Data Mining HW3 Report

:girl: P77111037 樊紹萱

## :one:  Implementation detail

:star: 解釋你是怎麼實作這三個演算法、三個演算法的原理（可比較相同或不同處）

| Algorithm | 原理 | 實作方式 |
| ---- | ---------- | ------ |
| HITS | :black_small_square: 透過計算該節點**被多少個節點指到**，以及該節點**指向多少個節點**，來計算該節點的權重 | :black_small_square: 每一個 iteration 時，會先計算所有節點的 authority & hub <br> :small_red_triangle:  Authority = Sum(該節點所有的父節點的 Hub 值) :small_red_triangle:  Hub = Sum(該節點所有的子節點的 Authority 值)<br> :black_small_square: 接著進行標準化<br>  :small_red_triangle:  Authority = 該節點未標準化前的authority / 未標準化前所有節點的Authority總和<br> :small_red_triangle:  Hub = 該節點未標準化前的Hub / 未標準化前所有節點的Hub總和 |
| PageRank | :black_small_square: PageRank 是指網頁被看到的可能性，每個網頁都有個別的 PageRank，取決於網頁間連結關係<br>:bulb: 一個網站的 PageRank 值，來自於**加總所有連結到該網站的網站的PageRank 值除以本身的導出連結數** |  |
| SimRank  |  |  |

以下分別用七張圖去解釋 HITS、PageRank、SimRank

### :world_map:  Graph 1

![graph-1](graph-image/graph-1.png)
| Algorithm | Result | Explanation |
| --------- | ----- | ------------ |
HITS | Authority: [0.0 0.2 0.2 0.2 0.2 0.2]<br> Hub: [0.2 0.2 0.2 0.2 0.2 0.0] | :bulb:發現到 node1 的 **authority 是 0**，因為 node1 沒有被任何節點指到<br>:bulb:發現到 node6 的 **hub 是 0**，因為 node6 沒有指到任何節點 |
PageRank | <font color="pink">0.003210</font> | <font color="green">0.001221</font> | 0.001474 |

### :world_map:  Graph 2

![graph-2](graph-image/graph-2.png)

### :world_map:  Graph 3

![graph-3](graph-image/graph-3.png)

### :world_map:  Graph 4

![graph-4](graph-image/graph-4.png)

### :world_map:  Graph 5

![graph-5](graph-image/graph-5.png)

### :world_map:  Graph 6

![graph-6](graph-image/graph-6.png)

### :high_brightness: HITS

| Algorithm | Paper Name | Author |
| ---- | ---------- | ------ |
| HITS | [LeNet](http://yann.lecun.com/exdb/publis/pdf/lecun-01a.pdf) | Yann LeCun |
| PageRank | [AlexNet](https://proceedings.neurips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf) | Alex Krizhevsky |
| SimRank  | [AlexNet](https://proceedings.neurips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf) | Alex Krizhevsky |

## :three: :stopwatch: Computation performance analysis

:star: 對 dataset 中的圖1到5，計時每張圖在三個演算法上的秒數。並試著解釋為什麼某些演算法或某些圖要跑特別久。

| Graph | HITS<br>:stopwatch:Time <br> **second** | PageRank<br>:stopwatch:Time <br> **second** | SimRank<br>:stopwatch:Time <br> **second** |
| --------- | ----- | -------------- | ----------- |
1 | <font color="pink">0.002520</font> | <font color="green">0.001192</font> | 0.001477 |
2 | <font color="pink">0.003210</font> | <font color="green">0.001221</font> | 0.001474 |
3 | <font color="pink">0.003011</font> | 0.001218 | <font color="green">0.001154</font> |
4 | <font color="pink">0.002703</font> | <font color="green">0.001078</font>  | 0.001954 |
5 | 0.018052 | 0.008929 | :warning:<font color="#FF0000">11.646827</font> |

:pencil: Explanation

graph_5.txt 用 SimRank 演算法的時候花費很久的時間
