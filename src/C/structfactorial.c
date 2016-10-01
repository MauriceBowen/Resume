#include "stdlib.h"
#include "stdio.h"
struct Node
{
	int x;
	int countdown;
	struct Node * next;
};
int main(int argc, char const *argv[])
{
	/* code */
	int input, result=1;
	struct Node * nodeList = (struct Node *) calloc(1, sizeof(struct Node));
	input = atoi(argv[1]);
	printf("%d is the input\n", input);
	nodeList->countdown = input;
	nodeList->x = input;
	while(nodeList->countdown > 1)
	{
		nodeList->next = (struct Node *) calloc(1, sizeof(struct Node));
		nodeList->next->x = nodeList->x * (nodeList->x - 1);
		nodeList->next->countdown = nodeList->countdown - 1;
		printf("%d is the next number\n", nodeList->next->x  );
		nodeList = nodeList->next;
		result = nodeList->x;
	}
	printf("%d is the result\n", result );

	return result;
}