#include "lists.h"

/**
 * reverse_list - creates reversed linked list
 * @h1: list to reverse
 * @h2: reversed list
 */
void reverse_list(listint_t *h1, listint_t **h2)
{
	if (h1 == NULL)
		return;

	reverse_list(h1->next, h2);
	add_nodeint_end(h2, h1->n);
}

/**
 * is_palindrome - checks if list is palindrome
 * @head: head of list
 * Return: int 0 if not, 1 if so
 */
int is_palindrome(listint_t **head)
{
	listint_t *h2 = NULL;
	listint_t *forward = NULL;
	listint_t *backward = NULL;

	if (head == NULL || *head == NULL)
		return (1);

	reverse_list(*head, &h2);

	forward = *head;
	backward = h2;
	while (forward)
	{
		if (forward->n != backward->n)
		{
			free_listint(h2);
			return (0);
		}
		forward = forward->next;
		backward = backward->next;
	}
	free_listint(h2);
	return (1);
}
