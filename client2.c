#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>
#define port 21505

int main()
{
	int cSocket;
	int a, b, i, j, order;
	float det;
	struct sockaddr_in serverAddr;
	socklen_t addr_size;

	cSocket = socket(PF_INET, SOCK_DGRAM, 0);

	serverAddr.sin_family = AF_INET;
	serverAddr.sin_port = htons(port);
	serverAddr.sin_addr.s_addr = inet_addr("127.0.0.1");
	memset(serverAddr.sin_zero, '\0', sizeof serverAddr.sin_zero);

	addr_size = sizeof serverAddr;;

	printf("What order matrix would you like to use: \n");
	scanf("%d", &order);

	float matrix[order][order];
	printf("Please enter elements of matrix: \n");
	for(i=0; i<order; i++){
		for(j=0; j<order; j++){
			printf("? ");
			scanf("%f", &matrix[i][j]);

		}
	}

	printf("The matrix you input is: \n");
	for(a=0; a<order; a++){
		for(b=0; b<order; b++){
			printf("%.2f \t",matrix[a][b]);
		}
		printf("\n");
	}


	sendto(cSocket, &order, sizeof(order), 0, (struct sockaddr *) &serverAddr, addr_size);
	sendto(cSocket, matrix, sizeof(matrix), 0, (struct sockaddr *) &serverAddr, addr_size);

	recvfrom(cSocket, &det, sizeof(det), 0, (struct sockaddr *) &serverAddr, &addr_size);
	printf("The determinant of the matrix is: %.2f \n", det);

	close(cSocket);

	return 0;
}