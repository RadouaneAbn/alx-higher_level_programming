#include "lists.h"

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
	listint_t *fast = *head, *slow = *head;
	listint_t *new_head = NULL, *tmp;
	int is_poli = 1;

	if (slow == NULL || slow->next == NULL)
		return (is_poli);

	while (fast && fast->next)
	{
		fast = fast->next->next;

		tmp = slow->next;
		slow->next = new_head;
		new_head = slow;
		slow = tmp;
	}
	if (fast != NULL)
		slow = slow->next;

	while (new_head)
	{
		if (new_head->n != slow->n)
		{
			is_poli = 0;
			break;
		}
		slow = slow->next;
		new_head = new_head->next;
	}
	return (is_poli);
}
