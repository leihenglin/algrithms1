# -*- coding: utf-8 -*-
str1 = input()
n = len(str1)
count = 0
for i in range(n):
    for j in range(i+1,n):
        print(i,j)
        if str1[i:j]==str1[-n+j:-n+i:-1]:
            count+=1
        print(str1[i:j])
        print(str1[-n+j-1:-n+i-1:-1])
            

print(count+n)
            
"""


dp解法。记dp[i][j]为s索引从i到j的的子串是否为回文字符串。
若j-i>=2，那么dp[i][j]=dp[i+1][j-1]&&s[i]==s[j]；因此推断i的遍历为降序，而j的遍历为升序，又有i到j的子串，所以i<=j；    若j-i==1，dp[i][j]=s[i]==s[j]；    若j==i，dp[i][j]=true。
在求每个dp[i][j]时判断其是否为true，并记录true的个数即可。

	
#include<iostream>
#include<string>
#include<vector>
using namespace std;
int main()
{
    string s;
    cin>>s;
    int n=s.size();//字符串长度
    vector<vector<bool>> dp(n,vector<bool>(n,0));//dp[i][j] 从i到j的子串是否为回文串
    int res=0;//记录回文子串的个数
    for(int i=n-1;i>=0;i--)//i降序
        for(int j=i;j<n;j++)//j升序 且j>=i
        {
            if(i==j)
                dp[i][j]=true;//一个字母是回文字符串
            else if(j-i==1)//首尾相邻
            {
                if(s[i]==s[j])
                    dp[i][j]=true;//相同为回文
                else
                    dp[i][j]=false;//不同不为回文
            }
            else//首尾不相邻
            {
                if(dp[i+1][j-1]==true&&s[i]==s[j])//中间为回文且首尾相同为回文
                    dp[i][j]=true;
                else
                    dp[i][j]=false;//否则不为回文
            }
            if(dp[i][j]==true)
                res++;//记录回文子串的个数
        }
    cout<<res<<endl;
    return 0;
}
"""