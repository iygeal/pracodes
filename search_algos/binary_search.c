#include <stdio.h>

/**
 * binary_search - Function that searches for a value in an array
 * of integers using the Binary search algorithm
 * @array: pointer to the first element of the array
 * @size: number of elements in the array
 * @value: value to search for
 * Return: index where value is located or -1 if not found
 */

int binary_search(int *array, size_t size, int value)
{
	int left = 0;		  /* left index */
	int right = size - 1; /* right index */
	int middle;			  /* middle index */

	while (left <= right)
	{
		middle = left + (right - left) / 2;
		if (array[middle] == value)
			return (middle);
		if (array[middle] < value)
			left = middle + 1; /* Search right subarray */
		else
			right = middle - 1; /* Search left subarray */
	}
	return (-1); /* Value not found */
}

/**
 * main - Entry point
 * Return: Always 0
 */

int main(void)
{
	int array[] = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50};
	int size = sizeof(array) / sizeof(array[0]);
	int values[] = {45, 10, 35, 100};
	int i;
	int my_value = sizeof(values) / sizeof(values[0]);
	int index;

	for (i = 0; i < my_value; i++)
	{
		index = binary_search(array, size, values[i]);
		if (index == -1)
			printf("Value %d not found\n", values[i]);
		else
			printf("Value %d found at index %d\n", values[i], index);
	}
	return (0);
}
