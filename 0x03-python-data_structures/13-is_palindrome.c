#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

void reverse_list(listint_t **head);
int compare_lists(listint_t *list1, listint_t *list2);

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to a pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head) {
    listint_t *slow = *head, *fast = *head;
    listint_t *prev_slow = NULL, *mid = NULL, *second_half = NULL;
    int is_palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return 1;

    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    if (fast != NULL) {
        mid = slow;
        slow = slow->next;
    }

    second_half = slow;
    prev_slow->next = NULL;
    reverse_list(&second_half);
    is_palindrome = compare_lists(*head, second_half);
    reverse_list(&second_half);

    if (mid != NULL) {
        prev_slow->next = mid;
        mid->next = second_half;
    } else {
        prev_slow->next = second_half;
    }

    return is_palindrome;
}

/**
 * reverse_list - reverses a linked list
 * @head: pointer to a pointer to the head of the list
 */
void reverse_list(listint_t **head) {
    listint_t *prev = NULL, *current = *head, *next;

    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
}

/**
 * compare_lists - compares two linked lists
 * @list1: pointer to the head of the first list
 * @list2: pointer to the head of the second list
 * Return: 1 if lists are equal, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2) {
    while (list1 != NULL && list2 != NULL) {
        if (list1->n != list2->n)
            return 0;
        list1 = list1->next;
        list2 = list2->next;
    }

    return (list1 == NULL && list2 == NULL);
}
