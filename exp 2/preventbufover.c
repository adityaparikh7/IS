#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 11 

int main(void)
{
    char *ptr = (char *)malloc(BUFFER_SIZE * sizeof(char));  
    char *dptr = (char *)malloc(BUFFER_SIZE * sizeof(char)); 

    if (ptr == NULL || dptr == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return 1;
    }

    printf("Address of ptr = %p\n", (void *)ptr);
    printf("Address of dptr = %p\n", (void *)dptr);

    printf("Enter Input = ");
    if (fgets(ptr, BUFFER_SIZE, stdin) == NULL) {
        fprintf(stderr, "Error reading input\n");
        return 1;
    }

    size_t len = strlen(ptr);
    if (len > 0 && ptr[len - 1] == '\n') {
        ptr[len - 1] = '\0';
    }

    printf("\nValue inside ptr = %s\n", ptr);
    printf("Value inside dptr = %s\n", dptr);

    free(ptr);
    free(dptr);

    return 0;
}
