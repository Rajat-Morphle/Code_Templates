#include <stdio.h>

union FloatUnion {
    float floatValue;
    unsigned char byte[4];
};

int main() {
    float number = 210;

    union FloatUnion u;
    u.floatValue = number;

    for(int i = 0; i<4; i++)
    {
        printf("\n %d \n", u.byte[i]);
    }

// populating the bytes:
    u.byte[0] = 0x00;
    u.byte[1] = 0x00;
    u.byte[2] = 0xB4;
    u.byte[3] = 0x42;

    printf("\n %f \n", u.floatValue);

// to print the address of the variables in the union ( the address would be same.)
    printf("address of float number: %p \n", (void *)&u.floatValue);
    printf("address of float number: %p \n", (void *)&u.byte);

    return 0;
}
