"""
题目描述
我们部门要排队唱歌，大家乱哄哄的挤在一起，现在需要按从低到高的顺序拍成一列，但每次只能交换相邻的两位，请问最少要交换多少次

输入描述:
第一行是N（N<50000）,表示有N个人
然后每一行是人的身高Hi（Hi<2000000,不要怀疑，我们以微米计数），持续N行，表示现在排列的队伍

输出描述:
输出一个数，代表交换次数。

#解决方法：寻找逆序对，或者用归并排序,快速排序，python会有运算速度过慢的问题
#include <bits/stdc++.h>
using namespace std;
 
int main(){
    int n, cnt=0;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++)
        cin>>a[i];
    for(int i=0;i<n;i++)
        for(int j=0;j<i;j++)
            if(a[j]>a[i])
                cnt++;
    cout<<cnt<<endl;
    return 0;
}
"""
if __name__=="__main__":
    n = int(input())
    His = []
    for i in range(n):
        His.append(int(input()))
    counts = 0
    for i in range(n):
        j=0
        while j < i:
            if His[i]<His[j]:
                counts +=1
            j+=1
    
    print(counts)