#include <stdio.h> 
#include <netdb.h> 
#include <netinet/in.h> 
#include <stdlib.h> 
#include <string.h> 
#include <sys/socket.h> 
#include <sys/types.h>
#include<unistd.h>
#define MAX 300 
#define PORT 8080 
#define SA struct sockaddr  
void get_matrix(int sockfd) 
{ 
	while(1)
	{
		int row_length, col_length, counter1, counter2;
		char string[MAX], *ptr; 
		bzero(string, MAX); 
		read(sockfd, string, sizeof(string));
		if(strncmp("exit",string,5) == 0)
			break;
		ptr = string;
		ptr++;
		row_length = (*ptr)%48;
		ptr+=2;
		col_length = (*ptr)%48;
		ptr+=4;
		int row_array[2][row_length], col_array[2][col_length];
		printf("LENGTH OF SUBSTRING: %d\n",row_length);
		for(counter1 = 0;counter1<row_length; counter1++, ptr+=2)
		{
			if(*ptr == '0')
				row_array[0][counter1] =0;
			else
				row_array[0][counter1] =1;
		}
		ptr+=4;
		for(counter1=0;counter1<col_length; counter1++, ptr+=2)
		{
			if(*ptr == '0')
				col_array[0][counter1] =0;
			else
				col_array[0][counter1] =1;
		}
		ptr+=4;
		for(counter1 = 0;counter1<row_length; counter1++, ptr+=2)
		{
			if(*ptr == '0')
				row_array[1][counter1] =0;
			else
				row_array[1][counter1] =1;	
		}
		ptr+=4;
		for(counter1=0;counter1<col_length; counter1++, ptr+=2)
		{
			if(*ptr == '0')
				col_array[1][counter1] =0;
			else
				col_array[1][counter1] =1;
		}
		ptr++;
		for(counter1=0;counter1<row_length;counter1++)
		if(row_array[0][counter1]!=row_array[1][counter1])
		{
			for(counter2=0;counter2<col_length;counter2++)
				if(col_array[0][counter2]!=col_array[1][counter2])
					break;
			break;
		}
		printf("ERROR AT: ARRAY[%d %d]\n", counter1,counter2);
		bzero(string, MAX);
		sprintf(string,"%d %d",counter1,counter2); 
		write(sockfd, string,5);
	}
} 

int main() 
{ 
	unsigned int sockfd, connfd, len; 
	struct sockaddr_in servaddr, cli; 

	sockfd = socket(AF_INET, SOCK_STREAM, 0); 
	if (sockfd == -1)
	{ 
		printf("ERROR:  SOCKET CREATION FAILED\n"); 
		exit(0); 
	} 
	else
		printf("MESSAGE:  SOCKET SUECESSFULLY CREATED\n"); 
	bzero(&servaddr, sizeof(servaddr)); 

	servaddr.sin_family=AF_INET; 
	servaddr.sin_addr.s_addr=htonl(INADDR_ANY); 
	servaddr.sin_port=htons(PORT); 

	if ((bind(sockfd, (SA*)&servaddr, sizeof(servaddr)))!=0)
	{ 
		printf("ERROR:  SOCKET BIND FAILED\n"); 
		exit(0); 
	} 
	else
		printf("MESSAGE:  SOCKE SUECESSFULLY BINDED\n"); 

	if ((listen(sockfd, 5))!=0) 
	{ 
		printf("ERROR:  LISTEN FAILED\n"); 
		exit(0); 
	} 
	else
		printf("MESSAGE:  SERVER IS LISTENING\n"); 
	len = sizeof(cli); 

	connfd = accept(sockfd, (SA*)&cli, &len); 
	if (connfd < 0) 
	{ 
		printf("ERROR: SERVER REJECTED THE CLIENT\n"); 
		exit(0); 
	} 
	else
		printf("MESSAGE:  SERVER ACCEPTED THE CLIENT\n"); 
	printf("\n");
	get_matrix(connfd); 
	close(sockfd); 
} 
