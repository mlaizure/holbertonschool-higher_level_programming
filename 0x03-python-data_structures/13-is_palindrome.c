#include "lists.h"

short int _is_palindrome(listint_t **start, listint_t *end);

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to head of list
 * Return: 0 if not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	if (!*head)
		return (1);

	return (_is_palindrome(head, *head));
}

/**
 * _is_palindrome - recurses through list to check if end equals start
 * @start: pointer to pointer to start of list
 * @end: pointer that gets moved to end of list
 * Return: 0 if not palindrome, 1 if it is
 */

short int _is_palindrome(listint_t **start, listint_t *end)
{
	if (!end)
		return (1);

	if (_is_palindrome(start, end->next) && (*start)->n == end->n)
	{
		*start = (*start)->next;
		return (1);
	}
	else
		return (0);
}
