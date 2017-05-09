#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>
#define port 21505

int order;
float calc_determinant(float matrix[order][order], int order);
float cofactor(float matrix[order][order], float ab[order][order], int rw, int cl, int ord);
int main()
{
	int mySocket, cSocket;
	int a, b, count, recv_len;
	float det;
	struct sockaddr_in serverAddr;
	struct sockaddr_in clientAddr;
	struct sockaddr_storage serverStorage;
	socklen_t addr_size;

	mySocket = socket(PF_INET, SOCK_DGRAM, 0);
	memset((char *)&serverAddr, 0, sizeof(serverAddr));
	serverAddr.sin_family = AF_INET;

	serverAddr.sin_port = htons(port);
	//serverAddr.sin_addr.s_addr = inet_addr(INADDR_ANY);
	serverAddr.sin_addr.s_addr = inet_addr("127.0.0.1");

	if(bind(mySocket, (struct sockaddr *)&serverAddr, sizeof(serverAddr)) < 0){
		printf("Unable to bind!!\n");
	}
	addr_size = sizeof(serverStorage);
	for(;;)
	{
		printf("Waiting on port %d\n", port);

		count = recvfrom(mySocket, &order, sizeof(order), 0, (struct sockaddr *)&serverStorage, &addr_size);

		float matrix[order][order];

		count = recvfrom(mySocket, matrix, sizeof(matrix), 0, (struct sockaddr *)&serverStorage, &addr_size);
		if(count > 0){
			printf("The matrix you received is: \n");
			for(a=0; a<order; a++){
				for(b=0; b<order; b++){
					printf("%.2f \t", matrix[a][b]);
				}
				printf("\n");
			}
		}
		else{
			printf("There was an error receiving data from the client!!\n");
		}

		det = calc_determinant(matrix, order);
		printf("The determinant is: %.2f \n", det);
		//write(cSocket, &det, sizeof(det));
		sendto(mySocket, &det, sizeof(det), 0,(struct sockaddr *) &serverStorage, addr_size);
		

		close(cSocket);
	}
	return 0;
}
float cofactor(float matrix[order][order], float ab[order][order], int rw, int cl, int ord)
{
	int a = 0, b = 0, row, col;

	for(row=0; row<ord; row++){
		for(col=0; col<ord; col++){
			if(row != rw && col != cl){
				ab[a][b++] = matrix[row][col];

				if(b == ord-1){
					b = 0;
					a++;
				}
			}
		}
	}
}

float calc_determinant(float matrix[order][order], int order)
{
	float det = 0;
	int c;

	if(order == 1){
		return matrix[0][0];
	}

	float ab[order-1][order-1];
	int sign = 1;

	for(c=0; c<order; c++){
		cofactor(matrix, ab, 0, c, order);
		det += sign * matrix[0][c] * calc_determinant(ab, order-1);

		sign = -sign;
	}
	return det;

}
