#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - detect a loop in a linked list
 * @list: list address
 *
 * Return: 1 on success
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = list;
	fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
