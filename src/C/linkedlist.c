#include "stdlib.h"
#include "stdio.h"
struct Node
{
	int x;
	struct Node* next;
};

int main(int argc, char const *argv[])
{
	/* code */
	struct Node * root;
	root = (struct Node *) calloc(1, sizeof(struct Node));
	root->x = 500;
	root->next = (struct Node *) calloc(1, sizeof(struct Node));
	printf("%d\n",root->x );
	free(root->next);
	free(root);
	printf("successfully freed!\n");
	return 0;
}