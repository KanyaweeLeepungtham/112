#include <stdio.h>
#include <string.h>

struct student {
    char name[31];
    int age;
    float gpa;
};

void find_max(struct student students[], int n) {
    float max = students[0].gpa;
    int max_index = 0;

    for (int k = 1; k < n; k++) {
        if (students[k].gpa > max) {
            max = students[k].gpa;
            max_index = k;
        }
    }

    printf("Max GPA: %.2f %s\n", max, students[max_index].name);
}

int main() {
    struct student students[5];
    int i;

    for (i = 0; i < 5; i++) {
        scanf("%30s %d %f", students[i].name, &students[i].age, &students[i].gpa);
    }

    float gpax = 0.0;
    for (int j = 0; j < 5; j++) {
        gpax += students[j].gpa;
    }
    gpax /= 5.0;

    printf("Average GPA: %.2f\n", gpax);

    find_max(students, 5);

    return 0;
}
