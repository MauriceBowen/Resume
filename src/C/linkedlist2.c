#include "stdio.h"
#include "stdlib.h"
struct Node
{
	int x;
	struct Node * next;
};
#define NODECOUNT 100
int main(int argc, char const *argv[])
{
	/* code */
	struct Node nodeArray[NODECOUNT];
	struct Node * temp;
	int i;
	//nodeArray = (struct Node *) calloc(NODECOUNT, sizeof(struct Node));
	
	for(i=0; i<NODECOUNT; i++)
	{
		temp = &nodeArray[i];
		temp->x = i;
		if (i==NODECOUNT-1)
		{
			temp->next = &nodeArray[0];
		}
		else
		{
			temp->next = &nodeArray[i+1];
		}
	}
	printf("node list created\n");
	printf("now to print the list\n");
	temp = &nodeArray[0];
	printf("%d\n", temp->x);
	temp = temp->next;
	while(temp->x != 0)
	{
		printf("%d\n", temp->x);
		temp = temp->next;
	}
	return 0;
}