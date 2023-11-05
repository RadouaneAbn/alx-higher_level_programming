#include "lists.h"

/**
 * add_node - this function adds a node at the beginning of
 *	a linked list
 * @head: the head of the linked list
 * @n: the integer
 *
 * Return: pointer to the new node
 *	or NULL in case of failure
 */

listint_t *add_node(listint_t **head, int n)
{
	listint_t *new = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = *head;
	*head = new;

	return (new);
}

/**
 * rev_list - this function create a reverse list of the given linked list
 * @head: the head of the new linked list
 * @current: pointer to the current node (or head) of
 *	the original linked list
 * Return: pointer to the head of the new reversed linked list
 *	or NULL in case of a failure
 */

listint_t *rev_list(listint_t **head, listint_t *current)
{

	while (current)
	{
		add_node(head, current->n);
		if (head == NULL)
			return (NULL);
		current = current->next;
	}
	return (*head);
}

/**
 * is_palindrome - this is a function that checks
 *	if a linked list is a polindrome
 * @head: the head of the linked list
 *
 * Return: 1 if a linked list is polidrome
 *	or 0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *tmp, *current_1 = *head, *head_2 = NULL;
	listint_t *current_2;
	int len_list, half_list, i;

	if (*head == NULL)
		return (1);
	tmp = *head;
	for (len_list = 0; tmp; len_list++)
		tmp = tmp->next;
	half_list = len_list / 2;

	tmp = *head;
	for (i = 0; i < half_list; i++)
		tmp = tmp->next;
	rev_list(&head_2, tmp);

	current_1 = *head;
	current_2 = head_2;

	for (i = 0; i < half_list; i++)
	{
		if (current_1->n != current_2->n)
		{
			free_listint(head_2);
			return (0);
		}
		current_1 = current_1->next;
		current_2 = current_2->next;
	}
	free_listint(head_2);
	return (1);
}
