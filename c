include <stdio.h>
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
    float gpax;
    for(j=0;j<5;j++){
        gpax += student[j] /5;
    }
    printf("%f", gpax);
		int max=0;
		for(k=0; k<5;k++)
		{
		if(gpa>max)
		{
			max= gpa;
		}
		}
		print("%d",max);
    return 0;
}