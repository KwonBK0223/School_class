#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int getRandomNumber(int level);
void ShowQuestion(int level, int num1, int num2);
void success();
void fail();

int main(void) {
	//문이 5개 있고, 각 문마다 어려운 수식 퀴즈가 출제 (랜덤)
	//문제를 맞히면 통과, 틀리면 실패

	srand(time(NULL));
	int count = 0;  // 맞힌 문제 개수
	for (int i = 1; i =< 5; i++) {
		int num1 = getRandomNumber(i);
		int num2 = getRandomNumber(i);
		//printf("%d X %d ?", num1, num2);
		ShowQuestion(i, num1, num2);

		int answer = -1;
		scanf_s("%d", &answer);
		if (answer == -1) {
			printf("프로그램을 종료합니다.\n");
			exit(0);
		}
		else if (answer == num1 * num2) {
			success();
			count++;

		}
		else {
			printf("실패");
		}
	}
	printf("\n\n 당신은 5개의 비밀번호 중 %d개를 맞췄습니다. \n",count);

	return 0;
}

int getRandomNumber(int level) {
	return rand() % (level*7)+1 ;
}
void ShowQuestion(int level, int num1, int num2) {
	printf("\n\n\n######### %d 번째 비밀번호 #########\n", level);
	printf("\n\t%d x %d 는?\n\n", num1, num2);
	printf("#################################\n");
	printf("비밀번호를 입력하세요 (종로 : -1) >>");
}
void success() {
	printf("\n >> Good! 정답입니다.\n");
}
void fail() {
	printf("\n >> Fail! 오답입니다.\n");
}