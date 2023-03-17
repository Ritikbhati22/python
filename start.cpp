#include<iostream>
using namespace std;
int print(int a,int b){
    if(a<b){
        return print(b,a);
    }
    else if(b!=0){
        return(a*print(a,b-1));
    }
    else{
        return 0;
    }
}

int main(){tsc --version
    int a =5;
    int b =5;
   cout << print(a,b);

    }