#include <stdio.h>

union FloatUnion {
    float floatValue;
    unsigned char byte[4];
};

int main() {
    float number = 2.5;

    union FloatUnion u;
    u.floatValue = number;

    for(int i = 0; i<4; i++)
    {
        printf("\n %d \n", u.byte[i]);
    }

// populating the bytes:
    u.byte[0] = 0;
    u.byte[1] = 0;
    u.byte[2] = 32;
    u.byte[3] = 64;

    printf("\n %f \n", u.floatValue);

// to print the address of the variables in the union ( the address would be same.)
    printf("address of float number: %p \n", (void *)&u.floatValue);
    printf("address of float number: %p \n", (void *)&u.byte);

    return 0;
}
