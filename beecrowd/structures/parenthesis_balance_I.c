#include <stdlib.h>
#include <stdio.h>

#define MAX_SIZE 1000

typedef struct
{
    char *values;
    int size;

} stack;

stack *par;

void push(stack *par_stack, char value)
{
    par_stack->values[par_stack->size++] = value;
}

void pop(stack *par_stack)
{

    par_stack->size--;
}

void print_stack(stack *par_stack)
{
    printf("size: %d ->", par_stack->size);
    for (int i = 0; i < par_stack->size; i++)
        printf("%c, ", par_stack->values[i]);
    printf("\n");
}

int main()
{

    int count = 100;
    par = malloc(sizeof(stack));
    par->values = malloc(sizeof(char) * MAX_SIZE);
    par->size = 0;
    int flag_incorrect = 0;
    char r = getchar();

    do
    {
        if (r == '(')
            push(par, '(');
        else if (r == ')')
        {
            if (par->size == 0)
                flag_incorrect = 1;
            pop(par);
        }

        if (r == '\n')
        {
            printf("%s\n", (par->size == 0 && flag_incorrect == 0) ? "correct" : "incorrect");
            par->size = 0;
            flag_incorrect = 0;
        }
        r = getchar();

    } while (r != -1);

    return 0;
}