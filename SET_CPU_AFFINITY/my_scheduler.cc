#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/time.h>
#include<sys/types.h>
#include<sys/sysinfo.h>
#include<time.h>

#include<sched.h>
#include<ctype.h>
#include<string.h>

int
main(int argc,char* argv[]) {    
  struct sched_param param;
  long int ret = 0;    
    
  cpu_set_t mask ;
  CPU_ZERO(&mask);
  CPU_SET(1,&mask);

  if (sched_setaffinity(0, sizeof(mask), &mask) == -1) {
    printf("warning: could not set CPU affinity, continuing...\n");
  }
    
  printf("current pid is %ld\n", getpid());
  sched_setaffinity(getpid(), sizeof(mask), &mask);
  sched_getaffinity(getpid(), sizeof(mask), &mask);
  printf("current cpu affinity mask is %d\n", mask);

/*
** CPU_ZERO(&mask);
*/

  CPU_CLR(1, &mask);
  CPU_SET(2, &mask);
    
  printf("current pid is %ld\n", getpid());
  sched_setaffinity(getpid(), sizeof(mask), &mask);
  sched_getaffinity(getpid(), sizeof(mask), &mask);
  printf("current cpu affinity mask is %d\n", mask);
    
  int sched_method = SCHED_FIFO;
  int sched_priority = sched_get_priority_max(SCHED_FIFO);

  param.sched_priority = sched_priority;
  ret = sched_setscheduler(getpid(), sched_method, &param);
  if (ret) {
    fprintf(stderr, "set scheduler to %ld, failed %m\n", getpid());
    return -4;
  }
    
  int scheduler = sched_getscheduler(getpid());
    
  fprintf(stderr, "The scheduler of PID(%ld) is %d, priority (%d)\n", getpid(), scheduler, sched_priority);    
  
  return 0;
}
