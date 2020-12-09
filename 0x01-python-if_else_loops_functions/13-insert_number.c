#include "lists.h"

/**
 * insert_node - inserts number into sorted singly linked list
 * @head: head of the linked list
 * @number: number to be inserted
 * Return: address of the new node or NULL on failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *p = *head;

	if (!new)
		return (NULL);

	new->n = number;

	while (p->next && p->next->n < number)
		p = p->next;

	if (p == *head)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		new->next = p->next;
		p->next = new;
	}
	return (new);
}
