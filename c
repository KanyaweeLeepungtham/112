#include <stdio.h>

struct student {
    char name[31];
    int age;
    float gpa;
};
float max = students[0].gpa;
 void find_max()
		{
    for (int k = 1; k < 5; k++) {
        if (students[k].gpa > max) {
            max = students[k].gpa;
        }
    }
		}
int main() {
    struct student students[5];
    int i;

    for (i = 0; i < 5; i++) {
        printf("Enter name, age, GPA for student %d: ", i+1);
        scanf("%30s %d %f", students[i].name, &students[i].age, &students[i].gpa);
    }

    float gpax = 0.0;
    for (int j = 0; j < 5; j++) {
        gpax += students[j].gpa;
    }
    gpax /= 5.0;

    printf("Average GPA: %.2f\n", gpax);



    printf("Max GPA: %.2f\n", max);

    return 0;
}

}