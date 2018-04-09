#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - checks linked list for cycle
 * @list: listint_t linked list
 * Return: 0 if none, 1 if cycle found
 */
int check_cycle(listint_t *list)
{
	int idx;
	int i;
	listint_t *current = NULL;
	listint_t *checker = NULL;

	idx = 0;
	current = list;
	while (current)
	{
		i = 0;
		checker = list;
		while (i < idx)
		{
			if (checker == current)
				return (1);
			i++;
			checker = checker->next;
		}
		idx++;
		current = current->next;
	}
	return (0);
}
