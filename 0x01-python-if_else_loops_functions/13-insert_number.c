#include "lists.h"
/**
 * insert_node - insert node into ordered linked list
 * @head: head of list
 * @number: node data
 * Return: pointer to new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	if (head == NULL)
		return (NULL);

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else if ((*head)->n > new->n)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		while (current->next && current->next->n < new->n)
			current = current->next;
		new->next = current->next;
		current->next = new;
	}
	return (new);
}
