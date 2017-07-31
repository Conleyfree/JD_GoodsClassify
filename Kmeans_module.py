# coding=utf-8
# created by czc on 2017.7.19
import math


class kmeans:
    k = 2                                               # K值，簇的个数
    vec_set = []                                        # 传入待聚类的向量集合
    clusters = []                                       # 簇的集合
    clusters_ofIndex = []                               # 簇的集合以传入原文档集合的下标为表现形式
    centers = []                                        # 每个簇对应的质心点集合

    def __init__(self, k, vec_set):
        self.k = k
        self.vec_set = vec_set

    # 计算节点到簇的质心点的欧氏距离
    @staticmethod
    def getDistance(node, center):
        distance = 0.0
        for i in range(0, len(node)):
            dist = center[i] - node[i]
            distance += (dist * dist)
        return math.sqrt(distance)

    # 计算聚类中心
    def getCenterOfClusters(self):
        new_centers = []                                # 所有簇的新质心
        for cluster in self.clusters:
            new_center = []                             # 当前簇的新质心
            dimension = len(self.vec_set[0])            # 维度
            i, theSum = 1, 0.0
            while i <= dimension:                       # 同簇中所有点同维度坐标的均值
                for node in cluster:
                    theSum += node[i-1]
                if len(cluster) == 0:
                    print(self.clusters)
                new_center.append(theSum / float(len(cluster)))
                theSum = 0.0
                i += 1
            new_centers.append(new_center)
        return new_centers

    # 为节点寻找最近簇
    def node2cluster(self, node, index):
        min_distance = -1              # 当前点到各簇的最小距离
        cluster_index = -1             # 当前已知最近簇的下标
        i = 0

        # 遍历所有的簇的质心点，找出相似度最大的簇质心
        for center_node in self.centers:
            if cluster_index == -1:
                min_distance = self.getDistance(node, center_node)      # 计算欧氏距离
                cluster_index = 0
            else:
                distance = self.getDistance(node, center_node)
                if distance < min_distance:
                    min_distance = distance
                    cluster_index = i
            i += 1
        self.clusters[cluster_index].append(node)                   # 将结点加入对应的簇中
        self.clusters_ofIndex[cluster_index].append(index)

    # 比较两个质心集合是否相同
    @staticmethod
    def isSame(list1, list2):
        if list1 is None or list2 is None or not isinstance(list1, list) or not isinstance(list2, list):
            return -1                               # 传入参数错误
        if len(list1) == len(list2):
            for i in range(0, len(list1)):
                node1 = list1[i]
                node2 = list2[i]
                if isinstance(node1, list) and isinstance(node2, list):
                    if len(node1) == len(node2):
                        for j in range(0, len(node1)):
                            if node1[j] != node2[j]:
                                return 0                # 一旦检查到不相等的元素
                    else:
                        return 0
                else:
                    return -1                       # 传入参数错误
            return 1                                # 没有因为不相等的元素而被终止
        else:
            return 0

    # 开始训练
    def train(self):
        if len(self.vec_set) <= self.k:
            print("参数k值设置错误：大于训练集个数")
            return

        i = 0
        for node in self.vec_set:
            i += 1
            if i <= self.k:                             # 当 i 小于或等于 k 值时
                self.centers.append(node)               # 把当前的节点作为中心添加到质心点集合
                cluster_list = [node]                   # 创建一个集合保存一个簇
                cluster_list_ofIndex = [i-1]            # 将当前的下标添加入一个簇
                self.clusters.append(cluster_list)
                self.clusters_ofIndex.append(cluster_list_ofIndex)
            else:                                       # 当 i 大于 k 值时
                # print(self.centers)
                self.node2cluster(node, index=i)                 # node 需要寻找最近的质心点添加到对应的簇中
        # print("首次划分结果：", self.clusters)

        # 做重复划分，直到聚类中心不变为止
        new_centers = self.getCenterOfClusters()
        while self.isSame(new_centers, self.centers) != 1:      # 新划分的簇中心有变化
            # print("旧质心集合：", self.centers)
            # print("新质心集合：", new_centers)
            self.centers = new_centers
            self.clusters.clear()                               # 清空上一回合的聚类结果
            self.clusters_ofIndex.clear()
            for i in range(0, self.k):                          # 添加簇的集合
                cluster = []
                cluster_ofIndex = []
                self.clusters.append(cluster)
                self.clusters_ofIndex.append(cluster_ofIndex)
            i = 0
            for node in self.vec_set:
                self.node2cluster(node, index=i)
                i += 1
            new_centers = self.getCenterOfClusters()

        # print("旧质心集合：", self.centers)
        # print("新质心集合：", new_centers)
        print("训练结束：")
        return self.clusters_ofIndex            # 要返回保存文档下标的簇集合

    # 输出训练结果
    def show(self):
        if self.k != len(self.clusters):
            print("错误！还未训练模型！")
            return
        count = 0
        while count < self.k:
            print("簇 ", count, " ：")
            print(self.clusters[count])
            count += 1
