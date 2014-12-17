1 : #include <stdio.h>
2 : #include <stdlib.h>

3 : int main(int argc, char **argv)
4 : {
5 :   char *buf;
6 :
7 :   buf = malloc(1<<31);
8 :
9 :   fgets(buf, 1024, stdin);
10:   printf("%s\n", buf);
11:
12:   return 1;
13: }
