#include <stdio.h>
/**
* @file type_and_size.C
* @anchor Samuel Okunlade (samueleniola29@gmail.com)
* @brief entry function
* @version 0.1
* @date 2022-09-06
*
* @copyright copyright (c) 2022
*/

int add_two (int y, int x);

int main()
{
    //char
    char c = '1';
    // Print 'char is 1byte'
    printf("char is %c byte\n",c);
    add_two(2, 3);
    return (0);
}

int char_type () 
{
    //char
    char C = '1';
    //print 'char is 1 byte'
    printf("char is %c byte\n", C);
    
}

int add_two (int y, int x)
{
    int result = y + x;
    printf("%d\n", result);
    return (result);
}
