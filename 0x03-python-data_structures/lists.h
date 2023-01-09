#ifndef LISTNEW
#define LISTNEW
#include <stdio.h>
#include <stdlib.h>
size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
int is_palindrome(listint_t **head);
#endif
