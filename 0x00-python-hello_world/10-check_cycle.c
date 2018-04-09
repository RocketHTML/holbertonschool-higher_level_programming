#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks linked list for cycle
 * @list: listint_t linked list
 * Return: 0 if none, 1 if cycle found
 */
int check_cycle(listint_t *list)
{
	int idx = 0;
	int i;
	int size = 8;
	listint_t *current = NULL;
	listint_t **addrs = NULL;

	addrs = malloc(sizeof(listint_t *) * size);
	if (!addrs)
		return (1);
	current = list;
	while (current)
	{
		addrs[idx] = current;
		for (i = 0; i < idx; i++)
		{
			if (current == addrs[i])
			{
				free(addrs);
				return (1);
			}
		}
		idx++;
		if (idx == size)
		{
			size *= 2;
			addrs = realloc(addrs, size);
		}
		current = current->next;
	}
	free(addrs);
	return (0);
}
