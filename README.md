# GSII_findoptval
芝浦工業大学柏高等学校における
GSIIの研究「遺伝的アルゴリズムの効率的なパラメータについて」にあたって作成したソースコードのリポジトリです。

## 各ファイルの説明
<pre>
.
├── onemax Onemax問題のソースコード
│   ├── findoptval.py onemax問題に対するパラメータの最適解を求める
│   └── fitness.py 評価関数(onemax問題に基づいたもの)
├── knapsack
│   ├── findoptval.py knapsack問題に対するパラメータの最適解を求める
│   └── fitness.py 評価関数(knapsack問題に基づいたもの) 
├── tsp 巡回セールスマン問題のソースコード
│   ├── findoptval.py tsp問題に対するパラメータの最適解を求める
│   └── fitness.py 評価関数(tsp問題に基づいたもの) 
└── weightedonemax weighted onemax問題のソースコード
    ├── findoptval.py weighted onemax問題に対するパラメータの最適解を求める
    └── fitness.py 評価関数(weighted onemax問題に基づいたもの)
</pre>

## ライセンス
本リポジトリはMITライセンスのもとで公開されています。

## 今後の計画
今回の研究では、自分はOnemax問題とWeighted Onemax問題という比較的考察のしやすい問題にしか焦点を当てなかった。
そこで、更に他の問題に対してもデータを取って問題の構造についての分析を進め、任意の問題に対して最適なパラメータを動的に考える[1]メタ遺伝的アルゴリズムという仕組みについて研究していきたい。
そして遺伝的アルゴリズムは進化的アルゴリズムの一種であるため、そこから生命の進化についても考えることができたら面白いと感じる。
[1]:https://ieeexplore.ieee.org/document/6253010