#include "lists.h"

/**
 * check_cycle - checks for a cycle in a singly linked list
 * @list: pointer to the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fire, *ice;

	if (list == NULL)
		return (0);

	ice = list;
	fire = list->next;

	if (fire == NULL)
		return (0);

	while (fire != ice)
	{
		if (fire->next == NULL || fire->next->next == NULL)
			return (0);
		ice = ice->next;
		fire = fire->next->next;
	}
	return (1);
}
