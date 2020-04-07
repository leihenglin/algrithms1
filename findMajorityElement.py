# -*- coding: utf-8 -*-
"""
numbs = list(map(int,input().replace('[','').replace(']','').split(',')))
n = int(len(numbs)/2)
b = sorted(numbs)
print(b[n])
"""
"""
numbs = list(map(int,input().replace('[','').replace(']','').split(',')))
n = int(len(numbs)/2)
sortedNums = sorted(numbs)
print(sortedNums[n])
"""
"""
numbs = list(map(int,input().replace('[','').replace(']','').split(',')))
n = int(len(numbs)/2)

j = len(numbs)
if j==1:
    print(numbs[0])
    exit(0)
while j > 0:
    if j==n:
        print(numbs[j])
        break
    for i in range(0,j-1):
        if numbs[i]<numbs[i+1]:
            temp = numbs[i]
            numbs[i] = numbs[i+1]
            numbs[i+1] = temp
    j-=1
"""

"""
众数的定义，给的数据中一定会出现次数超过n/2的数，那么如果数组中一次删去两个不同的数，那么最后剩下来的数一定是众数，提供一种不用排序，时间复杂度O(n)，空间复杂度O(1)的AC方法 
import java.util.Scanner;
import static java.lang.System.in;
 
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(in);
        String[] str = sc.nextLine().replace("[", "").replace("]", "").split(",");
        int[] data = new int[str.length];
        for (int i = 0; i < data.length; i++) {
            data[i] = Integer.parseInt(str[i]);
        }
        if (data.length == 1 || data.length == 2) {
            System.out.println(data[0]);
            return;
        }
        int hp = 0;
        int flag = data[0];
        for (int i = 0; i < data.length; i++) {
            if (hp == 0) {
                flag = data[i];
                hp++;
            } else if (data[i] == flag) {
                hp++;
            } else{
                hp--;
            }
        }
        System.out.println(flag);
    }
}
"""