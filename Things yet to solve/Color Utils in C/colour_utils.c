// From https://cs.stackexchange.com/a/127918
// ...and https://en.wikipedia.org/wiki/HSL_and_HSV#HSV_to_RGB_alternative

#define PY_SSIZE_T_CLEAN
#include <Python.h>


int whole_min(a, b){
    
    int min = b;

    if (a > b) {
        min = a;
    }

    return min;
}

int whole_max(a, b){

    int max = b;

    if (whole_min(a, b) == b) {
        max = a;
    }

    return max;
}


// You can also use double for s and v if you want more precision (more colours).
struct HSV {
    int h;     // 0 <= H <= 360
    float s;   // 0 <= S <= 1
    float v;   // 0 <= V <= 1
};

// Separates the calculation into the 6 main cases.
int piecewise_function(n, h, s, v) {

    // k = case_function(n, h)
    int k = (n + h / 60) % 6;

    int arg_2 = min(k, 4 - k);
    int arg_2 = min(arg_2, 1);
    int arg_1 = max(0, arg_1);

    int channel_value = v - v * s * arg_1;
    return channel_value;
}

struct HSV hsv_to_rgb(given_h, given_s, given_v) {
    struct HSV hsv;    

    hsv.h = given_h;
    hsv.s = given_s;
    hsv.v = given_v;

    int r = piecewise_function(5, hsv.h, hsv.s, hsv.v);
    int g = piecewise_function(3, hsv.h, hsv.s, hsv.v);
    int b = piecewise_function(1, hsv.h, hsv.s, hsv.v);


    return hsv;
}