#include <time.h>
#include <stdlib.h>
#include <stdio.h>

int main(void) {
	//srand(time(NULL));   // 난수 초기화
	//int num = rand() % 3+1; // 1~3 중 한개 뽑는다

	printf("난수 초기화 이전..\n");
	for (int i = 0; i < 10; i++)
		printf("%d ", rand() % 10);
	
	srand(time(NULL));
	printf("\n\n난수 초기화 이후..\n");
	for (int i = 0; i < 10; i++)
		printf("%d ", rand() % 10);

	return 0;
}