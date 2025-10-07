#include <stdio.h>
#include <string.h>
struct student{
    char name;
    int age;
    int gpa;
};
int main() {
    for (int i=0;i<5;i++){
        scanf("%30s %d %.2f",&student[i].name,&student[i].age,&student[i].gpa);
    }
    float gapx;
    for(j=0 j<5;j++){
        gpax += student[j] /5;
    }
    printf("%f", gpax)
    return 0;
}