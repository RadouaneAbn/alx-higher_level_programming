#include "lists.h"

/**
 * insert_node - this function inserts a number in a sorted linked list
 * @head: teh head of the linked list
 * @number: the number
 *
 * Return: return the address of the new node
 *	or NULL in case of failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *previous = NULL, *new = NULL;

	while (current)
	{
		if (number < current->n)
		{
			new = malloc(sizeof(listint_t));
			if (new == NULL)
				return (NULL);

			new->n = number;
			new->next = current;
			previous->next = new;
			return (new);
		}
		previous = current;
		current = current->next;
	}

	return (NULL);
}
