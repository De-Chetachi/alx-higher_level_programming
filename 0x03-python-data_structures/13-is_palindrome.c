#include "lists.h"

/**
* reverse_listint - reverses a linked list
* @head: pointer to the head of the list
* Return: pointer to the new head of the list
*/

listint_t *reverse_listint(listint_t **head)
{
	listint_t *current, *next, *previous = NULL;

	current = *head;
	while (current)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}

	*head = previous;
	return (*head);
}

/**
* is_palindrome -  checks if a singly linked list is a palindrome.
* @head: pointer to the list
* Return: 0 or 1
*/

int is_palindrome(listint_t **head)
{
	listint_t *temp, *tail, *headd;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);
	headd = *head;
	temp = *head;
	tail = reverse_listint(head);
	while (headd->next != tail)
	{
		if (headd->n != tail->n)
		{
			return (0);
		}
		headd = headd->next;
		tail = tail->next;
	}
	return (1);
}
