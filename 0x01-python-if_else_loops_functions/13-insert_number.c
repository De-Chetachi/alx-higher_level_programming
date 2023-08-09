#include "lists.h"

/**
* node_index - finds the index where to insert a node in a sorted list
* @head: pointer to the node
* @number: the int data of the new node
* Return: the required index
*/

int node_index(listint_t **head, int number)
{
	int index = 0;
	listint_t *node_temp = *head;
	if (node_temp == NULL)
		return (index);

	while (node_temp->n < number && node_temp->next != NULL)
	{
		index++;
		node_temp = node_temp->next;
	}

	return index;
}

/**
* insert_node - inserts a node in a sorted array
* @head: pointer to the node
* @number: the int data of the new node
* Return: address of new node
*/

listint_t *insert_node(listint_t **head, int number)
{
	int index;
	listint_t *node_temp, *new_node;
	int i;

	index = node_index(head, number);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL || head == NULL)
		return (NULL);

	node_temp = *head;
	new_node->n = number;
	new_node->next = NULL;

	if (index == 0)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	i = 1;
	while (i < index)
	{
		node_temp = node_temp->next;
		i++;
	}
	new_node->next = node_temp->next;
	node_temp->next = new_node;
	return (new_node);
}
