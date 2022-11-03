#include <stdio.h>

int main(void) {
	//배열
	/*int subway_1 = 30;
	int subway_2 = 40;
	int subway_3 = 50;

	printf("지하철 1호차에 %d 명이 타고있습니다.\n", subway_1);
	printf("지하철 2호차에 %d 명이 타고있습니다.\n", subway_2);
	printf("지하철 3호차에 %d 명이 타고있습니다.\n", subway_3);*/

	//여러 개의 변수를 함께 동시에 생성
	/*int subway_array[3];
	subway_array[0] = 30;
	subway_array[1] = 40;
	subway_array[2] = 50;
	
	for (int i = 0; i < 3; i++) {
		printf("지하철 %d호차에 %d 명이 타고있습니다.\n", i + 1, subway_array[i]);
	}*/

	////값 설정 방법
	//int arr[10] = { 1,2,3,4,5,6,7,8,9,10 };  // 값을 늘 초기화 해야함
	//for (int i = 0; i < 10; i++) {
	//	printf("%d\n", arr[i]);
	//}
	
	//// 배열 크기는 항상 상수로 선언
	//int size = 10;
	//int arr[10];

	//int arr[10] = {1, 2};      // 3번째 값부터는 자동으로 '0'으로 초기화됨
	//for (int i = 0; i < 10; i++) {
	//	printf("%d\n", arr[i]);
	//}

	//int arr[] = { 1,2 };  //arr[2]

	/*float arr_f[5] = { 1.0f,2.0f,3.0f };
	for (int i = 0; i < 5; i++) {
		printf("%.2f\n", arr_f[i]);
	}*/

	// 문자 vs 문자열
	//char c = 'a';
	//printf("%c\n", c);
	
	/*char str[6] = "coding";*/ // [c][o][d][i][n][g]
	//문자열 끝에는 끝 을 의미하는 NULL문자 '\0'이 포함 되어야함
	//char str[7] = "coding"; // [c][o][d][i][n][g][\0]
	//printf("%s\n", str);

	//char str[] = "coding";
	///*printf("%s\n", str);
	//printf("%d\n", sizeof(str));*/

	//for (int i = 0; i < sizeof(str); i++) {
	//	printf("%c\n", str[i]);
	//}

	//char kor[] = "나도코딩";
	//printf("%s\n", kor);
	//printf("%d\n", sizeof(kor));
	//// 영어는 한글자 : 1byte(한칸)
	//// 한글은 한글자 : 2byte(두칸)

	/*char c_array[10] = { 'c','o','d','i','n','g','\0' };
	printf("%s\n", c_array);
	for (int i = 0; i < sizeof(c_array); i++) {
		printf("%c\n", c_array[i]);
	}*/

	









	return 0;
}