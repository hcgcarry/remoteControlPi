#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
int main(){
	pid_t pid;
	int n=0;
	for(n=0;n<16;n++){
		pid=fork();
	if(pid==-1){
		printf("fork failed\n");
		exit(-1);
	}
	else if(pid==0){
		printf("I am father\n");
	}
	else{
		printf("i am child\n");
		exit(0);
	}
	}
}
