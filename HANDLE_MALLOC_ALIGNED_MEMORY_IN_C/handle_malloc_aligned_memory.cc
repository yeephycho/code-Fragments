#include <malloc.h>

void**
handleMalloc(size_t numBytes) {
  void **mem;
  mem = (void **)malloc(sizeof(char *));
  if(mem == NULL) {
    return (void **)NULL;
  }
  else {
    (*mem) = memalign(16, numBytes);
    if(*mem == NULL) {
      free(mem);
      return (void **)NULL;
    }
    else {
      return (void **)mem;
    }
  }
}

void
handleFree(void **hdl) {
    free((char *) *hdl);
    free((char **) hdl);
}

int
main(int argc, char **argv){
  int numbytes = 1024;
  char **blob;
  blob = (char **)handleMalloc(numbytes * sizeof(char));
  if(blob == NULL) {
    printf("Handle malloc failed!\n");
  }
  
  handleFree((void **)blob);

  return 0;
}
