#include "lists.h"

/**
* is_palindrome -  checks if a singly linked list is a palindrome.
* @head: pointer to the list
* Return: 0 or 1
*/

int is_palindrome(listint_t **head)
{
	listint_t *temp, *temp_;
	int i, j, k, len, *array = NULL;

	if (head == NULL || *head == NULL)
		return (1);
	temp = *head;
	temp_ = *head;
	len = 0;
	while (temp)
	{
		len++;
		temp = temp->next;
	}
	array = malloc(sizeof(int) * (len));

	for (i = 0; temp_; i++)
	{
		array[i] = temp_->n;
		temp_ = temp_->next;
	}
	j = len - 1;
	for (k = 0; k < (len / 2); k++)
	{
		if (array[k] != array[j])
		{
			free(array);
			return (0);
		}
		j--;
	}
	free(array);
	return (1);
}
