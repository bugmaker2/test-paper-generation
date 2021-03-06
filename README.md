# 自动组卷评卷系统-Python课设

> Author：Baiyuan Qiu(Bugmaker)

## 运行环境

安装GUI库pyqt

```cmd
pip install pyqt5
```

题库三个文件为：

```
single choice.csv
cloze.csv
binery choice.csv
```

分别为单选、填空、判断题库。请将py文件与题库放置在同一文件夹中运行。



在文件夹中中运行如下cmd代码，或直接双击py文件即可运行

```python
python '.\Test paper generation.py'
```

## 功能简介

组卷评卷系统，利用本地或线上题库组成试卷（满分100分），在答题后进行评卷



点击```选择题库```可以切换线上和线下题库，由于时间原因，线上题库功能暂时没有完成

![测试图片](test.png)

### 组卷

#### 线下题库

读取文件夹内```single choice.csv```、```cloze.csv```、```binery choice.csv```文件，随机抽取题目，打乱顺序组成卷面。

#### 线上题库

与服务器连接，接收数据组成卷面。

> 该功能未完成
>
> 基本思路为：利用腾讯云服务器，编写socket服务端程序，利用```screen```让服务端持续运行，监听连接请求；组卷程序如果点选“线上题库”，则利用socket客户端程序连接服务端，接受文本并组卷

### 单选

单选有四个选项，四个选项为互斥的，点选其中一个进行选择，其他选项会自动取消

### 填空

直接在文本框内输入答案即可

### 判断

点选T（True）或F（False）进行选择

### 评卷

如果尚未组卷，点击提交按钮将会提示组卷

如果组卷后未完成试卷，将会提醒完成试卷

如果完成了试卷，将会与答案进行比对，最终返回成绩和一句鼓励的话。

## 联系方式

QQ：1061688677

个人网站：https://bugmaker.netlify.app/

本项目Repository（将在24号后上传）: https://github.com/bugmaker2/test-paper-generation

可能在后续更新socket连接功能
