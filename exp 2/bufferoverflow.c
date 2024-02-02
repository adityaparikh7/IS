// #include <stdio.h>
// #include <stdlib.h>
// int main(void)
// {
//     char *ptr = (char *)malloc(10 * sizeof(char));
//     char *dptr = (char *)malloc(10 * sizeof(char));
//     printf("Address of ptr = %d\n", (int)ptr);
//     printf("Address of dptr = %d\n", (int)dptr);
//     printf("Enter Input = ");
//     gets(ptr);
//     printf("\nValue inside ptr = ");
//     fputs(ptr, stdout);
//     printf("\nValue inside dptr = ");
//     fputs(dptr, stdout);
//     system(dptr);
// }


#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char *ptr = (char *)malloc(11 * sizeof(char));  // +1 for null terminator
    char *dptr = (char *)malloc(11 * sizeof(char)); // +1 for null terminator

    if (ptr == NULL || dptr == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return 1;
    }

    printf("Address of ptr = %p\n", (void *)ptr);
    printf("Address of dptr = %p\n", (void *)dptr);

    printf("Enter Input = ");
    gets(ptr);

    printf("\nValue inside ptr = %s", ptr);
    printf("\nValue inside dptr = %s", dptr);

    free(ptr);
    free(dptr);

    return 0;
}
