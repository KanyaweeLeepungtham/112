#include <stdio.h>

int main() {
    int num;
    scanf("%d",&num);
    if(num%2 == 0){
    printf("even");
    }
    else{
    printf("odd");
    }
    return 0;
}

int demo1() {
    int score;
    scanf("%d",&score);
    if(score >100){
        return 0;
    }
    
    if(score>=80){
        printf("Grade A");
    }
    else if(score>=70){
        printf("Grade B");
    }
    else if(score>=60){
        printf("Grade C");
    }
    else if(score>=50){
        printf("Grade D");
    }
    else {
        printf("Grade F");
    }
    return 0;
}


int demo2() {
    int menu;
    scanf("%d",&menu);
    if (menu<= 3){
        printf("You chose Option %d",menu);
    }
    else{
        printf("Invalid option");
    }
    return 0;
}


int main() {
    int num;
     int ans;
    scanf("%d",&num);
    for(int i=1; i<=12;i++){
        ans =i*num;
        printf("%d x %d = %d \n",num,i,ans);
    }
    return 0;
}


int main() {
    int num;
    int sum;
    sum =0;
    scanf("%d",&num);
    for(int i=1; i<=num; i++){
        sum=sum+i;
    }
    printf("Sum = %d",sum);
    return 0;
}

int main() {
    int num;
    scanf("%d",&num);
    for(int i=1; i<= num; i--){
        num =num-1;
        printf("%d\n",num);
        if (num ==1){
            return 0;
        }
    }
}