#include <stdio.h>
#include <stdbool.h>

int main(void) {
        char username[10];
        bool is_admin = false;
        puts("Enter your username: ");
        gets(username);
        if (is_admin) {
                puts("PLACEHOLDER{THIS_IS_NOT_A_FLAG}\n");
        } else {
                puts("You are not the admin, no flag for you!\n");
        }        
}