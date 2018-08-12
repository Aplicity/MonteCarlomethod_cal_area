# MonteCarlomethod_cal_area
有如下一个问题，见下图，简单来说就是求粉红色三角形所占正方形的面积。
![image](https://github.com/Aplicity/MonteCarlomethod_cal_area/blob/master/question.png)

以上问题相信一般高年纪的小学生都能求解，初中生甚至可以利用三角相似的方法可以心酸出答案。但是我不行，我觉得这个图形很复杂，因此我想借助一些很粗暴的算法来求解。这个方法是 蒙特卡洛方法。

蒙特卡罗是一类随机方法的统称。这类方法的特点是，可以在随机采样上计算得到近似结果，随着采样的增多，得到的结果是正确结果的概率逐渐加大，但在（放弃随机采样，而采用类似全采样这样的确定性方法）获得真正的结果之前，无法知道目前得到的结果是不是真正的结果。

以求不规则图形的面积的应用下一个具体的定义：

在广场上画一个边长一米的正方形，在正方形内部随意用粉笔画一个不规则的形状，现在要计算这个不规则图形的面积，怎么计算列?蒙特卡洛(MonteCarlo)方法告诉我们，均匀的向该正方形内撒N（N 是一个很大的自然数）个黄豆，随后数数有多少个黄豆在这个不规则几何形状内部，比如说有M个，那么，这个奇怪形状的面积便近似于M/N，N越大，算出来的值便越精确。在这里我们要假定豆子都在一个平面上，相互之间没有重叠。

生成1万个点的时候，其图像如下：
![image](https://github.com/Aplicity/MonteCarlomethod_cal_area/blob/master/Figure_1.png)

生成10万个点的时候，其图像如下：
![image](https://github.com/Aplicity/MonteCarlomethod_cal_area/blob/master/Figure_2.png)

