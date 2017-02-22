#include <stdio.h>
#include <sys/time.h>

int
main(int argc, char **argv) {
  struct timeval start, end;
  long mtime = 0, seconds, useconds;
  gettimeofday(&start, NULL);

  /*
  ** Insert code here.
  */
  for(int i = 99999999; i >= 0; i--){
    int a = 1;
    int b = 2;
    a = b;
  }

  gettimeofday(&end, NULL);
  seconds = end.tv_sec - start.tv_sec;
  useconds = end.tv_usec - start.tv_usec;

  mtime = ((seconds) * 1000 + useconds/1000.0) + 0.5;
  printf("Elapsed time: %ld milliseconds\n", mtime);
}
