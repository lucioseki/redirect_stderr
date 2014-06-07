#include <stdio.h>

void cfunc()
{
  fprintf(stderr, "%s: some annoying message\n", __FILE__);
}
