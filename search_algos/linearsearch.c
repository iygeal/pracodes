#include <stdio.h>
#include <stdlib.h>

/**
 * linear_search - searches for a value in an array of integers
 * using the Binary search algorithm
 * @array: pointer to the first element of the array
 * @size: number of elements in the array
 * @value: value to search for
 * Return: index where value is located or -1 if not found
 */

int linear_search(int *array, size_t size, int value)
{
	int i;

	if (array == NULL)
		return (-1);

	for (i = 0; i < size; i++)
	{
		if (array[i] == value)
			return (i);
	}
	return (-1);
}

/**
 * main - Entry point
 * Return: Always 0
 */

int main(void)
{
	int array[] = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50};
	int size = sizeof(array) / sizeof(array[0]);
	int values[] = {35, 10, 45};
	int value = sizeof(values) / sizeof(values[0]);
	int index;
	int i;

	for (i = 0; i < value; i++)
	{
		index = linear_search(array, size, values[i]);
		if (index == -1)
			printf("Value %d not found\n", values[i]);
		else
			printf("Value %d found at index %d\n", values[i], index);
	}
	return (0);
}
