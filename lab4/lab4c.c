#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>
#include <netdb.h> 
#include <sys/socket.h> 
#include<unistd.h>
#include <arpa/inet.h>
#define SA struct sockaddr 
#define PORT 8080 
int word_count(char *string)
{
	int counter=0;
	while(*string)
	{
		if(*string == ' ')
			counter++;
		string++;
	}
	return counter+1;
}
void print(int size, int array[size][7])
{
	for(int i=0; i<size; i++)
	{
		printf("[ ");
		for(int j=0; j<7; j++)
			printf("%d ",array[i][j]);
		printf("]\n");
	
	}
}

void send_and_recieve_matrix(int sockfd, int size, char string[],int array[size][7])
{
	int iterator = 0,row,column;
	write(sockfd,string,100);
	bzero(string, sizeof(string)); 
	read(sockfd, string, sizeof(string));
	row = string[0]%48;
	column =string[2]%48;
	printf("MESSAGE FROM THE SERVER:\n");
	printf("ERROR DETECTED AT: [%d %d]\n",row,column );
	printf("DAMAGED ARRAY:\n");
	print(size,array);
	if(array[row][column] == 0)
		array[row][column] = 1;
	else
		array[row][column] = 0;
	printf("\nREPAIRED ARRAY:\n");
	print(size,array);


}
void append_sizes(int size, char string[])
{
	char rowsize[3], colsize[3];
	sprintf(rowsize,"%d",size);
	sprintf(colsize,"%d",7);
	strcat(string,rowsize);
	strcat(string," ");
	strcat(string,colsize);
}
void generate_parity_bit_matrix(int size,int array[size][7], char string[])
{
	int sum, iterator1, iterator2;
	strcat(string,"\n[ ");
	for(iterator1=0; iterator1<size;iterator1++)
	{
		sum = 0;
		for(iterator2=0; iterator2<7;iterator2++)
			sum = sum + array[iterator1][iterator2];
		if(sum%2 == 0)
			strcat(string,"0 ");
		else
			strcat(string,"1 ");
	}
	strcat(string,"]\n");
	strcat(string,"[ ");
	for(iterator1=0; iterator1<7;iterator1++)
	{
		sum = 0;
		for(iterator2=0; iterator2<size;iterator2++)
			sum = sum + array[iterator2][iterator1];
		if(sum%2 == 0)
			strcat(string,"0 ");
		else
			strcat(string,"1 ");
	}
	strcat(string,"]");
}

void distort_array(int size, int array[size][7])
{
	int row_error, col_error;

	row_error = (rand()%(size));
	col_error = (rand()%7);
	printf("ERROR INDUCED AT: [%d %d]\n",row_error,col_error);
	if(array[row_error][col_error] == 1)
		array[row_error][col_error] =0;
	else
		array[row_error][col_error] = 1;
}

void convert_string_to_matrix(char* string, int size, int sockfd)
{
	int ascii, iterator1, iterator2=0, bit, array[size][7];
	char bit_message[200];
	while(*string)
	{
		ascii = (int)(*string);
		for (iterator1=6; iterator1>=0; iterator1--)
		{
			bit = ascii>>iterator1;
			if (bit & 1)
      			array[iterator2][6-iterator1]=1;
    		else
      			array[iterator2][6-iterator1]=0;
		}
		string++;
		iterator2++;
	}
	append_sizes(size, bit_message);
	generate_parity_bit_matrix(size,array,bit_message);
	distort_array(size, array);
	printf("PARITY MATRICES: \n");
	generate_parity_bit_matrix(size,array,bit_message);
	puts(bit_message);
	send_and_recieve_matrix(sockfd,size,bit_message,array);
}

void process_string(char *string, int sockfd)
{
	int iterator;
	char substring[10], *fptr, *bptr, end[5] = {'e','x','i','t','\0'};
	fptr = string;
	bptr = string;
	while(*fptr)
	{
		while(*fptr != ' ' && *fptr != '\0')
			fptr++;
		iterator = 0;
		while(bptr!= fptr)
		{
			substring[iterator] = *bptr;
			iterator++;
			bptr++;
		}
		substring[iterator] = '\0';
		printf("SUBSTRING: ");
		puts(substring);
		convert_string_to_matrix(substring, iterator, sockfd);
		if(*fptr == '\0')
			break;
		fptr++;
		bptr++;
	}
	write(sockfd,end,5);	
}

int main()
{
	int sockfd, connfd, number_of_words; 
	struct sockaddr_in servaddr, cli;
	char string[50];
	printf("ENTER A STRING: ");
	gets(string);
	number_of_words = word_count(string);
	sockfd = socket(AF_INET, SOCK_STREAM, 0); 
	if (sockfd == -1) 
	{ 
		printf("ERROR:  SOCKET CREATION FAILED\n"); 
		exit(0); 
	} 
	else
		printf("MESSAGE:  SOCKET SUECESSFULLY CREATED\n"); 
	bzero(&servaddr, sizeof(servaddr));  
	servaddr.sin_family = AF_INET; 
	servaddr.sin_addr.s_addr = inet_addr("127.0.0.1");
	servaddr.sin_port = htons(PORT); 
	if(connect(sockfd, (SA*)&servaddr, sizeof(servaddr)) != 0)
	{ 
		printf("ERROR:  CONNECTION TO SERVER FAILED\n"); 
		exit(0); 
	} 
	else
		printf("MESSAGE:  CONNECTED TO THE SERVER\n"); 
		printf("\n");
	

	process_string(string, sockfd);
	return 0;
}