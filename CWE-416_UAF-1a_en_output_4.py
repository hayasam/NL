
#include <stdio.h>
#include <string.h>

void vulnerable_function(int buffer_size) {
    char buffer[buffer_size];
    memset(buffer, 'A', buffer_size);
    printf("Buffer filled with 'A's\n");
}

int main() {
    int size = 64;
    vulnerable_function(size);
    return 0;
}
