
#include <stdio.h>
#include <string.h>

void vulnerable_function(int buffer_size) {
    char buffer[buffer_size];
    memset(buffer, 'A', buffer_size);
    buffer[buffer_size - 1] = '\0';
    printf("Buffer filled: %s\n", buffer);
}

int main() {
    int size = 64;
    vulnerable_function(size);
    return 0;
}
